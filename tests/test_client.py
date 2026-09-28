import asyncio
import importlib
import ssl

import httpx
import pytest

from veeam_br.client import VeeamClient, _camel_to_snake
from veeam_br.versions import VERSION_TO_PACKAGE


def make_client(api_version="1.3-rev2", **kwargs):
    return VeeamClient(
        host="https://vbr.example.com:9419",
        username="administrator",
        password="SuperSecretPassword",
        api_version=api_version,
        **kwargs,
    )


@pytest.mark.parametrize("version,package", sorted(VERSION_TO_PACKAGE.items()))
def test_routes_to_version_package(version, package):
    assert make_client(version).package == package


def test_rejects_unsupported_version():
    with pytest.raises(ValueError, match="Unsupported API version"):
        make_client("1.1-rev0")


def test_defaults_to_verifying_ssl():
    assert make_client().verify_ssl is True
    assert make_client(verify_ssl=False).verify_ssl is False


def test_starts_unauthenticated():
    vc = make_client()
    assert vc._client is None
    assert vc._access_token is None
    assert vc._expires_at is None


def test_namespace_resolves_operation():
    vc = make_client()
    assert callable(vc.api("repositories").get_all_repositories)


def test_dotted_path_resolves_operation():
    vc = make_client()
    dotted = vc.api("repositories.get_all_repositories")
    namespaced = vc.api("repositories").get_all_repositories
    assert dotted is namespaced


def test_unknown_operation_raises():
    vc = make_client()
    with pytest.raises(ModuleNotFoundError):
        vc.api("repositories").no_such_operation


@pytest.mark.parametrize(
    "camel,snake",
    [
        ("getAllRepositories", "get_all_repositories"),
        ("BackupObjects", "backup_objects"),
        ("createHTTPToken", "create_http_token"),
        ("already_snake", "already_snake"),
    ],
)
def test_camel_to_snake(camel, snake):
    assert _camel_to_snake(camel) == snake


def test_store_token_records_aware_expiry():
    """Expiry is compared against datetime.now(timezone.utc); a naive value
    would raise TypeError on the next refresh check."""
    from datetime import datetime, timedelta, timezone

    class FakeToken:
        access_token = "access"
        refresh_token = "refresh"
        expires_in = 900

    vc = make_client()
    before = datetime.now(timezone.utc)
    vc._store_token(FakeToken(), lambda **kwargs: object())

    assert vc._expires_at.tzinfo is not None
    # 900s lifetime minus the 30s safety margin
    assert before + timedelta(seconds=869) < vc._expires_at < before + timedelta(seconds=871)


@pytest.mark.asyncio
async def test_call_injects_api_version_and_client():
    vc = make_client()
    vc._client = object()
    vc._expires_at = _far_future()

    captured = {}

    async def fake_operation(**kwargs):
        captured.update(kwargs)
        return "ok"

    assert await vc.call(fake_operation) == "ok"
    assert captured["x_api_version"] == "1.3-rev2"
    assert captured["client"] is vc._client


@pytest.mark.asyncio
async def test_call_respects_explicit_api_version():
    vc = make_client()
    vc._client = object()
    vc._expires_at = _far_future()

    captured = {}

    async def fake_operation(**kwargs):
        captured.update(kwargs)

    await vc.call(fake_operation, x_api_version="1.3-rev0")
    assert captured["x_api_version"] == "1.3-rev0"


def _far_future():
    """Timezone-aware UTC, matching how VeeamClient stores token expiry."""
    from datetime import datetime, timedelta, timezone

    return datetime.now(timezone.utc) + timedelta(hours=1)


# ---------------------------------------------------------------------------
# Token handling when the server refuses the login
#
# create_token returns an Error model for a documented failure (401) and None for an
# undocumented status; it does not raise. Treating either as a token used to surface as
# "'Error' object has no attribute 'access_token'" from deep inside a refresh, and left
# every later call using a dead token.
# See https://github.com/Cenvora/ha-veeam-br/issues/82
# ---------------------------------------------------------------------------


class FakeError:
    """Shaped like the generated Error model."""

    def __init__(self, message="Unauthorized", error_code="unauthorized"):
        self.message = message
        self.error_code = error_code


class FakeToken:
    def __init__(self, access_token="access", refresh_token="refresh", expires_in=900):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = expires_in


def _fake_authenticated_client(**kwargs):
    return object()


@pytest.mark.parametrize(
    "result",
    [FakeError(), None, object()],
    ids=["error-model", "no-token", "unexpected-object"],
)
def test_store_token_rejects_non_tokens(result):
    vc = make_client()

    with pytest.raises(PermissionError, match="Veeam login failed"):
        vc._store_token(result, _fake_authenticated_client)

    assert vc._access_token is None, "a refused login must not look authenticated"
    assert vc._expires_at is None


def test_store_token_reports_the_server_message():
    vc = make_client()

    with pytest.raises(PermissionError, match="wrong credentials"):
        vc._store_token(FakeError(message="wrong credentials"), _fake_authenticated_client)


@pytest.mark.asyncio
async def test_refresh_falls_back_to_password_when_refresh_is_refused(monkeypatch):
    """A revoked refresh token comes back as an Error, not an exception."""
    vc = make_client()
    vc._client = object()
    vc._access_token = "stale"
    vc._refresh_token = "revoked"
    vc._expires_at = None  # expired

    connected = []

    async def fake_connect():
        connected.append(True)
        vc._access_token = "fresh"

    monkeypatch.setattr(vc, "connect", fake_connect)
    monkeypatch.setattr(
        "veeam_br.client.importlib.import_module",
        _refusing_login_modules(),
    )

    await vc._refresh_token_if_needed()

    assert connected, "a refused refresh should re-authenticate with the password grant"
    assert vc._access_token == "fresh"


@pytest.mark.asyncio
async def test_refresh_connects_when_there_is_no_refresh_token(monkeypatch):
    vc = make_client()
    connected = []

    async def fake_connect():
        connected.append(True)

    monkeypatch.setattr(vc, "connect", fake_connect)

    await vc._refresh_token_if_needed()

    assert connected, "with no token to refresh, it should connect from scratch"


@pytest.mark.asyncio
async def test_call_invalidates_session_on_undecodable_response():
    """An empty body from a rejected token must not poison every later call."""
    from json import JSONDecodeError

    vc = make_client()
    vc._client = object()
    vc._access_token = "stale"
    vc._refresh_token = "stale-refresh"
    vc._expires_at = _far_future()

    async def fake_operation(**kwargs):
        raise JSONDecodeError("Expecting value", "", 0)

    with pytest.raises(PermissionError, match="undecodable response"):
        await vc.call(fake_operation)

    assert vc._access_token is None, "the dead session should be dropped"
    assert vc._refresh_token is None
    assert vc._expires_at is None


@pytest.mark.asyncio
async def test_call_does_not_retry_the_operation():
    """Retrying could repeat a non-idempotent operation such as starting a job."""
    from json import JSONDecodeError

    vc = make_client()
    vc._client = object()
    vc._expires_at = _far_future()

    calls = []

    async def fake_operation(**kwargs):
        calls.append(True)
        raise JSONDecodeError("Expecting value", "", 0)

    with pytest.raises(PermissionError):
        await vc.call(fake_operation)

    assert len(calls) == 1, "the operation must be attempted exactly once"


def _refusing_login_modules():
    """Stand in for importlib.import_module so the refresh grant is refused."""
    real_import = importlib.import_module

    class FakeCreateToken:
        @staticmethod
        async def asyncio(**kwargs):
            return FakeError()

    class FakeSpec:
        def __init__(self, **kwargs):
            pass

    class FakeGrantType:
        REFRESH_TOKEN = "refresh_token"
        PASSWORD = "password"

    def fake_import(name):
        if name.endswith(".api.login.create_token"):
            return FakeCreateToken
        if name.endswith(".models.token_login_spec"):
            return type("M", (), {"TokenLoginSpec": FakeSpec})
        if name.endswith(".models.e_login_grant_type"):
            return type("M", (), {"ELoginGrantType": FakeGrantType})
        if name.endswith(".client"):
            return type(
                "M",
                (),
                {
                    "Client": lambda **kw: object(),
                    "AuthenticatedClient": _fake_authenticated_client,
                },
            )
        return real_import(name)

    return fake_import


# ---------------------------------------------------------------------------
# Error types
#
# Integrations need to tell "the password was refused" (ask the user for new credentials)
# from "the session was dropped" (retry; the next call logs in again) from "the server
# could not be reached" (transient). All three used to arrive as a bare PermissionError or
# were swallowed into a password fallback.
# ---------------------------------------------------------------------------


def test_exception_hierarchy():
    from veeam_br.exceptions import VeeamAuthenticationError, VeeamError, VeeamSessionError

    for cls in (VeeamAuthenticationError, VeeamSessionError):
        assert issubclass(cls, VeeamError)
        assert issubclass(cls, PermissionError), "existing PermissionError handlers must keep working"
    assert not issubclass(VeeamAuthenticationError, VeeamSessionError)
    assert not issubclass(VeeamSessionError, VeeamAuthenticationError)


def test_store_token_raises_authentication_error():
    from veeam_br.exceptions import VeeamAuthenticationError

    vc = make_client()
    with pytest.raises(VeeamAuthenticationError, match="Veeam login failed"):
        vc._store_token(FakeError(), _fake_authenticated_client)


@pytest.mark.asyncio
async def test_call_raises_session_error_on_undecodable_response():
    from json import JSONDecodeError

    from veeam_br.exceptions import VeeamAuthenticationError, VeeamSessionError

    vc = make_client()
    vc._client = object()
    vc._expires_at = _far_future()

    async def fake_operation(**kwargs):
        raise JSONDecodeError("Expecting value", "", 0)

    with pytest.raises(VeeamSessionError) as excinfo:
        await vc.call(fake_operation)

    assert isinstance(excinfo.value, PermissionError)
    assert not isinstance(excinfo.value, VeeamAuthenticationError), "a dropped session is not bad credentials"


class FakeAsyncHttpx:
    def __init__(self):
        self.closed = False

    async def aclose(self):
        self.closed = True


class RecordingClient:
    """Stands in for a generated Client/AuthenticatedClient."""

    instances: list

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self._async_client = FakeAsyncHttpx()
        type(self).instances.append(self)


def _login_modules(create_token, instances):
    """Stand in for importlib.import_module with a scripted create_token.

    create_token receives the grant type and returns (or raises) the login result.
    Every generated client constructed is appended to ``instances``.
    """
    real_import = importlib.import_module

    class Spec:
        def __init__(self, **kwargs):
            self.grant_type = kwargs["grant_type"]

    class GrantType:
        REFRESH_TOKEN = "refresh_token"
        PASSWORD = "password"

    class CreateToken:
        @staticmethod
        async def asyncio(*, client, body, x_api_version):
            return await create_token(body.grant_type)

    client_cls = type("Client", (RecordingClient,), {"instances": instances})
    auth_cls = type("AuthenticatedClient", (RecordingClient,), {"instances": instances})

    def fake_import(name):
        if name.endswith(".api.login.create_token"):
            return CreateToken
        if name.endswith(".models.token_login_spec"):
            return type("M", (), {"TokenLoginSpec": Spec})
        if name.endswith(".models.e_login_grant_type"):
            return type("M", (), {"ELoginGrantType": GrantType})
        if name.endswith(".client"):
            return type("M", (), {"Client": client_cls, "AuthenticatedClient": auth_cls})
        return real_import(name)

    return fake_import


def _expired_session(vc):
    vc._client = None
    vc._access_token = "stale"
    vc._refresh_token = "refresh"
    vc._expires_at = None


@pytest.mark.asyncio
async def test_password_login_refused_raises_authentication_error(monkeypatch):
    from veeam_br.exceptions import VeeamAuthenticationError

    async def create_token(grant):
        return FakeError(message="bad password")

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, []))

    vc = make_client()
    with pytest.raises(VeeamAuthenticationError, match="bad password"):
        await vc.connect()
    assert vc._access_token is None


@pytest.mark.asyncio
async def test_refused_refresh_then_refused_password_raises_authentication_error(monkeypatch):
    from veeam_br.exceptions import VeeamAuthenticationError

    grants = []

    async def create_token(grant):
        grants.append(grant)
        return FakeError()

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, []))

    vc = make_client()
    _expired_session(vc)
    with pytest.raises(VeeamAuthenticationError):
        await vc._refresh_token_if_needed()
    assert grants == ["refresh_token", "password"]


@pytest.mark.asyncio
async def test_non_transport_refresh_exception_falls_back_to_password(monkeypatch):
    grants = []

    async def create_token(grant):
        grants.append(grant)
        if grant == "refresh_token":
            raise ValueError("unparseable refresh response")
        return FakeToken(access_token="fresh")

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, []))

    vc = make_client()
    _expired_session(vc)
    await vc._refresh_token_if_needed()
    assert grants == ["refresh_token", "password"]
    assert vc._access_token == "fresh"


TRANSPORT_ERRORS = [
    httpx.ConnectError("connection refused"),
    httpx.ReadTimeout("read timed out"),
    OSError("network unreachable"),
    TimeoutError(),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("error", TRANSPORT_ERRORS, ids=lambda e: type(e).__name__)
async def test_transport_error_during_refresh_propagates(monkeypatch, error):
    """An unreachable server is not a refused refresh token: no password fallback."""
    from veeam_br.exceptions import VeeamError

    grants = []

    async def create_token(grant):
        grants.append(grant)
        raise error

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, []))

    vc = make_client()
    _expired_session(vc)
    with pytest.raises(type(error)) as excinfo:
        await vc._refresh_token_if_needed()

    assert excinfo.value is error
    assert not isinstance(excinfo.value, VeeamError)
    assert grants == ["refresh_token"], "a transport failure must not fall back to the password grant"
    assert vc._refresh_token == "refresh", "the refresh token may still be good"


@pytest.mark.asyncio
@pytest.mark.parametrize("error", TRANSPORT_ERRORS, ids=lambda e: type(e).__name__)
async def test_transport_error_during_login_propagates(monkeypatch, error):
    from veeam_br.exceptions import VeeamError

    async def create_token(grant):
        raise error

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, []))

    vc = make_client()
    with pytest.raises(type(error)) as excinfo:
        await vc.connect()
    assert excinfo.value is error
    assert not isinstance(excinfo.value, VeeamError)


@pytest.mark.asyncio
async def test_transport_error_during_fallback_login_propagates(monkeypatch):
    """Refresh refused, then the password login cannot reach the server."""
    from veeam_br.exceptions import VeeamError

    error = httpx.ConnectError("connection refused")

    async def create_token(grant):
        if grant == "refresh_token":
            return FakeError()
        raise error

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, []))

    vc = make_client()
    _expired_session(vc)
    with pytest.raises(httpx.ConnectError) as excinfo:
        await vc._refresh_token_if_needed()
    assert excinfo.value is error
    assert not isinstance(excinfo.value, VeeamError)


@pytest.mark.asyncio
async def test_concurrent_calls_refresh_once(monkeypatch):
    """A poll and a button press that both find the token expired must not both
    spend the same refresh token."""
    grants = []
    release = asyncio.Event()

    async def create_token(grant):
        grants.append(grant)
        await release.wait()
        return FakeToken(access_token="fresh")

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, []))

    vc = make_client()
    _expired_session(vc)

    async def fake_operation(**kwargs):
        return kwargs["client"]

    tasks = [asyncio.create_task(vc.call(fake_operation)) for _ in range(5)]
    for _ in range(5):
        await asyncio.sleep(0)
    release.set()
    results = await asyncio.gather(*tasks)

    assert grants == ["refresh_token"]
    assert all(r is vc._client for r in results)


@pytest.mark.asyncio
async def test_concurrent_first_calls_log_in_once(monkeypatch):
    grants = []

    async def create_token(grant):
        grants.append(grant)
        await asyncio.sleep(0)
        return FakeToken()

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, []))

    vc = make_client()

    async def fake_operation(**kwargs):
        return "ok"

    await asyncio.gather(*(vc.call(fake_operation) for _ in range(5)))
    assert grants == ["password"]


def test_client_can_be_constructed_outside_a_running_loop():
    """The auth lock is created in __init__, which runs outside any loop here."""
    vc = make_client()

    async def use():
        async with vc._auth_lock:
            return True

    assert asyncio.run(use())


@pytest.mark.asyncio
async def test_connect_closes_replaced_clients(monkeypatch):
    instances = []

    async def create_token(grant):
        return FakeToken()

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, instances))

    vc = make_client()
    await vc.connect()
    first_auth = vc._client
    await vc.connect()

    # each connect builds an unauthenticated client and then an authenticated one
    assert len(instances) == 4
    assert all(c._async_client.closed for c in instances[:3])
    assert first_auth._async_client.closed
    assert not vc._client._async_client.closed, "the live client must stay open"


@pytest.mark.asyncio
async def test_refresh_closes_replaced_client(monkeypatch):
    instances = []

    async def create_token(grant):
        return FakeToken(access_token=grant)

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, instances))

    vc = make_client()
    await vc.connect()
    before = vc._client
    vc._expires_at = None
    await vc._refresh_token_if_needed()

    assert vc._access_token == "refresh_token"
    assert vc._client is not before
    assert before._async_client.closed
    assert not vc._client._async_client.closed


@pytest.mark.asyncio
async def test_closing_skips_clients_that_never_opened_a_connection():
    """The generated clients create their httpx client lazily."""
    vc = make_client()
    unused = RecordingClient.__new__(RecordingClient)
    unused._async_client = None
    vc._client = unused
    await vc.close()
    assert vc._client is None


@pytest.mark.asyncio
async def test_close_closes_client_and_invalidates_session():
    vc = make_client()
    live = RecordingClient.__new__(RecordingClient)
    live._async_client = FakeAsyncHttpx()
    vc._client = live
    vc._access_token = "access"
    vc._refresh_token = "refresh"
    vc._expires_at = _far_future()

    await vc.close()

    assert live._async_client.closed
    assert vc._client is None
    assert vc._access_token is None
    assert vc._refresh_token is None
    assert vc._expires_at is None


@pytest.mark.asyncio
async def test_async_context_manager_closes():
    vc = make_client()
    live = RecordingClient.__new__(RecordingClient)
    live._async_client = FakeAsyncHttpx()
    vc._client = live

    async with vc as entered:
        assert entered is vc

    assert live._async_client.closed
    assert vc._client is None


# ---------------------------------------------------------------------------
# Timeouts
#
# The generated clients default to timeout=None, which httpx treats as "wait forever":
# one hung server blocked the caller indefinitely.
# ---------------------------------------------------------------------------


def test_default_timeout():
    assert make_client().timeout == httpx.Timeout(30.0)


def test_float_timeout_is_converted():
    assert make_client(timeout=5).timeout == httpx.Timeout(5)


def test_timeout_object_is_kept():
    custom = httpx.Timeout(10.0, connect=3.0)
    assert make_client(timeout=custom).timeout is custom


def test_timeout_none_opts_out():
    assert make_client(timeout=None).timeout is None


@pytest.mark.asyncio
async def test_timeout_and_ssl_reach_every_generated_client(monkeypatch):
    instances = []

    async def create_token(grant):
        return FakeToken()

    monkeypatch.setattr("veeam_br.client.importlib.import_module", _login_modules(create_token, instances))

    ctx = ssl.create_default_context()
    vc = make_client(timeout=7.5, verify_ssl=ctx)
    await vc.connect()
    vc._expires_at = None
    await vc._refresh_token_if_needed()

    assert len(instances) == 3  # unauthenticated, authenticated, refreshed
    for instance in instances:
        assert instance.kwargs["timeout"] == httpx.Timeout(7.5)
        assert instance.kwargs["verify_ssl"] is ctx


@pytest.mark.asyncio
@pytest.mark.parametrize("package", sorted(set(VERSION_TO_PACKAGE.values())))
async def test_real_generated_clients_apply_timeout(monkeypatch, package):
    """The generated clients hand timeout= through to the httpx client they build,
    and close() closes that httpx client."""
    version = next(v for v, p in VERSION_TO_PACKAGE.items() if p == package)
    real_import = importlib.import_module

    class CreateToken:
        @staticmethod
        async def asyncio(**kwargs):
            return FakeToken()

    def fake_import(name):
        if name.endswith(".api.login.create_token"):
            return CreateToken
        return real_import(name)

    monkeypatch.setattr("veeam_br.client.importlib.import_module", fake_import)

    vc = make_client(version, timeout=4.0)
    await vc.connect()

    httpx_client = vc._client.get_async_httpx_client()
    assert httpx_client.timeout == httpx.Timeout(4.0)

    await vc.close()
    assert httpx_client.is_closed
