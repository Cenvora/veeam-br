import asyncio
import importlib
import re
import ssl
from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone
from json import JSONDecodeError
from typing import Any

import httpx

from .exceptions import VeeamAuthenticationError, VeeamSessionError

# Seconds. Without a timeout httpx waits forever, so one hung server blocks the caller
# indefinitely.
DEFAULT_TIMEOUT = 30.0

# Failures to reach the server at all. These say nothing about the credentials, so they
# must not trigger a password fallback or be reported as an authentication error.
# asyncio.TimeoutError is only an alias of TimeoutError from 3.11.
_TRANSPORT_ERRORS = (httpx.HTTPError, OSError, TimeoutError, asyncio.TimeoutError)

# ----------------------------
# helpers
# ----------------------------


async def _aclose_generated_client(client: Any) -> None:
    """Close the httpx clients a generated Client/AuthenticatedClient created, if any.

    The generated clients create their httpx clients lazily and never close them, so
    every replaced client would otherwise leak a connection pool.
    """
    if client is None:
        return

    async_client = getattr(client, "_async_client", None)
    if async_client is not None:
        await async_client.aclose()

    sync_client = getattr(client, "_client", None)
    if isinstance(sync_client, httpx.Client):
        sync_client.close()


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
    - token refresh (serialised, so concurrent calls refresh once)
    - x-api-version injection
    - API namespace routing

    Usable as an async context manager; leaving the block closes the client.

    Errors:
    - ``VeeamAuthenticationError`` (a ``PermissionError``): the password login was refused.
    - ``VeeamSessionError`` (a ``PermissionError``): the session was rejected mid-use; the
      next call re-authenticates.
    - Transport errors (``httpx.HTTPError``, ``OSError``, ``TimeoutError``) propagate as-is.
    """

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        api_version: str,
        verify_ssl: bool | ssl.SSLContext | str = True,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
    ):
        self.host = host
        self.username = username
        self.password = password
        self.api_version = api_version
        self.verify_ssl = verify_ssl
        # None is an explicit opt-out: httpx then waits indefinitely.
        self.timeout: httpx.Timeout | None = (
            timeout if timeout is None or isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)
        )

        from .versions import VERSION_TO_PACKAGE

        if api_version not in VERSION_TO_PACKAGE:
            raise ValueError(f"Unsupported API version: {api_version}")

        self.package = VERSION_TO_PACKAGE[api_version]

        self._client = None
        self._access_token = None
        self._refresh_token = None
        self._expires_at: datetime | None = None

        # Serialises authentication so a poll and a user action that both find the token
        # expired refresh it once, rather than both spending the same refresh token.
        # asyncio.Lock binds to a loop on first use (3.10+), so constructing it here is
        # safe outside a running loop.
        self._auth_lock = asyncio.Lock()
        self._auth_owner: asyncio.Task | None = None

    async def __aenter__(self) -> "VeeamClient":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

    # ----------------------------
    # connection + auth
    # ----------------------------

    @asynccontextmanager
    async def _auth_guard(self):
        """Hold the auth lock, unless the current task already holds it.

        asyncio.Lock is not reentrant, and the refresh path calls connect() while
        holding it.
        """
        current = asyncio.current_task()
        if current is not None and self._auth_owner is current:
            yield
            return

        async with self._auth_lock:
            self._auth_owner = current
            try:
                yield
            finally:
                self._auth_owner = None

    async def connect(self):
        """Log in with the password grant.

        Raises VeeamAuthenticationError if the server refuses the credentials. Transport
        errors propagate unchanged.
        """
        async with self._auth_guard():
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

            # unauthenticated client; replacing it closes whatever it supersedes
            await self._replace_client(
                Client(
                    base_url=self.host,
                    verify_ssl=self.verify_ssl,
                    timeout=self.timeout,
                    headers={"x-api-version": self.api_version},
                )
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

            await _aclose_generated_client(self._store_token(token, AuthenticatedClient))

    async def close(self):
        """Close the underlying HTTP connection pool and forget the session."""
        async with self._auth_guard():
            previous, self._client = self._client, None
            self._invalidate_session()
            await _aclose_generated_client(previous)

    async def _replace_client(self, new_client):
        previous, self._client = self._client, new_client
        await _aclose_generated_client(previous)

    # ----------------------------
    # token handling
    # ----------------------------

    def _store_token(self, token, AuthenticatedClient):
        """Record a login result and switch to an authenticated client.

        Returns the generated client it replaced, which the caller must close — closing
        is async and this stays sync.
        """
        if not _is_token(token):
            # Without this the next line raises AttributeError ("'Error' object has no
            # attribute 'access_token'"), which says nothing about the credentials being
            # refused. A distinct error lets a caller tell "wrong password" from
            # "server unreachable" and prompt for re-authentication.
            self._invalidate_session()
            raise VeeamAuthenticationError(f"Veeam login failed: {_describe_login_failure(token)}")

        self._access_token = token.access_token
        self._refresh_token = token.refresh_token
        self._expires_at = datetime.now(timezone.utc) + timedelta(seconds=token.expires_in - 30)

        previous = self._client
        self._client = AuthenticatedClient(
            base_url=self.host,
            token=self._access_token,
            verify_ssl=self.verify_ssl,
            timeout=self.timeout,
            headers={"x-api-version": self.api_version},
        )
        return previous

    def _session_is_current(self) -> bool:
        return self._expires_at is not None and datetime.now(timezone.utc) < self._expires_at

    async def _refresh_token_if_needed(self):
        if self._session_is_current():
            return

        async with self._auth_guard():
            # Another caller may have refreshed while this one waited for the lock.
            if self._session_is_current():
                return
            await self._refresh_locked()

    async def _refresh_locked(self):
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
        #
        # Transport errors are the exception: the server was not reached, so the refresh
        # token may still be good, and a password login would only fail the same way.
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
        except _TRANSPORT_ERRORS:
            raise
        except Exception:
            token = None

        if not _is_token(token):
            self._invalidate_session()
            await self.connect()
            return

        await _aclose_generated_client(self._store_token(token, AuthenticatedClient))

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
            raise VeeamSessionError(
                "Veeam returned an undecodable response, which usually means the session "
                f"was rejected; re-authenticating on the next call ({err})"
            ) from err
