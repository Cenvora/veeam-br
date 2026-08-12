"""Tests for API version detection.

Served against httpx.MockTransport, so the probing behaviour is exercised for real rather
than mocked out.
"""

import httpx
import pytest

from veeam_br.discovery import (
    RestApiEndpoint,
    detect_api_version,
    detect_rest_api,
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


# ---------------------------------------------------------------------------
# Endpoint detection: which port, and which version on it
#
# 13.1 serves the REST API on 443 and answers on 9419 too; older releases only have 9419,
# and Veeam has said 9419 will be removed in a future release.
# ---------------------------------------------------------------------------


def make_endpoint_client(served, fail_with=None):
    """A client whose server serves Swagger only at the given (port, version) pairs.

    httpx reports url.port as None for a scheme's default port, so an https URL written as
    ":443" arrives here with no port at all — hence the fallback. A real server still sees
    the TCP port it was reached on.
    """
    requested = []

    def port_of(request):
        return request.url.port or 443

    def handler(request):
        requested.append((port_of(request), str(request.url.path)))
        if fail_with is not None:
            raise fail_with
        for port, version in served:
            if (
                port_of(request) == port
                and request.url.path == f"/swagger/v{version}/swagger.json"
            ):
                return httpx.Response(200, json={"openapi": "3.0.1"})
        return httpx.Response(404)

    return httpx.AsyncClient(transport=httpx.MockTransport(handler)), requested


@pytest.mark.asyncio
async def test_prefers_443_when_a_server_answers_on_both():
    """A 13.1 server serves both; the modern port is the one to keep using."""
    client, _ = make_endpoint_client([(443, "1.3-rev2"), (9419, "1.3-rev2")])

    endpoint = await detect_rest_api("vbr.example.com", client=client)

    assert endpoint == RestApiEndpoint(port=443, api_version="1.3-rev2")


@pytest.mark.asyncio
async def test_finds_the_legacy_port_on_an_older_server():
    """Pre-13.1 servers have nothing on 443."""
    client, _ = make_endpoint_client([(9419, "1.3-rev0")])

    endpoint = await detect_rest_api("vbr.example.com", client=client)

    assert endpoint == RestApiEndpoint(port=9419, api_version="1.3-rev0")


@pytest.mark.asyncio
async def test_reports_the_newest_version_on_the_preferred_port():
    """Port preference comes first, then the newest version that port serves."""
    client, _ = make_endpoint_client(
        [(443, "1.3-rev1"), (443, "1.3-rev2"), (9419, "1.3-rev2")]
    )

    endpoint = await detect_rest_api("vbr.example.com", client=client)

    assert endpoint == RestApiEndpoint(port=443, api_version="1.3-rev2")


@pytest.mark.asyncio
async def test_port_order_is_the_callers_choice():
    """A caller that wants the legacy port checked first can say so."""
    client, _ = make_endpoint_client([(443, "1.3-rev2"), (9419, "1.3-rev2")])

    endpoint = await detect_rest_api(
        "vbr.example.com", ports=(9419, 443), client=client
    )

    assert endpoint.port == 9419


@pytest.mark.asyncio
async def test_probes_every_port_and_version_combination():
    client, requested = make_endpoint_client([])

    await detect_rest_api(
        "vbr.example.com", client=client, versions=["1.3-rev2", "1.2-rev1"]
    )

    assert sorted(requested) == sorted(
        [
            (port, f"/swagger/v{version}/swagger.json")
            for port in (443, 9419)
            for version in ("1.3-rev2", "1.2-rev1")
        ]
    )


@pytest.mark.asyncio
async def test_returns_none_when_no_port_answers():
    """Caller keeps whatever the user configured rather than guessing."""
    client, _ = make_endpoint_client([])

    assert await detect_rest_api("vbr.example.com", client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_the_host_is_unreachable():
    client, _ = make_endpoint_client([], fail_with=httpx.ConnectError("no route"))

    assert await detect_rest_api("vbr.example.com", client=client) is None


@pytest.mark.asyncio
async def test_no_ports_means_no_requests():
    client, requested = make_endpoint_client([])

    assert await detect_rest_api("vbr.example.com", ports=(), client=client) is None
    assert requested == []


@pytest.mark.asyncio
async def test_detected_endpoint_builds_a_working_base_url():
    """The result should drop straight into a VeeamClient host argument."""
    from veeam_br.client import VeeamClient

    client, _ = make_endpoint_client([(443, "1.3-rev2")])
    endpoint = await detect_rest_api("vbr.example.com", client=client)

    vc = VeeamClient(
        host=f"https://vbr.example.com{endpoint.base_url_suffix}",
        username="administrator",
        password="pw",
        api_version=endpoint.api_version,
    )
    assert vc.host == "https://vbr.example.com:443"
    assert vc.package == VERSION_TO_PACKAGE[endpoint.api_version]
