from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_role_model import CustomRoleModel
from ...models.custom_role_spec import CustomRoleSpec
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: CustomRoleSpec,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/security/roles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomRoleModel | Error | None:
    if response.status_code == 201:
        response_201 = CustomRoleModel.from_dict(response.json())

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
) -> Response[CustomRoleModel | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CustomRoleSpec,
    x_api_version: str = "1.3-rev2",
) -> Response[CustomRoleModel | Error]:
    """Create Custom Role

     The HTTP POST request to the `/api/v1/security/roles` endpoint creates a custom role with tailored
    permissions and granular access scopes.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (CustomRoleSpec): Custom role settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomRoleModel | Error]
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
    body: CustomRoleSpec,
    x_api_version: str = "1.3-rev2",
) -> CustomRoleModel | Error | None:
    """Create Custom Role

     The HTTP POST request to the `/api/v1/security/roles` endpoint creates a custom role with tailored
    permissions and granular access scopes.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (CustomRoleSpec): Custom role settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomRoleModel | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CustomRoleSpec,
    x_api_version: str = "1.3-rev2",
) -> Response[CustomRoleModel | Error]:
    """Create Custom Role

     The HTTP POST request to the `/api/v1/security/roles` endpoint creates a custom role with tailored
    permissions and granular access scopes.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (CustomRoleSpec): Custom role settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomRoleModel | Error]
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
    body: CustomRoleSpec,
    x_api_version: str = "1.3-rev2",
) -> CustomRoleModel | Error | None:
    """Create Custom Role

     The HTTP POST request to the `/api/v1/security/roles` endpoint creates a custom role with tailored
    permissions and granular access scopes.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (CustomRoleSpec): Custom role settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomRoleModel | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_api_version=x_api_version,
        )
    ).parsed
