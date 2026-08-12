from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.helper_appliance_template_state_model import HelperApplianceTemplateStateModel
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/backupInfrastructure/helperApplianceTemplates/{id}/state".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | HelperApplianceTemplateStateModel | None:
    if response.status_code == 200:
        response_200 = HelperApplianceTemplateStateModel.from_dict(response.json())

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
) -> Response[Error | HelperApplianceTemplateStateModel]:
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
    x_api_version: str = "1.3-rev2",
) -> Response[Error | HelperApplianceTemplateStateModel]:
    """Get Helper Appliance Template State

     The HTTP GET request to the `/api/v1/backupInfrastructure/helperApplianceTemplates/{id}/state`
    endpoint gets the state of the helper appliance template that has the specified `id`. The state
    shows where the template is deployed (its Microsoft Azure subscription and region) and its current
    status, for example whether the template is up to date or must be upgraded.<p>**Available to**&#58;
    Backup Administrator, Restore Operator. Also available to custom roles that have backup or restore
    permissions.</p>

    Args:
        id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HelperApplianceTemplateStateModel]
    """

    kwargs = _get_kwargs(
        id=id,
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
    x_api_version: str = "1.3-rev2",
) -> Error | HelperApplianceTemplateStateModel | None:
    """Get Helper Appliance Template State

     The HTTP GET request to the `/api/v1/backupInfrastructure/helperApplianceTemplates/{id}/state`
    endpoint gets the state of the helper appliance template that has the specified `id`. The state
    shows where the template is deployed (its Microsoft Azure subscription and region) and its current
    status, for example whether the template is up to date or must be upgraded.<p>**Available to**&#58;
    Backup Administrator, Restore Operator. Also available to custom roles that have backup or restore
    permissions.</p>

    Args:
        id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HelperApplianceTemplateStateModel
    """

    return sync_detailed(
        id=id,
        client=client,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Response[Error | HelperApplianceTemplateStateModel]:
    """Get Helper Appliance Template State

     The HTTP GET request to the `/api/v1/backupInfrastructure/helperApplianceTemplates/{id}/state`
    endpoint gets the state of the helper appliance template that has the specified `id`. The state
    shows where the template is deployed (its Microsoft Azure subscription and region) and its current
    status, for example whether the template is up to date or must be upgraded.<p>**Available to**&#58;
    Backup Administrator, Restore Operator. Also available to custom roles that have backup or restore
    permissions.</p>

    Args:
        id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HelperApplianceTemplateStateModel]
    """

    kwargs = _get_kwargs(
        id=id,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_api_version: str = "1.3-rev2",
) -> Error | HelperApplianceTemplateStateModel | None:
    """Get Helper Appliance Template State

     The HTTP GET request to the `/api/v1/backupInfrastructure/helperApplianceTemplates/{id}/state`
    endpoint gets the state of the helper appliance template that has the specified `id`. The state
    shows where the template is deployed (its Microsoft Azure subscription and region) and its current
    status, for example whether the template is up to date or must be upgraded.<p>**Available to**&#58;
    Backup Administrator, Restore Operator. Also available to custom roles that have backup or restore
    permissions.</p>

    Args:
        id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HelperApplianceTemplateStateModel
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_api_version=x_api_version,
        )
    ).parsed
