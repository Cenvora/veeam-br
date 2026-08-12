from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disk_layout_operation_spec import DiskLayoutOperationSpec
from ...models.disk_mapping_context import DiskMappingContext
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    disk_management_session_id: UUID,
    *,
    body: DiskLayoutOperationSpec,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/diskManagement/{disk_management_session_id}/applyDiskLayout".format(
            disk_management_session_id=quote(str(disk_management_session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DiskMappingContext | Error | None:
    if response.status_code == 200:
        response_200 = DiskMappingContext.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

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
) -> Response[DiskMappingContext | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    disk_management_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DiskLayoutOperationSpec,
    x_api_version: str = "1.3-rev2",
) -> Response[DiskMappingContext | Error]:
    """Apply Disk Layout

     The HTTP POST request to the `/api/v1/diskManagement/{diskManagementSessionId}/applyDiskLayout`
    endpoint applies a disk layout from an original disk to the specified target disk.<p>**Available
    to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that have restore
    permissions.</p>

    Args:
        disk_management_session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (DiskLayoutOperationSpec): Settings for applying a backup disk layout to a target
            disk.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiskMappingContext | Error]
    """

    kwargs = _get_kwargs(
        disk_management_session_id=disk_management_session_id,
        body=body,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    disk_management_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DiskLayoutOperationSpec,
    x_api_version: str = "1.3-rev2",
) -> DiskMappingContext | Error | None:
    """Apply Disk Layout

     The HTTP POST request to the `/api/v1/diskManagement/{diskManagementSessionId}/applyDiskLayout`
    endpoint applies a disk layout from an original disk to the specified target disk.<p>**Available
    to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that have restore
    permissions.</p>

    Args:
        disk_management_session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (DiskLayoutOperationSpec): Settings for applying a backup disk layout to a target
            disk.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiskMappingContext | Error
    """

    return sync_detailed(
        disk_management_session_id=disk_management_session_id,
        client=client,
        body=body,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    disk_management_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DiskLayoutOperationSpec,
    x_api_version: str = "1.3-rev2",
) -> Response[DiskMappingContext | Error]:
    """Apply Disk Layout

     The HTTP POST request to the `/api/v1/diskManagement/{diskManagementSessionId}/applyDiskLayout`
    endpoint applies a disk layout from an original disk to the specified target disk.<p>**Available
    to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that have restore
    permissions.</p>

    Args:
        disk_management_session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (DiskLayoutOperationSpec): Settings for applying a backup disk layout to a target
            disk.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiskMappingContext | Error]
    """

    kwargs = _get_kwargs(
        disk_management_session_id=disk_management_session_id,
        body=body,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    disk_management_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DiskLayoutOperationSpec,
    x_api_version: str = "1.3-rev2",
) -> DiskMappingContext | Error | None:
    """Apply Disk Layout

     The HTTP POST request to the `/api/v1/diskManagement/{diskManagementSessionId}/applyDiskLayout`
    endpoint applies a disk layout from an original disk to the specified target disk.<p>**Available
    to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that have restore
    permissions.</p>

    Args:
        disk_management_session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (DiskLayoutOperationSpec): Settings for applying a backup disk layout to a target
            disk.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiskMappingContext | Error
    """

    return (
        await asyncio_detailed(
            disk_management_session_id=disk_management_session_id,
            client=client,
            body=body,
            x_api_version=x_api_version,
        )
    ).parsed
