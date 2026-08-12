from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.unstructured_data_archive_retrieval_models_result import UnstructuredDataArchiveRetrievalModelsResult
from ...types import UNSET, Response


def _get_kwargs(
    *,
    server_id_filter: list[UUID],
    backup_id_filter: list[UUID],
    restore_point_id_filter: list[UUID],
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    params: dict[str, Any] = {}

    json_server_id_filter = []
    for server_id_filter_item_data in server_id_filter:
        server_id_filter_item = str(server_id_filter_item_data)
        json_server_id_filter.append(server_id_filter_item)

    params["serverIdFilter"] = json_server_id_filter

    json_backup_id_filter = []
    for backup_id_filter_item_data in backup_id_filter:
        backup_id_filter_item = str(backup_id_filter_item_data)
        json_backup_id_filter.append(backup_id_filter_item)

    params["backupIdFilter"] = json_backup_id_filter

    json_restore_point_id_filter = []
    for restore_point_id_filter_item_data in restore_point_id_filter:
        restore_point_id_filter_item = str(restore_point_id_filter_item_data)
        json_restore_point_id_filter.append(restore_point_id_filter_item)

    params["restorePointIdFilter"] = json_restore_point_id_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/restore/unstructuredData/retrieveFromArchiveStorage",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | UnstructuredDataArchiveRetrievalModelsResult | None:
    if response.status_code == 201:
        response_201 = UnstructuredDataArchiveRetrievalModelsResult.from_dict(response.json())

        return response_201

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
) -> Response[Error | UnstructuredDataArchiveRetrievalModelsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    server_id_filter: list[UUID],
    backup_id_filter: list[UUID],
    restore_point_id_filter: list[UUID],
    x_api_version: str = "1.3-rev2",
) -> Response[Error | UnstructuredDataArchiveRetrievalModelsResult]:
    """Get Cold Object Storage Retrieval Operations

     The HTTP GET request to the `/api/v1/restore/unstructuredData/retrieveFromArchiveStorage` endpoint
    returns the current retrieval operations from cold object storage with their expiration periods.
    <p>**Available to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that
    have restore permissions.</p>

    Args:
        server_id_filter (list[UUID]):
        backup_id_filter (list[UUID]):
        restore_point_id_filter (list[UUID]):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UnstructuredDataArchiveRetrievalModelsResult]
    """

    kwargs = _get_kwargs(
        server_id_filter=server_id_filter,
        backup_id_filter=backup_id_filter,
        restore_point_id_filter=restore_point_id_filter,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    server_id_filter: list[UUID],
    backup_id_filter: list[UUID],
    restore_point_id_filter: list[UUID],
    x_api_version: str = "1.3-rev2",
) -> Error | UnstructuredDataArchiveRetrievalModelsResult | None:
    """Get Cold Object Storage Retrieval Operations

     The HTTP GET request to the `/api/v1/restore/unstructuredData/retrieveFromArchiveStorage` endpoint
    returns the current retrieval operations from cold object storage with their expiration periods.
    <p>**Available to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that
    have restore permissions.</p>

    Args:
        server_id_filter (list[UUID]):
        backup_id_filter (list[UUID]):
        restore_point_id_filter (list[UUID]):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UnstructuredDataArchiveRetrievalModelsResult
    """

    return sync_detailed(
        client=client,
        server_id_filter=server_id_filter,
        backup_id_filter=backup_id_filter,
        restore_point_id_filter=restore_point_id_filter,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    server_id_filter: list[UUID],
    backup_id_filter: list[UUID],
    restore_point_id_filter: list[UUID],
    x_api_version: str = "1.3-rev2",
) -> Response[Error | UnstructuredDataArchiveRetrievalModelsResult]:
    """Get Cold Object Storage Retrieval Operations

     The HTTP GET request to the `/api/v1/restore/unstructuredData/retrieveFromArchiveStorage` endpoint
    returns the current retrieval operations from cold object storage with their expiration periods.
    <p>**Available to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that
    have restore permissions.</p>

    Args:
        server_id_filter (list[UUID]):
        backup_id_filter (list[UUID]):
        restore_point_id_filter (list[UUID]):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UnstructuredDataArchiveRetrievalModelsResult]
    """

    kwargs = _get_kwargs(
        server_id_filter=server_id_filter,
        backup_id_filter=backup_id_filter,
        restore_point_id_filter=restore_point_id_filter,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    server_id_filter: list[UUID],
    backup_id_filter: list[UUID],
    restore_point_id_filter: list[UUID],
    x_api_version: str = "1.3-rev2",
) -> Error | UnstructuredDataArchiveRetrievalModelsResult | None:
    """Get Cold Object Storage Retrieval Operations

     The HTTP GET request to the `/api/v1/restore/unstructuredData/retrieveFromArchiveStorage` endpoint
    returns the current retrieval operations from cold object storage with their expiration periods.
    <p>**Available to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that
    have restore permissions.</p>

    Args:
        server_id_filter (list[UUID]):
        backup_id_filter (list[UUID]):
        restore_point_id_filter (list[UUID]):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UnstructuredDataArchiveRetrievalModelsResult
    """

    return (
        await asyncio_detailed(
            client=client,
            server_id_filter=server_id_filter,
            backup_id_filter=backup_id_filter,
            restore_point_id_filter=restore_point_id_filter,
            x_api_version=x_api_version,
        )
    ).parsed
