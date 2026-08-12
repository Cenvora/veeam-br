from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.general_options_host_authentication_import_model import GeneralOptionsHostAuthenticationImportModel
from ...models.general_options_host_authentication_import_result_model import (
    GeneralOptionsHostAuthenticationImportResultModel,
)
from ...types import Response


def _get_kwargs(
    *,
    body: GeneralOptionsHostAuthenticationImportModel,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/generalOptions/hostAuthentication/importTrustedHosts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GeneralOptionsHostAuthenticationImportResultModel | None:
    if response.status_code == 200:
        response_200 = GeneralOptionsHostAuthenticationImportResultModel.from_dict(response.json())

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
) -> Response[Error | GeneralOptionsHostAuthenticationImportResultModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GeneralOptionsHostAuthenticationImportModel,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | GeneralOptionsHostAuthenticationImportResultModel]:
    """Import Trusted Hosts List from a File

     The HTTP POST request to the `/api/v1/generalOptions/hostAuthentication/importTrustedHosts` endpoint
    imports trusted hosts from a file using the configured settings.<p>**Available to**&#58; Backup
    Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (GeneralOptionsHostAuthenticationImportModel): Settings for importing the list of
            trusted hosts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GeneralOptionsHostAuthenticationImportResultModel]
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
    body: GeneralOptionsHostAuthenticationImportModel,
    x_api_version: str = "1.3-rev2",
) -> Error | GeneralOptionsHostAuthenticationImportResultModel | None:
    """Import Trusted Hosts List from a File

     The HTTP POST request to the `/api/v1/generalOptions/hostAuthentication/importTrustedHosts` endpoint
    imports trusted hosts from a file using the configured settings.<p>**Available to**&#58; Backup
    Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (GeneralOptionsHostAuthenticationImportModel): Settings for importing the list of
            trusted hosts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GeneralOptionsHostAuthenticationImportResultModel
    """

    return sync_detailed(
        client=client,
        body=body,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GeneralOptionsHostAuthenticationImportModel,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | GeneralOptionsHostAuthenticationImportResultModel]:
    """Import Trusted Hosts List from a File

     The HTTP POST request to the `/api/v1/generalOptions/hostAuthentication/importTrustedHosts` endpoint
    imports trusted hosts from a file using the configured settings.<p>**Available to**&#58; Backup
    Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (GeneralOptionsHostAuthenticationImportModel): Settings for importing the list of
            trusted hosts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GeneralOptionsHostAuthenticationImportResultModel]
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
    body: GeneralOptionsHostAuthenticationImportModel,
    x_api_version: str = "1.3-rev2",
) -> Error | GeneralOptionsHostAuthenticationImportResultModel | None:
    """Import Trusted Hosts List from a File

     The HTTP POST request to the `/api/v1/generalOptions/hostAuthentication/importTrustedHosts` endpoint
    imports trusted hosts from a file using the configured settings.<p>**Available to**&#58; Backup
    Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (GeneralOptionsHostAuthenticationImportModel): Settings for importing the list of
            trusted hosts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GeneralOptionsHostAuthenticationImportResultModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_api_version=x_api_version,
        )
    ).parsed
