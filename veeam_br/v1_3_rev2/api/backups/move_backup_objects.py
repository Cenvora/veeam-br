from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.move_backup_objects_spec import MoveBackupObjectsSpec
from ...models.session_model import SessionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: MoveBackupObjectsSpec,
    move_associated_backup_copies: bool | Unset = False,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    params: dict[str, Any] = {}

    params["moveAssociatedBackupCopies"] = move_associated_backup_copies

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/backups/{id}/objects/moveTo".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SessionModel | None:
    if response.status_code == 201:
        response_201 = SessionModel.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SessionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MoveBackupObjectsSpec,
    move_associated_backup_copies: bool | Unset = False,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | SessionModel]:
    """Move Backup Objects to Another Job

     The HTTP POST request to the `/api/v1/backups/{id}/objects/moveTo` endpoint moves backup objects
    (virtual or physical machines) from a backup with the specified `id` to a specified target
    job.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        id (UUID):
        move_associated_backup_copies (bool | Unset):  Default: False.
        x_api_version (str):  Default: '1.3-rev2'.
        body (MoveBackupObjectsSpec): Spec for moving backup objects to another job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SessionModel]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        move_associated_backup_copies=move_associated_backup_copies,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MoveBackupObjectsSpec,
    move_associated_backup_copies: bool | Unset = False,
    x_api_version: str = "1.3-rev2",
) -> Error | SessionModel | None:
    """Move Backup Objects to Another Job

     The HTTP POST request to the `/api/v1/backups/{id}/objects/moveTo` endpoint moves backup objects
    (virtual or physical machines) from a backup with the specified `id` to a specified target
    job.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        id (UUID):
        move_associated_backup_copies (bool | Unset):  Default: False.
        x_api_version (str):  Default: '1.3-rev2'.
        body (MoveBackupObjectsSpec): Spec for moving backup objects to another job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SessionModel
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        move_associated_backup_copies=move_associated_backup_copies,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MoveBackupObjectsSpec,
    move_associated_backup_copies: bool | Unset = False,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | SessionModel]:
    """Move Backup Objects to Another Job

     The HTTP POST request to the `/api/v1/backups/{id}/objects/moveTo` endpoint moves backup objects
    (virtual or physical machines) from a backup with the specified `id` to a specified target
    job.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        id (UUID):
        move_associated_backup_copies (bool | Unset):  Default: False.
        x_api_version (str):  Default: '1.3-rev2'.
        body (MoveBackupObjectsSpec): Spec for moving backup objects to another job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SessionModel]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        move_associated_backup_copies=move_associated_backup_copies,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MoveBackupObjectsSpec,
    move_associated_backup_copies: bool | Unset = False,
    x_api_version: str = "1.3-rev2",
) -> Error | SessionModel | None:
    """Move Backup Objects to Another Job

     The HTTP POST request to the `/api/v1/backups/{id}/objects/moveTo` endpoint moves backup objects
    (virtual or physical machines) from a backup with the specified `id` to a specified target
    job.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        id (UUID):
        move_associated_backup_copies (bool | Unset):  Default: False.
        x_api_version (str):  Default: '1.3-rev2'.
        body (MoveBackupObjectsSpec): Spec for moving backup objects to another job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SessionModel
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            move_associated_backup_copies=move_associated_backup_copies,
            x_api_version=x_api_version,
        )
    ).parsed
