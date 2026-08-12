from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.flr_validate_restore_item_target_path_result import FlrValidateRestoreItemTargetPathResult
from ...models.flr_validate_restore_item_target_path_spec import FlrValidateRestoreItemTargetPathSpec
from ...types import Response


def _get_kwargs(
    session_id: UUID,
    *,
    body: FlrValidateRestoreItemTargetPathSpec,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/restore/flr/{session_id}/validateRestoreItemTargetPath".format(
            session_id=quote(str(session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | FlrValidateRestoreItemTargetPathResult | None:
    if response.status_code == 200:
        response_200 = FlrValidateRestoreItemTargetPathResult.from_dict(response.json())

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
) -> Response[Error | FlrValidateRestoreItemTargetPathResult]:
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
    body: FlrValidateRestoreItemTargetPathSpec,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | FlrValidateRestoreItemTargetPathResult]:
    """Validate FLR Restore Item Target Path

     The HTTP POST request to the `/api/v1/restore/flr/{sessionId}/validateRestoreItemTargetPath`
    endpoint checks whether a target path needs to be provided for the specified file-level restore
    item. Call this endpoint after the target machine credentials have been validated.<p>**Available
    to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that have restore
    permissions.</p>

    Args:
        session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (FlrValidateRestoreItemTargetPathSpec): Settings to check whether a target path needs
            to be provided for a file-level restore item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FlrValidateRestoreItemTargetPathResult]
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
    body: FlrValidateRestoreItemTargetPathSpec,
    x_api_version: str = "1.3-rev2",
) -> Error | FlrValidateRestoreItemTargetPathResult | None:
    """Validate FLR Restore Item Target Path

     The HTTP POST request to the `/api/v1/restore/flr/{sessionId}/validateRestoreItemTargetPath`
    endpoint checks whether a target path needs to be provided for the specified file-level restore
    item. Call this endpoint after the target machine credentials have been validated.<p>**Available
    to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that have restore
    permissions.</p>

    Args:
        session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (FlrValidateRestoreItemTargetPathSpec): Settings to check whether a target path needs
            to be provided for a file-level restore item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FlrValidateRestoreItemTargetPathResult
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
    body: FlrValidateRestoreItemTargetPathSpec,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | FlrValidateRestoreItemTargetPathResult]:
    """Validate FLR Restore Item Target Path

     The HTTP POST request to the `/api/v1/restore/flr/{sessionId}/validateRestoreItemTargetPath`
    endpoint checks whether a target path needs to be provided for the specified file-level restore
    item. Call this endpoint after the target machine credentials have been validated.<p>**Available
    to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that have restore
    permissions.</p>

    Args:
        session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (FlrValidateRestoreItemTargetPathSpec): Settings to check whether a target path needs
            to be provided for a file-level restore item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FlrValidateRestoreItemTargetPathResult]
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
    body: FlrValidateRestoreItemTargetPathSpec,
    x_api_version: str = "1.3-rev2",
) -> Error | FlrValidateRestoreItemTargetPathResult | None:
    """Validate FLR Restore Item Target Path

     The HTTP POST request to the `/api/v1/restore/flr/{sessionId}/validateRestoreItemTargetPath`
    endpoint checks whether a target path needs to be provided for the specified file-level restore
    item. Call this endpoint after the target machine credentials have been validated.<p>**Available
    to**&#58; Backup Administrator, Restore Operator. Also available to custom roles that have restore
    permissions.</p>

    Args:
        session_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (FlrValidateRestoreItemTargetPathSpec): Settings to check whether a target path needs
            to be provided for a file-level restore item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FlrValidateRestoreItemTargetPathResult
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            body=body,
            x_api_version=x_api_version,
        )
    ).parsed
