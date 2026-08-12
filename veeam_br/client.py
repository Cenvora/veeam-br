import importlib
import re
from datetime import datetime, timedelta, timezone
from json import JSONDecodeError
from typing import Any

# ----------------------------
# helpers
# ----------------------------


def _camel_to_snake(name: str) -> str:
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def _is_token(candidate: Any) -> bool:
    """Whether a create_token result is actually a token.

    The login operation returns a TokenModel on success, but an Error model for a
    documented failure such as 401, and None for an undocumented status. Reading
    .access_token off those raises AttributeError far from the real cause.
    """
    fields = ("access_token", "refresh_token", "expires_in")
    return all(hasattr(candidate, field) for field in fields)


def _describe_login_failure(result: Any) -> str:
    """Explain a create_token result that is not a token."""
    if result is None:
        return "the server returned no token and an unexpected status"

    message = getattr(result, "message", None)
    error_code = getattr(result, "error_code", None)
    if message or error_code:
        code = getattr(error_code, "value", error_code)
        return f"the server rejected the login: {message or ''} ({code})".replace(" ()", "")

    return f"the server returned {type(result).__name__} instead of a token"


# ----------------------------
# API namespace proxy
# ----------------------------


class ApiNamespace:
    """
    Lazy namespace for openapi-python-client operation modules.

    Example:
        vc.api("repositories").get_all_repositories
        → veeam_br.vX.api.repositories.get_all_repositories.asyncio
    """

    def __init__(self, client: "VeeamClient", base_module: str):
        self._client = client
        self._base = base_module

    def __getattr__(self, name: str):
        mod = importlib.import_module(f"{self._base}.{name}")
        return mod.asyncio


# ----------------------------
# main client
# ----------------------------


class VeeamClient:
    """
    Shared async client for versioned openapi-python-client SDKs.

    Responsibilities:
    - version routing
    - authentication
    - token refresh
    - x-api-version injection
    - API namespace routing
    """

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        api_version: str,
        verify_ssl: bool = True,
    ):
        self.host = host
        self.username = username
        self.password = password
        self.api_version = api_version
        self.verify_ssl = verify_ssl

        from .versions import VERSION_TO_PACKAGE

        if api_version not in VERSION_TO_PACKAGE:
            raise ValueError(f"Unsupported API version: {api_version}")

        self.package = VERSION_TO_PACKAGE[api_version]

        self._client = None
        self._access_token = None
        self._refresh_token = None
        self._expires_at: datetime | None = None

    # ----------------------------
    # connection + auth
    # ----------------------------

    async def connect(self):
        Client = getattr(importlib.import_module(f"{self.package}.client"), "Client")
        AuthenticatedClient = getattr(importlib.import_module(f"{self.package}.client"), "AuthenticatedClient")

        login_mod = importlib.import_module(f"{self.package}.api.login.create_token")
        create_token = getattr(login_mod, "asyncio")

        TokenLoginSpec = getattr(
            importlib.import_module(f"{self.package}.models.token_login_spec"),
            "TokenLoginSpec",
        )
        ELoginGrantType = getattr(
            importlib.import_module(f"{self.package}.models.e_login_grant_type"),
            "ELoginGrantType",
        )

        # unauthenticated client
        self._client = Client(
            base_url=self.host,
            verify_ssl=self.verify_ssl,
            headers={"x-api-version": self.api_version},
        )

        body = TokenLoginSpec(
            grant_type=ELoginGrantType.PASSWORD,
            username=self.username,
            password=self.password,
        )

        token = await create_token(
            client=self._client,
            body=body,
            x_api_version=self.api_version,
        )

        self._store_token(token, AuthenticatedClient)

    async def close(self):
        # openapi-python-client has no shared session to close
        pass

    # ----------------------------
    # token handling
    # ----------------------------

    def _store_token(self, token, AuthenticatedClient):
        if not _is_token(token):
            # Without this the next line raises AttributeError ("'Error' object has no
            # attribute 'access_token'"), which says nothing about the credentials being
            # refused. PermissionError lets a caller tell "wrong password" from
            # "server unreachable" and prompt for re-authentication.
            raise PermissionError(f"Veeam login failed: {_describe_login_failure(token)}")

        self._access_token = token.access_token
        self._refresh_token = token.refresh_token
        self._expires_at = datetime.now(timezone.utc) + timedelta(seconds=token.expires_in - 30)

        self._client = AuthenticatedClient(
            base_url=self.host,
            token=self._access_token,
            verify_ssl=self.verify_ssl,
            headers={"x-api-version": self.api_version},
        )

    async def _refresh_token_if_needed(self):
        if self._expires_at and datetime.now(timezone.utc) < self._expires_at:
            return

        if not self._refresh_token:
            # Nothing to refresh with — first use, or a session invalidated below
            await self.connect()
            return

        login_mod = importlib.import_module(f"{self.package}.api.login.create_token")
        create_token = getattr(login_mod, "asyncio")

        TokenLoginSpec = getattr(
            importlib.import_module(f"{self.package}.models.token_login_spec"),
            "TokenLoginSpec",
        )
        ELoginGrantType = getattr(
            importlib.import_module(f"{self.package}.models.e_login_grant_type"),
            "ELoginGrantType",
        )

        AuthenticatedClient = getattr(importlib.import_module(f"{self.package}.client"), "AuthenticatedClient")

        # Try the refresh grant first, then fall back to the password grant. A refresh
        # token expires or is revoked server-side, and the server reports that by
        # *returning* an Error rather than raising — so a non-token result has to fall
        # back just like an exception does, or every later call uses a stale token.
        token = None
        try:
            body = TokenLoginSpec(
                grant_type=ELoginGrantType.REFRESH_TOKEN,
                refresh_token=self._refresh_token,
            )
            token = await create_token(
                client=self._client,
                body=body,
                x_api_version=self.api_version,
            )
        except Exception:
            token = None

        if not _is_token(token):
            self._invalidate_session()
            await self.connect()
            return

        self._store_token(token, AuthenticatedClient)

    def _invalidate_session(self):
        """Forget the current token so the next call authenticates from scratch."""
        self._access_token = None
        self._refresh_token = None
        self._expires_at = None

    # ----------------------------
    # API access
    # ----------------------------

    def api(self, name: str) -> Any:
        """
        Smart API accessor.

        Examples:
            vc.api("repositories").get_all_repositories
            vc.api("repositories.get_all_repositories")
        """

        # direct operation
        if "." in name:
            mod = importlib.import_module(f"{self.package}.api.{name}")
            return mod.asyncio

        # namespace
        return ApiNamespace(self, f"{self.package}.api.{name}")

    async def call(self, fn, *args, **kwargs):
        """
        Wrap any API call with:
        - automatic token refresh
        - automatic x-api-version injection
        """
        await self._refresh_token_if_needed()

        if "x_api_version" not in kwargs:
            kwargs["x_api_version"] = self.api_version

        try:
            return await fn(client=self._client, *args, **kwargs)
        except JSONDecodeError as err:
            # VBR answers a rejected token with an empty body, which the generated parser
            # reports as "Expecting value: line 1 column 1 (char 0)" — the same error from
            # every endpoint until the process restarts. Drop the session so the next call
            # authenticates again.
            #
            # The call is deliberately not retried here: the operation may not be
            # idempotent (starting a job, for instance), and a body that failed to decode
            # is no proof the server did not act on it.
            self._invalidate_session()
            raise PermissionError(
                "Veeam returned an undecodable response, which usually means the session "
                f"was rejected; re-authenticating on the next call ({err})"
            ) from err
