from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acl_change_effective_access_spec import AclChangeEffectiveAccessSpec
from ...models.acl_record_model import AclRecordModel
from ...models.e_acl_object_kind import EAclObjectKind
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    object_type: EAclObjectKind,
    object_id: UUID,
    *,
    body: AclChangeEffectiveAccessSpec,
    x_api_version: str = "1.3-rev2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-version"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/acl/{object_type}/{object_id}/changeEffectiveAccess".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AclRecordModel | Error | None:
    if response.status_code == 200:
        response_200 = AclRecordModel.from_dict(response.json())

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
) -> Response[AclRecordModel | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: EAclObjectKind,
    object_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AclChangeEffectiveAccessSpec,
    x_api_version: str = "1.3-rev2",
) -> Response[AclRecordModel | Error]:
    """Change Effective Access of ACL Record

     The HTTP POST request to the `/api/v1/acl/{objectType}/{objectId}/changeEffectiveAccess` endpoint
    changes the effective access of an Access Control List (ACL) record for the object that has the
    specified `objectType` and `objectId`.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        object_type (EAclObjectKind): ACL object type.
        object_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (AclChangeEffectiveAccessSpec): Settings for changing effective access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AclRecordModel | Error]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        body=body,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: EAclObjectKind,
    object_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AclChangeEffectiveAccessSpec,
    x_api_version: str = "1.3-rev2",
) -> AclRecordModel | Error | None:
    """Change Effective Access of ACL Record

     The HTTP POST request to the `/api/v1/acl/{objectType}/{objectId}/changeEffectiveAccess` endpoint
    changes the effective access of an Access Control List (ACL) record for the object that has the
    specified `objectType` and `objectId`.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        object_type (EAclObjectKind): ACL object type.
        object_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (AclChangeEffectiveAccessSpec): Settings for changing effective access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AclRecordModel | Error
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        client=client,
        body=body,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    object_type: EAclObjectKind,
    object_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AclChangeEffectiveAccessSpec,
    x_api_version: str = "1.3-rev2",
) -> Response[AclRecordModel | Error]:
    """Change Effective Access of ACL Record

     The HTTP POST request to the `/api/v1/acl/{objectType}/{objectId}/changeEffectiveAccess` endpoint
    changes the effective access of an Access Control List (ACL) record for the object that has the
    specified `objectType` and `objectId`.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        object_type (EAclObjectKind): ACL object type.
        object_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (AclChangeEffectiveAccessSpec): Settings for changing effective access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AclRecordModel | Error]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        body=body,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: EAclObjectKind,
    object_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AclChangeEffectiveAccessSpec,
    x_api_version: str = "1.3-rev2",
) -> AclRecordModel | Error | None:
    """Change Effective Access of ACL Record

     The HTTP POST request to the `/api/v1/acl/{objectType}/{objectId}/changeEffectiveAccess` endpoint
    changes the effective access of an Access Control List (ACL) record for the object that has the
    specified `objectType` and `objectId`.<p>**Available to**&#58; Backup Administrator.</p>

    Args:
        object_type (EAclObjectKind): ACL object type.
        object_id (UUID):
        x_api_version (str):  Default: '1.3-rev2'.
        body (AclChangeEffectiveAccessSpec): Settings for changing effective access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AclRecordModel | Error
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            client=client,
            body=body,
            x_api_version=x_api_version,
        )
    ).parsed
