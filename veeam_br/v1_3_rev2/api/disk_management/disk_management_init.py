from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disk_management_initialization_request import DiskManagementInitializationRequest
from ...models.disk_management_initialization_response import DiskManagementInitializationResponse
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: DiskManagementInitializationRequest,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/diskManagement/init",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DiskManagementInitializationResponse | Error | None:
    if response.status_code == 200:
        response_200 = DiskManagementInitializationResponse.from_dict(response.json())

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
) -> Response[DiskManagementInitializationResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DiskManagementInitializationRequest,
    x_api_version: str = "1.3-rev2",
) -> Response[DiskManagementInitializationResponse | Error]:
    """Initialize Disk Management

     The HTTP POST request to the `/api/v1/diskManagement/init` endpoint initializes a disk management
    session and loads the live disk layout of the host.<p>**Available to**&#58; Backup Administrator,
    Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (DiskManagementInitializationRequest): Settings for initializing disk management for
            a host.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiskManagementInitializationResponse | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DiskManagementInitializationRequest,
    x_api_version: str = "1.3-rev2",
) -> DiskManagementInitializationResponse | Error | None:
    """Initialize Disk Management

     The HTTP POST request to the `/api/v1/diskManagement/init` endpoint initializes a disk management
    session and loads the live disk layout of the host.<p>**Available to**&#58; Backup Administrator,
    Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (DiskManagementInitializationRequest): Settings for initializing disk management for
            a host.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiskManagementInitializationResponse | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DiskManagementInitializationRequest,
    x_api_version: str = "1.3-rev2",
) -> Response[DiskManagementInitializationResponse | Error]:
    """Initialize Disk Management

     The HTTP POST request to the `/api/v1/diskManagement/init` endpoint initializes a disk management
    session and loads the live disk layout of the host.<p>**Available to**&#58; Backup Administrator,
    Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (DiskManagementInitializationRequest): Settings for initializing disk management for
            a host.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiskManagementInitializationResponse | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DiskManagementInitializationRequest,
    x_api_version: str = "1.3-rev2",
) -> DiskManagementInitializationResponse | Error | None:
    """Initialize Disk Management

     The HTTP POST request to the `/api/v1/diskManagement/init` endpoint initializes a disk management
    session and loads the live disk layout of the host.<p>**Available to**&#58; Backup Administrator,
    Restore Operator. Also available to custom roles that have restore permissions.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (DiskManagementInitializationRequest): Settings for initializing disk management for
            a host.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiskManagementInitializationResponse | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_api_version=x_api_version,
        )
    ).parsed
