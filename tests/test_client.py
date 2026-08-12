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
