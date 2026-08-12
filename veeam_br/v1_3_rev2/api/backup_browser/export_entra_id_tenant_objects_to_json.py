from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entra_id_tenant_export_to_json_download_request import EntraIdTenantExportToJsonDownloadRequest
from ...models.error import Error
from ...types import File, Response


def _get_kwargs(
    session_id: UUID,
    *,
    body: EntraIdTenantExportToJsonDownloadRequest,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/backupBrowser/entraIdTenant/{session_id}/exportToJsonDownload".format(
            session_id=quote(str(session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EntraIdTenantExportToJsonDownloadRequest,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | File]:
    """Export Microsoft Entra ID Tenant Objects To JSON

     The HTTP POST request to the `/api/v1/backupBrowser/entraIdTenant/{sessionId}/exportToJsonDownload`
    endpoint exports Microsoft Entra ID tenant objects to JSON.<p>**Available to**&#58; Backup
    Administrator, Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (EntraIdTenantExportToJsonDownloadRequest): Export Microsoft Entra ID items to JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EntraIdTenantExportToJsonDownloadRequest,
    x_api_version: str = "1.3-rev2",
) -> Error | File | None:
    """Export Microsoft Entra ID Tenant Objects To JSON

     The HTTP POST request to the `/api/v1/backupBrowser/entraIdTenant/{sessionId}/exportToJsonDownload`
    endpoint exports Microsoft Entra ID tenant objects to JSON.<p>**Available to**&#58; Backup
    Administrator, Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (EntraIdTenantExportToJsonDownloadRequest): Export Microsoft Entra ID items to JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        body=body,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EntraIdTenantExportToJsonDownloadRequest,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | File]:
    """Export Microsoft Entra ID Tenant Objects To JSON

     The HTTP POST request to the `/api/v1/backupBrowser/entraIdTenant/{sessionId}/exportToJsonDownload`
    endpoint exports Microsoft Entra ID tenant objects to JSON.<p>**Available to**&#58; Backup
    Administrator, Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (EntraIdTenantExportToJsonDownloadRequest): Export Microsoft Entra ID items to JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EntraIdTenantExportToJsonDownloadRequest,
    x_api_version: str = "1.3-rev2",
) -> Error | File | None:
    """Export Microsoft Entra ID Tenant Objects To JSON

     The HTTP POST request to the `/api/v1/backupBrowser/entraIdTenant/{sessionId}/exportToJsonDownload`
    endpoint exports Microsoft Entra ID tenant objects to JSON.<p>**Available to**&#58; Backup
    Administrator, Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (EntraIdTenantExportToJsonDownloadRequest): Export Microsoft Entra ID items to JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            body=body,
            x_api_version=x_api_version,
        )
    ).parsed
