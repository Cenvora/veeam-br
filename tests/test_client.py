import importlib

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
