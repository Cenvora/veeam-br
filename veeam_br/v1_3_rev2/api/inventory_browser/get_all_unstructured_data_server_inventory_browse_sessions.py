from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.e_unstructured_data_inventory_browse_sessions_filters_order_column import (
    EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn,
)
from ...models.error import Error
from ...models.unstructured_data_inventory_browse_sessions_result import UnstructuredDataInventoryBrowseSessionsResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip: int | Unset = UNSET,
    limit: int | Unset = 200,
    order_column: EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
    session_id_filter: str | Unset = UNSET,
    server_id_filter: str | Unset = UNSET,
    server_name_filter: str | Unset = UNSET,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    params: dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    json_order_column: str | Unset = UNSET
    if not isinstance(order_column, Unset):
        json_order_column = order_column.value

    params["orderColumn"] = json_order_column

    params["orderAsc"] = order_asc

    params["sessionIdFilter"] = session_id_filter

    params["serverIdFilter"] = server_id_filter

    params["serverNameFilter"] = server_name_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/inventory/unstructuredDataServers/sessions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | UnstructuredDataInventoryBrowseSessionsResult | None:
    if response.status_code == 200:
        response_200 = UnstructuredDataInventoryBrowseSessionsResult.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | UnstructuredDataInventoryBrowseSessionsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = UNSET,
    limit: int | Unset = 200,
    order_column: EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
    session_id_filter: str | Unset = UNSET,
    server_id_filter: str | Unset = UNSET,
    server_name_filter: str | Unset = UNSET,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | UnstructuredDataInventoryBrowseSessionsResult]:
    """Get All Unstructured Data Server Inventory Browse Sessions

     The HTTP GET request to the `/api/v1/inventory/unstructuredDataServers/sessions` endpoint gets an
    array of unstructured data server inventory browse sessions available on the backup
    server.<p>**Available to**&#58; Backup Administrator, Backup Operator, Restore Operator, Backup
    Viewer. Also available to custom roles that have backup or restore permissions.</p>

    Args:
        skip (int | Unset):
        limit (int | Unset):  Default: 200.
        order_column (EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset):
        order_asc (bool | Unset):
        session_id_filter (str | Unset):
        server_id_filter (str | Unset):
        server_name_filter (str | Unset):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UnstructuredDataInventoryBrowseSessionsResult]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        order_column=order_column,
        order_asc=order_asc,
        session_id_filter=session_id_filter,
        server_id_filter=server_id_filter,
        server_name_filter=server_name_filter,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = UNSET,
    limit: int | Unset = 200,
    order_column: EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
    session_id_filter: str | Unset = UNSET,
    server_id_filter: str | Unset = UNSET,
    server_name_filter: str | Unset = UNSET,
    x_api_version: str = "1.3-rev2",
) -> Error | UnstructuredDataInventoryBrowseSessionsResult | None:
    """Get All Unstructured Data Server Inventory Browse Sessions

     The HTTP GET request to the `/api/v1/inventory/unstructuredDataServers/sessions` endpoint gets an
    array of unstructured data server inventory browse sessions available on the backup
    server.<p>**Available to**&#58; Backup Administrator, Backup Operator, Restore Operator, Backup
    Viewer. Also available to custom roles that have backup or restore permissions.</p>

    Args:
        skip (int | Unset):
        limit (int | Unset):  Default: 200.
        order_column (EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset):
        order_asc (bool | Unset):
        session_id_filter (str | Unset):
        server_id_filter (str | Unset):
        server_name_filter (str | Unset):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UnstructuredDataInventoryBrowseSessionsResult
    """

    return sync_detailed(
        client=client,
        skip=skip,
        limit=limit,
        order_column=order_column,
        order_asc=order_asc,
        session_id_filter=session_id_filter,
        server_id_filter=server_id_filter,
        server_name_filter=server_name_filter,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = UNSET,
    limit: int | Unset = 200,
    order_column: EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
    session_id_filter: str | Unset = UNSET,
    server_id_filter: str | Unset = UNSET,
    server_name_filter: str | Unset = UNSET,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | UnstructuredDataInventoryBrowseSessionsResult]:
    """Get All Unstructured Data Server Inventory Browse Sessions

     The HTTP GET request to the `/api/v1/inventory/unstructuredDataServers/sessions` endpoint gets an
    array of unstructured data server inventory browse sessions available on the backup
    server.<p>**Available to**&#58; Backup Administrator, Backup Operator, Restore Operator, Backup
    Viewer. Also available to custom roles that have backup or restore permissions.</p>

    Args:
        skip (int | Unset):
        limit (int | Unset):  Default: 200.
        order_column (EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset):
        order_asc (bool | Unset):
        session_id_filter (str | Unset):
        server_id_filter (str | Unset):
        server_name_filter (str | Unset):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UnstructuredDataInventoryBrowseSessionsResult]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        order_column=order_column,
        order_asc=order_asc,
        session_id_filter=session_id_filter,
        server_id_filter=server_id_filter,
        server_name_filter=server_name_filter,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = UNSET,
    limit: int | Unset = 200,
    order_column: EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
    session_id_filter: str | Unset = UNSET,
    server_id_filter: str | Unset = UNSET,
    server_name_filter: str | Unset = UNSET,
    x_api_version: str = "1.3-rev2",
) -> Error | UnstructuredDataInventoryBrowseSessionsResult | None:
    """Get All Unstructured Data Server Inventory Browse Sessions

     The HTTP GET request to the `/api/v1/inventory/unstructuredDataServers/sessions` endpoint gets an
    array of unstructured data server inventory browse sessions available on the backup
    server.<p>**Available to**&#58; Backup Administrator, Backup Operator, Restore Operator, Backup
    Viewer. Also available to custom roles that have backup or restore permissions.</p>

    Args:
        skip (int | Unset):
        limit (int | Unset):  Default: 200.
        order_column (EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset):
        order_asc (bool | Unset):
        session_id_filter (str | Unset):
        server_id_filter (str | Unset):
        server_name_filter (str | Unset):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UnstructuredDataInventoryBrowseSessionsResult
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            limit=limit,
            order_column=order_column,
            order_asc=order_asc,
            session_id_filter=session_id_filter,
            server_id_filter=server_id_filter,
            server_name_filter=server_name_filter,
            x_api_version=x_api_version,
        )
    ).parsed
