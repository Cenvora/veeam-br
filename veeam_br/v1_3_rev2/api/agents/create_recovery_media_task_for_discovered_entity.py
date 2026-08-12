from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.e_recovery_media_format import ERecoveryMediaFormat
from ...models.error import Error
from ...models.task_model import TaskModel
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    entity_id: UUID,
    *,
    format_: ERecoveryMediaFormat,
    allow_remote_bmr: bool,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    params: dict[str, Any] = {}

    json_format_ = format_.value
    params["format"] = json_format_

    params["allowRemoteBmr"] = allow_remote_bmr

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/agents/protectionGroups/{id}/discoveredEntities/{entity_id}/createRecoveryMedia".format(
            id=quote(str(id), safe=""),
            entity_id=quote(str(entity_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TaskModel | None:
    if response.status_code == 201:
        response_201 = TaskModel.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TaskModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    entity_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    format_: ERecoveryMediaFormat,
    allow_remote_bmr: bool,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | TaskModel]:
    """Create Recovery Media Task for Discovered Entity

     The HTTP POST request to the
    `/api/v1/agents/protectionGroups/{id}/discoveredEntities/{entityId}/createRecoveryMedia` endpoint
    starts an asynchronous task that creates Veeam Recovery Media for a protected Microsoft Windows
    computer. The endpoint returns a task that you can poll through the [Get
    Task](Tasks#operation/GetTask) request to track progress and surface failures. To download the
    resulting ISO file once the task completes successfully, run the [Download Recovery Media](Recovery-
    Media#operation/DownloadRecoveryMedia) request. <p>**Available to**&#58; Backup Administrator,
    Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        id (UUID):
        entity_id (UUID):
        format_ (ERecoveryMediaFormat): Recovery media format.
        allow_remote_bmr (bool):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaskModel]
    """

    kwargs = _get_kwargs(
        id=id,
        entity_id=entity_id,
        format_=format_,
        allow_remote_bmr=allow_remote_bmr,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    entity_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    format_: ERecoveryMediaFormat,
    allow_remote_bmr: bool,
    x_api_version: str = "1.3-rev2",
) -> Error | TaskModel | None:
    """Create Recovery Media Task for Discovered Entity

     The HTTP POST request to the
    `/api/v1/agents/protectionGroups/{id}/discoveredEntities/{entityId}/createRecoveryMedia` endpoint
    starts an asynchronous task that creates Veeam Recovery Media for a protected Microsoft Windows
    computer. The endpoint returns a task that you can poll through the [Get
    Task](Tasks#operation/GetTask) request to track progress and surface failures. To download the
    resulting ISO file once the task completes successfully, run the [Download Recovery Media](Recovery-
    Media#operation/DownloadRecoveryMedia) request. <p>**Available to**&#58; Backup Administrator,
    Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        id (UUID):
        entity_id (UUID):
        format_ (ERecoveryMediaFormat): Recovery media format.
        allow_remote_bmr (bool):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaskModel
    """

    return sync_detailed(
        id=id,
        entity_id=entity_id,
        client=client,
        format_=format_,
        allow_remote_bmr=allow_remote_bmr,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    entity_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    format_: ERecoveryMediaFormat,
    allow_remote_bmr: bool,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | TaskModel]:
    """Create Recovery Media Task for Discovered Entity

     The HTTP POST request to the
    `/api/v1/agents/protectionGroups/{id}/discoveredEntities/{entityId}/createRecoveryMedia` endpoint
    starts an asynchronous task that creates Veeam Recovery Media for a protected Microsoft Windows
    computer. The endpoint returns a task that you can poll through the [Get
    Task](Tasks#operation/GetTask) request to track progress and surface failures. To download the
    resulting ISO file once the task completes successfully, run the [Download Recovery Media](Recovery-
    Media#operation/DownloadRecoveryMedia) request. <p>**Available to**&#58; Backup Administrator,
    Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        id (UUID):
        entity_id (UUID):
        format_ (ERecoveryMediaFormat): Recovery media format.
        allow_remote_bmr (bool):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaskModel]
    """

    kwargs = _get_kwargs(
        id=id,
        entity_id=entity_id,
        format_=format_,
        allow_remote_bmr=allow_remote_bmr,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    entity_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    format_: ERecoveryMediaFormat,
    allow_remote_bmr: bool,
    x_api_version: str = "1.3-rev2",
) -> Error | TaskModel | None:
    """Create Recovery Media Task for Discovered Entity

     The HTTP POST request to the
    `/api/v1/agents/protectionGroups/{id}/discoveredEntities/{entityId}/createRecoveryMedia` endpoint
    starts an asynchronous task that creates Veeam Recovery Media for a protected Microsoft Windows
    computer. The endpoint returns a task that you can poll through the [Get
    Task](Tasks#operation/GetTask) request to track progress and surface failures. To download the
    resulting ISO file once the task completes successfully, run the [Download Recovery Media](Recovery-
    Media#operation/DownloadRecoveryMedia) request. <p>**Available to**&#58; Backup Administrator,
    Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        id (UUID):
        entity_id (UUID):
        format_ (ERecoveryMediaFormat): Recovery media format.
        allow_remote_bmr (bool):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaskModel
    """

    return (
        await asyncio_detailed(
            id=id,
            entity_id=entity_id,
            client=client,
            format_=format_,
            allow_remote_bmr=allow_remote_bmr,
            x_api_version=x_api_version,
        )
    ).parsed
