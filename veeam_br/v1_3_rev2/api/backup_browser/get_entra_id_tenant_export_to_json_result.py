from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_entra_id_tenant_export_to_json_result_response import GetEntraIdTenantExportToJsonResultResponse
from ...types import Response


def _get_kwargs(
    session_id: UUID,
    export_session_id: UUID,
    *,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/backupBrowser/entraIdTenant/{session_id}/exportToJson/{export_session_id}/result".format(
            session_id=quote(str(session_id), safe=""),
            export_session_id=quote(str(export_session_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetEntraIdTenantExportToJsonResultResponse | None:
    if response.status_code == 200:
        response_200 = GetEntraIdTenantExportToJsonResultResponse.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GetEntraIdTenantExportToJsonResultResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: UUID,
    export_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | GetEntraIdTenantExportToJsonResultResponse]:
    """Get JSON Export Results for Microsoft Entra ID Items

     The HTTP GET request to the
    `/api/v1/backupBrowser/entraIdTenant/{sessionId}/exportToJson/{exportSessionId}/result` endpoint
    gets the JSON export results from an export session that has the specified `exportSessionId` within
    a mount session that has the specified `sessionId`. The response contains a SAS URI that you can use
    to download the exported JSON files.<p>**Available to**&#58; Backup Administrator, Restore Operator.
    Also available to custom roles that have restore permissions.</p>

    Args:
        session_id (UUID):
        export_session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetEntraIdTenantExportToJsonResultResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        export_session_id=export_session_id,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: UUID,
    export_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Error | GetEntraIdTenantExportToJsonResultResponse | None:
    """Get JSON Export Results for Microsoft Entra ID Items

     The HTTP GET request to the
    `/api/v1/backupBrowser/entraIdTenant/{sessionId}/exportToJson/{exportSessionId}/result` endpoint
    gets the JSON export results from an export session that has the specified `exportSessionId` within
    a mount session that has the specified `sessionId`. The response contains a SAS URI that you can use
    to download the exported JSON files.<p>**Available to**&#58; Backup Administrator, Restore Operator.
    Also available to custom roles that have restore permissions.</p>

    Args:
        session_id (UUID):
        export_session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetEntraIdTenantExportToJsonResultResponse
    """

    return sync_detailed(
        session_id=session_id,
        export_session_id=export_session_id,
        client=client,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    session_id: UUID,
    export_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | GetEntraIdTenantExportToJsonResultResponse]:
    """Get JSON Export Results for Microsoft Entra ID Items

     The HTTP GET request to the
    `/api/v1/backupBrowser/entraIdTenant/{sessionId}/exportToJson/{exportSessionId}/result` endpoint
    gets the JSON export results from an export session that has the specified `exportSessionId` within
    a mount session that has the specified `sessionId`. The response contains a SAS URI that you can use
    to download the exported JSON files.<p>**Available to**&#58; Backup Administrator, Restore Operator.
    Also available to custom roles that have restore permissions.</p>

    Args:
        session_id (UUID):
        export_session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetEntraIdTenantExportToJsonResultResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        export_session_id=export_session_id,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: UUID,
    export_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Error | GetEntraIdTenantExportToJsonResultResponse | None:
    """Get JSON Export Results for Microsoft Entra ID Items

     The HTTP GET request to the
    `/api/v1/backupBrowser/entraIdTenant/{sessionId}/exportToJson/{exportSessionId}/result` endpoint
    gets the JSON export results from an export session that has the specified `exportSessionId` within
    a mount session that has the specified `sessionId`. The response contains a SAS URI that you can use
    to download the exported JSON files.<p>**Available to**&#58; Backup Administrator, Restore Operator.
    Also available to custom roles that have restore permissions.</p>

    Args:
        session_id (UUID):
        export_session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetEntraIdTenantExportToJsonResultResponse
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            export_session_id=export_session_id,
            client=client,
            x_api_version=x_api_version,
        )
    ).parsed
