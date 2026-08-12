from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.session_model import SessionModel
from ...types import Response


def _get_kwargs(
    *,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/backups/moveCopySessions",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | list[SessionModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SessionModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Error | list[SessionModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | list[SessionModel]]:
    """Get Move/Copy Backup Sessions Awaiting Action

     The HTTP GET request to the `/api/v1/backups/moveCopySessions` endpoint gets an array of all
    Move/Copy backup sessions that are in the `ActionRequired` state and need user input to proceed
    (Retry, Detach failed, or Stop and undo).<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[SessionModel]]
    """

    kwargs = _get_kwargs(
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Error | list[SessionModel] | None:
    """Get Move/Copy Backup Sessions Awaiting Action

     The HTTP GET request to the `/api/v1/backups/moveCopySessions` endpoint gets an array of all
    Move/Copy backup sessions that are in the `ActionRequired` state and need user input to proceed
    (Retry, Detach failed, or Stop and undo).<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[SessionModel]
    """

    return sync_detailed(
        client=client,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | list[SessionModel]]:
    """Get Move/Copy Backup Sessions Awaiting Action

     The HTTP GET request to the `/api/v1/backups/moveCopySessions` endpoint gets an array of all
    Move/Copy backup sessions that are in the `ActionRequired` state and need user input to proceed
    (Retry, Detach failed, or Stop and undo).<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[SessionModel]]
    """

    kwargs = _get_kwargs(
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Error | list[SessionModel] | None:
    """Get Move/Copy Backup Sessions Awaiting Action

     The HTTP GET request to the `/api/v1/backups/moveCopySessions` endpoint gets an array of all
    Move/Copy backup sessions that are in the `ActionRequired` state and need user input to proceed
    (Retry, Detach failed, or Stop and undo).<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[SessionModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_api_version=x_api_version,
        )
    ).parsed
