from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acl_browser_filters import AclBrowserFilters
from ...models.acl_browser_result import AclBrowserResult
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AclBrowserFilters | Unset = UNSET,
    force_reload: bool | Unset = UNSET,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    params: dict[str, Any] = {}

    params["forceReload"] = force_reload

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/acl",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AclBrowserResult | Error | None:
    if response.status_code == 200:
        response_200 = AclBrowserResult.from_dict(response.json())

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
) -> Response[AclBrowserResult | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AclBrowserFilters | Unset = UNSET,
    force_reload: bool | Unset = UNSET,
    x_api_version: str = "1.3-rev2",
) -> Response[AclBrowserResult | Error]:
    """Get Access Control List

     The HTTP POST request to the `/api/v1/acl` endpoint gets an array of ACL rules. <p>**Available
    to**&#58; Backup Administrator, Backup Operator, Restore Operator, Backup Viewer, Security
    Administrator. Also available to custom roles that have backup or restore permissions.</p>

    Args:
        force_reload (bool | Unset):
        x_api_version (str):  Default: '1.3-rev2'.
        body (AclBrowserFilters | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AclBrowserResult | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        force_reload=force_reload,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AclBrowserFilters | Unset = UNSET,
    force_reload: bool | Unset = UNSET,
    x_api_version: str = "1.3-rev2",
) -> AclBrowserResult | Error | None:
    """Get Access Control List

     The HTTP POST request to the `/api/v1/acl` endpoint gets an array of ACL rules. <p>**Available
    to**&#58; Backup Administrator, Backup Operator, Restore Operator, Backup Viewer, Security
    Administrator. Also available to custom roles that have backup or restore permissions.</p>

    Args:
        force_reload (bool | Unset):
        x_api_version (str):  Default: '1.3-rev2'.
        body (AclBrowserFilters | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AclBrowserResult | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        force_reload=force_reload,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AclBrowserFilters | Unset = UNSET,
    force_reload: bool | Unset = UNSET,
    x_api_version: str = "1.3-rev2",
) -> Response[AclBrowserResult | Error]:
    """Get Access Control List

     The HTTP POST request to the `/api/v1/acl` endpoint gets an array of ACL rules. <p>**Available
    to**&#58; Backup Administrator, Backup Operator, Restore Operator, Backup Viewer, Security
    Administrator. Also available to custom roles that have backup or restore permissions.</p>

    Args:
        force_reload (bool | Unset):
        x_api_version (str):  Default: '1.3-rev2'.
        body (AclBrowserFilters | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AclBrowserResult | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        force_reload=force_reload,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AclBrowserFilters | Unset = UNSET,
    force_reload: bool | Unset = UNSET,
    x_api_version: str = "1.3-rev2",
) -> AclBrowserResult | Error | None:
    """Get Access Control List

     The HTTP POST request to the `/api/v1/acl` endpoint gets an array of ACL rules. <p>**Available
    to**&#58; Backup Administrator, Backup Operator, Restore Operator, Backup Viewer, Security
    Administrator. Also available to custom roles that have backup or restore permissions.</p>

    Args:
        force_reload (bool | Unset):
        x_api_version (str):  Default: '1.3-rev2'.
        body (AclBrowserFilters | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AclBrowserResult | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            force_reload=force_reload,
            x_api_version=x_api_version,
        )
    ).parsed
