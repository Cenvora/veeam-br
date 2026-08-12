from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.vsa_event_forwarding_daemon_settings_model import VsaEventForwardingDaemonSettingsModel
from ...types import Response


def _get_kwargs(
    *,
    body: VsaEventForwardingDaemonSettingsModel,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/generalOptions/vsaEventForwarding/daemonSettings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VsaEventForwardingDaemonSettingsModel,
    x_api_version: str = "1.3-rev2",
) -> Response[Any | Error]:
    """Edit Daemon Settings for VSA Event Forwarding

     The HTTP PUT request to the `/api/v1/generalOptions/vsaEventForwarding/daemonSettings` path allows
    you to update Infrastructure Metrics Syslog daemon event forwarding configuration. <p>**Available
    to**: Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (VsaEventForwardingDaemonSettingsModel): Infrastructure metrics — VSA Syslog event
            forwarding daemon settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    body: VsaEventForwardingDaemonSettingsModel,
    x_api_version: str = "1.3-rev2",
) -> Any | Error | None:
    """Edit Daemon Settings for VSA Event Forwarding

     The HTTP PUT request to the `/api/v1/generalOptions/vsaEventForwarding/daemonSettings` path allows
    you to update Infrastructure Metrics Syslog daemon event forwarding configuration. <p>**Available
    to**: Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (VsaEventForwardingDaemonSettingsModel): Infrastructure metrics — VSA Syslog event
            forwarding daemon settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VsaEventForwardingDaemonSettingsModel,
    x_api_version: str = "1.3-rev2",
) -> Response[Any | Error]:
    """Edit Daemon Settings for VSA Event Forwarding

     The HTTP PUT request to the `/api/v1/generalOptions/vsaEventForwarding/daemonSettings` path allows
    you to update Infrastructure Metrics Syslog daemon event forwarding configuration. <p>**Available
    to**: Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (VsaEventForwardingDaemonSettingsModel): Infrastructure metrics — VSA Syslog event
            forwarding daemon settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    body: VsaEventForwardingDaemonSettingsModel,
    x_api_version: str = "1.3-rev2",
) -> Any | Error | None:
    """Edit Daemon Settings for VSA Event Forwarding

     The HTTP PUT request to the `/api/v1/generalOptions/vsaEventForwarding/daemonSettings` path allows
    you to update Infrastructure Metrics Syslog daemon event forwarding configuration. <p>**Available
    to**: Backup Administrator.</p>

    Args:
        x_api_version (str):  Default: '1.3-rev2'.
        body (VsaEventForwardingDaemonSettingsModel): Infrastructure metrics — VSA Syslog event
            forwarding daemon settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_api_version=x_api_version,
        )
    ).parsed
