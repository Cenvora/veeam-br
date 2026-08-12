"""Tests for API version detection.

Served against httpx.MockTransport, so the probing behaviour is exercised for real rather
than mocked out.
"""

import httpx
import pytest

from veeam_br.discovery import (
    detect_api_version,
    newest_first,
    swagger_url,
)
from veeam_br.versions import VERSION_TO_PACKAGE

BASE_URL = "https://vbr.example.com:9419"


def make_client(served, status_for_unserved=404, fail_with=None):
    """An httpx client whose server serves Swagger only for `served` versions."""
    requested = []

    def handler(request):
        requested.append(str(request.url))
        if fail_with is not None:
            raise fail_with
        for version in served:
            if request.url.path == f"/swagger/v{version}/swagger.json":
                # Real documents are several MB; the body should never be needed
                return httpx.Response(200, json={"openapi": "3.0.1"})
        return httpx.Response(status_for_unserved)

    return httpx.AsyncClient(transport=httpx.MockTransport(handler)), requested


def test_swagger_url_adds_the_v_prefix():
    """Swagger paths carry a "v" that the x-api-version header does not."""
    assert (
        swagger_url(BASE_URL, "1.3-rev2")
        == f"{BASE_URL}/swagger/v1.3-rev2/swagger.json"
    )


def test_swagger_url_tolerates_a_trailing_slash():
    assert swagger_url(BASE_URL + "/", "1.2-rev1").count("//") == 1


@pytest.mark.parametrize(
    "versions,expected",
    [
        (["1.2-rev1", "1.3-rev2", "1.3-rev0"], ["1.3-rev2", "1.3-rev0", "1.2-rev1"]),
        # Numeric ordering, which string sorting would get wrong
        (["1.3-rev2", "1.3-rev10"], ["1.3-rev10", "1.3-rev2"]),
        (["1.3-rev0", "1.10-rev0"], ["1.10-rev0", "1.3-rev0"]),
        # Unrecognizable entries are dropped rather than ordered arbitrarily
        (["1.3-rev1", "nonsense", None, ""], ["1.3-rev1"]),
        ([], []),
    ],
)
def test_newest_first(versions, expected):
    assert newest_first(versions) == expected


@pytest.mark.asyncio
async def test_detects_the_newest_version_the_server_serves():
    client, _ = make_client(served=["1.2-rev1", "1.3-rev0"])

    detected = await detect_api_version(BASE_URL, client=client)

    assert detected == "1.3-rev0", "an older server must not be handed a newer revision"


@pytest.mark.asyncio
async def test_detects_the_newest_when_the_server_serves_everything():
    client, _ = make_client(served=list(VERSION_TO_PACKAGE))

    detected = await detect_api_version(BASE_URL, client=client)

    assert detected == newest_first(VERSION_TO_PACKAGE)[0]


@pytest.mark.asyncio
async def test_probes_only_versions_this_package_supports():
    """Reporting a version the SDK cannot speak would be useless to the caller."""
    client, requested = make_client(served=list(VERSION_TO_PACKAGE))

    await detect_api_version(BASE_URL, client=client)

    probed = {
        url.split("/swagger/v")[1].removesuffix("/swagger.json") for url in requested
    }
    assert probed == set(VERSION_TO_PACKAGE)


@pytest.mark.asyncio
async def test_candidate_list_can_be_narrowed():
    client, requested = make_client(served=["1.3-rev1"])

    detected = await detect_api_version(BASE_URL, client=client, versions=["1.3-rev1"])

    assert detected == "1.3-rev1"
    assert len(requested) == 1


@pytest.mark.asyncio
async def test_returns_none_when_no_version_answers():
    """The caller then falls back to a version of its own choosing."""
    client, _ = make_client(served=[])

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_swagger_is_gated():
    """Some deployments may require auth for the docs, or disable them."""
    client, _ = make_client(served=[], status_for_unserved=401)

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_the_server_is_unreachable():
    client, _ = make_client(served=[], fail_with=httpx.ConnectError("unreachable"))

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_a_probe_times_out():
    client, _ = make_client(served=[], fail_with=httpx.ReadTimeout("too slow"))

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_a_single_failing_probe_does_not_hide_the_others():
    """One version timing out must not lose a version that did answer."""
    calls = {"n": 0}

    def handler(request):
        if request.url.path == "/swagger/v1.3-rev2/swagger.json":
            raise httpx.ReadTimeout("too slow")
        if request.url.path == "/swagger/v1.3-rev1/swagger.json":
            calls["n"] += 1
            return httpx.Response(200, json={"openapi": "3.0.1"})
        return httpx.Response(404)

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))

    detected = await detect_api_version(BASE_URL, client=client)

    assert detected == "1.3-rev1"
    assert calls["n"] == 1


@pytest.mark.asyncio
async def test_empty_candidate_list_makes_no_requests():
    client, requested = make_client(served=[])

    assert await detect_api_version(BASE_URL, client=client, versions=[]) is None
    assert requested == []


@pytest.mark.asyncio
async def test_caller_supplied_client_is_left_open():
    """Reusing a caller's client must not close it out from under them."""
    client, _ = make_client(served=["1.3-rev1"])

    await detect_api_version(BASE_URL, client=client)

    assert not client.is_closed
    await client.aclose()


@pytest.mark.asyncio
async def test_detected_version_is_usable_with_veeam_client():
    """Detection is only useful if its result routes to a real SDK package."""
    from veeam_br.client import VeeamClient

    client, _ = make_client(served=list(VERSION_TO_PACKAGE))
    detected = await detect_api_version(BASE_URL, client=client)

    vc = VeeamClient(
        host=BASE_URL,
        username="administrator",
        password="pw",
        api_version=detected,
    )
    assert vc.package == VERSION_TO_PACKAGE[detected]
