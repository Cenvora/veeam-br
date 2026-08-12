"""Detect which REST API version a Veeam Backup & Replication server offers.

The REST API has no endpoint that reports its own supported versions — every request must
carry an ``x-api-version`` header, and Veeam's guidance is that the caller chooses:

    "you should be picking the API version you plan to use for your production code, the
    API cannot (and will not) decide for you"

What a server does expose is one Swagger document per version it serves, so probing
``/swagger/v{version}/swagger.json`` reveals the set. VeeamHub's config collector uses the
same approach:
https://github.com/VeeamHub/veeam-config-collector/blob/master/Veeam_Config_Collector.ps1

``detect_api_version`` intersects that with the versions this package can actually speak
(``VERSION_TO_PACKAGE``) and returns the newest one, so the answer is always a version the
caller can pass straight to ``VeeamClient``.

Detection is best-effort: Swagger endpoints may be unreachable, disabled, or gated, and any
of those cases returns None so the caller can fall back to a version of its own choosing
rather than failing outright.
"""

import asyncio
import logging
from collections.abc import Iterable, Sequence
from typing import NamedTuple

import httpx

from .versions import VERSION_TO_PACKAGE

_LOGGER = logging.getLogger(__name__)

# Probes run concurrently, so this bounds the whole detection rather than each version
DEFAULT_TIMEOUT = 8.0

# Swagger paths carry a "v" prefix that the x-api-version header does not: version
# "1.3-rev2" is documented at /swagger/v1.3-rev2/swagger.json
SWAGGER_PATH = "/swagger/v{version}/swagger.json"

# Ports the REST API is reachable on, most current first. 13.1 serves it on 443 and answers
# on 9419 too for backward compatibility; 9419 is the only port on older releases and Veeam
# has said it will be removed in a future release.
REST_PORT = 443
LEGACY_REST_PORT = 9419
DEFAULT_PORTS = (REST_PORT, LEGACY_REST_PORT)


class RestApiEndpoint(NamedTuple):
    """Where a server's REST API answers."""

    port: int
    api_version: str

    @property
    def base_url_suffix(self) -> str:
        """Port suffix for building a base URL, e.g. ":443"."""
        return f":{self.port}"


def swagger_url(base_url: str, version: str) -> str:
    """Build the Swagger document URL for one API version."""
    return f"{base_url.rstrip('/')}{SWAGGER_PATH.format(version=version)}"


def newest_first(versions: Iterable[str]) -> list[str]:
    """Order API versions newest first, dropping any that are not recognizable.

    Versions look like "1.3-rev2". Comparing the numbers rather than the strings keeps a
    hypothetical "1.10-rev0" above "1.3-rev0" instead of below it.
    """

    def key(version):
        try:
            head, _, revision = version.partition("-rev")
            major, _, minor = head.partition(".")
            return (int(major), int(minor), int(revision))
        except (AttributeError, TypeError, ValueError):
            return None

    # Filter before sorting: an unrecognizable entry has no key to compare, and mixing
    # those into the sort raises rather than just ordering them last
    ranked = [(key(version), version) for version in versions]
    return [version for _, version in sorted((r for r in ranked if r[0]), reverse=True)]


async def _serves(client, base_url: str, version: str, timeout: float):
    """Return the version if the server serves its Swagger document, else None."""
    url = swagger_url(base_url, version)
    try:
        # Streamed so only the status line is needed; these documents are several MB
        async with client.stream("GET", url, timeout=timeout) as response:
            if response.status_code == 200:
                return version
            _LOGGER.debug("%s returned HTTP %s", url, response.status_code)
            return None
    except Exception as err:
        _LOGGER.debug("%s did not answer: %s", url, err)
        return None


async def detect_api_version(
    base_url: str,
    *,
    verify_ssl: bool = True,
    timeout: float = DEFAULT_TIMEOUT,
    versions: Sequence[str] | None = None,
    client: "httpx.AsyncClient | None" = None,
) -> str | None:
    """Return the newest API version this server serves and this package supports.

    Args:
        base_url: Server base URL, e.g. "https://vbr.example.com:9419".
        verify_ssl: Whether to verify the server certificate. Ignored when ``client`` is
            given, since the caller's client carries its own settings.
        timeout: Per-request timeout in seconds. Probes are concurrent.
        versions: Candidate versions. Defaults to everything this package can speak.
        client: An existing httpx.AsyncClient to reuse instead of opening one.

    Returns:
        A version string such as "1.3-rev2", or None if no Swagger document answered — the
        caller should then fall back to a version it chooses.
    """
    candidates = newest_first(VERSION_TO_PACKAGE if versions is None else versions)
    if not candidates:
        return None

    owns_client = client is None
    if owns_client:
        client = httpx.AsyncClient(verify=verify_ssl)

    try:
        results = await asyncio.gather(
            *(_serves(client, base_url, version, timeout) for version in candidates),
            return_exceptions=True,
        )
    finally:
        if owns_client:
            await client.aclose()

    served = {result for result in results if isinstance(result, str)}
    if not served:
        _LOGGER.debug("No Swagger document answered on %s", base_url)
        return None

    # candidates is newest-first, so the first match is the newest version served
    detected = next(version for version in candidates if version in served)
    _LOGGER.debug("%s serves %s; selected %s", base_url, sorted(served), detected)
    return detected


async def detect_rest_api(
    host: str,
    *,
    ports: Sequence[int] = DEFAULT_PORTS,
    versions: Sequence[str] | None = None,
    verify_ssl: bool = True,
    timeout: float = DEFAULT_TIMEOUT,
    client: "httpx.AsyncClient | None" = None,
) -> RestApiEndpoint | None:
    """Find where a server answers: which port, and which API version.

    Veeam Backup & Replication 13.1 serves the REST API on 443 and no longer needs a
    dedicated port. 9419 still answers on 13.1 for backward compatibility, and is the only
    port on older releases, but Veeam has said it will be removed in a future release. A
    caller therefore cannot assume either port, and the Swagger URL contains the port — so
    one probe sweep answers both questions at once.

    Args:
        host: Hostname or address, without scheme or port.
        ports: Candidate ports, in order of preference. 13.1 answers on both, so the first
            that responds wins rather than the highest-numbered.
        versions: Candidate versions. Defaults to everything this package can speak.
        verify_ssl: Whether to verify the server certificate. Ignored when ``client`` is
            given, since the caller's client carries its own settings.
        timeout: Per-request timeout in seconds. Probes are concurrent.
        client: An existing httpx.AsyncClient to reuse instead of opening one.

    Returns:
        A RestApiEndpoint(port, api_version), or None if nothing answered.
    """
    candidates = newest_first(VERSION_TO_PACKAGE if versions is None else versions)
    if not candidates or not ports:
        return None

    owns_client = client is None
    if owns_client:
        client = httpx.AsyncClient(verify=verify_ssl)

    attempts = [(port, version) for port in ports for version in candidates]

    try:
        results = await asyncio.gather(
            *(_serves(client, f"https://{host}:{port}", version, timeout) for port, version in attempts),
            return_exceptions=True,
        )
    finally:
        if owns_client:
            await client.aclose()

    answered = {(port, version) for (port, version), result in zip(attempts, results) if isinstance(result, str)}
    if not answered:
        _LOGGER.debug("Nothing answered on %s across ports %s", host, list(ports))
        return None

    # ports is preference-ordered and candidates is newest-first, so the first hit in that
    # nesting is the preferred port running its newest served version
    port, version = next(attempt for attempt in attempts if attempt in answered)
    _LOGGER.debug(
        "%s answered on %s; selected port %s with %s",
        host,
        sorted(answered),
        port,
        version,
    )
    return RestApiEndpoint(port=port, api_version=version)
