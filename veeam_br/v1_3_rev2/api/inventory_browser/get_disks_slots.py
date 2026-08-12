from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disk_slots_result import DiskSlotsResult
from ...models.e_platform_type import EPlatformType
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    platform: EPlatformType,
    *,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/inventory/platforms/{platform}/diskSlots".format(
            platform=quote(str(platform), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DiskSlotsResult | Error | None:
    if response.status_code == 200:
        response_200 = DiskSlotsResult.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DiskSlotsResult | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    platform: EPlatformType,
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Response[DiskSlotsResult | Error]:
    """Get Available Disk Slots for Platform

     The HTTP GET request to the `/api/v1/inventory/platforms/{platform}/diskSlots` endpoint gets an
    array of available disk slots for selected platform. <p>**Available to**&#58; Backup Administrator,
    Backup Operator, Restore Operator. Also available to custom roles that have backup or restore
    permissions.</p>

    Args:
        platform (EPlatformType): Platform type.<p>`Test` is the platform of SureBackup content
            scan job (`SureBackupContentScan`) — backup verification and content scanning with
            antivirus software or YARA rules.</p>
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiskSlotsResult | Error]
    """

    kwargs = _get_kwargs(
        platform=platform,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    platform: EPlatformType,
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> DiskSlotsResult | Error | None:
    """Get Available Disk Slots for Platform

     The HTTP GET request to the `/api/v1/inventory/platforms/{platform}/diskSlots` endpoint gets an
    array of available disk slots for selected platform. <p>**Available to**&#58; Backup Administrator,
    Backup Operator, Restore Operator. Also available to custom roles that have backup or restore
    permissions.</p>

    Args:
        platform (EPlatformType): Platform type.<p>`Test` is the platform of SureBackup content
            scan job (`SureBackupContentScan`) — backup verification and content scanning with
            antivirus software or YARA rules.</p>
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiskSlotsResult | Error
    """

    return sync_detailed(
        platform=platform,
        client=client,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    platform: EPlatformType,
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Response[DiskSlotsResult | Error]:
    """Get Available Disk Slots for Platform

     The HTTP GET request to the `/api/v1/inventory/platforms/{platform}/diskSlots` endpoint gets an
    array of available disk slots for selected platform. <p>**Available to**&#58; Backup Administrator,
    Backup Operator, Restore Operator. Also available to custom roles that have backup or restore
    permissions.</p>

    Args:
        platform (EPlatformType): Platform type.<p>`Test` is the platform of SureBackup content
            scan job (`SureBackupContentScan`) — backup verification and content scanning with
            antivirus software or YARA rules.</p>
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiskSlotsResult | Error]
    """

    kwargs = _get_kwargs(
        platform=platform,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    platform: EPlatformType,
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> DiskSlotsResult | Error | None:
    """Get Available Disk Slots for Platform

     The HTTP GET request to the `/api/v1/inventory/platforms/{platform}/diskSlots` endpoint gets an
    array of available disk slots for selected platform. <p>**Available to**&#58; Backup Administrator,
    Backup Operator, Restore Operator. Also available to custom roles that have backup or restore
    permissions.</p>

    Args:
        platform (EPlatformType): Platform type.<p>`Test` is the platform of SureBackup content
            scan job (`SureBackupContentScan`) — backup verification and content scanning with
            antivirus software or YARA rules.</p>
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiskSlotsResult | Error
    """

    return (
        await asyncio_detailed(
            platform=platform,
            client=client,
            x_api_version=x_api_version,
        )
    ).parsed
