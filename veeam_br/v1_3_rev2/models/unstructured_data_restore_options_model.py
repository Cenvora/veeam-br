from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unstructured_data_restore_permissions_model import UnstructuredDataRestorePermissionsModel


T = TypeVar("T", bound="UnstructuredDataRestoreOptionsModel")


@_attrs_define
class UnstructuredDataRestoreOptionsModel:
    """Options for Instant File Share Recovery.

    Attributes:
        restore_point_id (UUID): Restore point ID. To get the ID, run the [Get All Restore Points](Restore-
            Points#operation/GetAllObjectRestorePoints) request.
        permissions (UnstructuredDataRestorePermissionsModel): Permissions for Instant File Share Recovery.
        mount_server_id (UUID | Unset): Mount server ID. The ID is the same as the ID of the managed server that was
            assigned a mount server role. To obtain the ID, run the [Get Mount Servers](Mount-
            Servers#operation/GetAllMountServers) request.<p> Do not specify this parameter if you have set the
            `autoSelectMountServers` property to `true`.
    """

    restore_point_id: UUID
    permissions: UnstructuredDataRestorePermissionsModel
    mount_server_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_point_id = str(self.restore_point_id)

        permissions = self.permissions.to_dict()

        mount_server_id: str | Unset = UNSET
        if not isinstance(self.mount_server_id, Unset):
            mount_server_id = str(self.mount_server_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restorePointId": restore_point_id,
                "permissions": permissions,
            }
        )
        if mount_server_id is not UNSET:
            field_dict["mountServerId"] = mount_server_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unstructured_data_restore_permissions_model import UnstructuredDataRestorePermissionsModel

        d = dict(src_dict)
        restore_point_id = UUID(d.pop("restorePointId"))

        permissions = UnstructuredDataRestorePermissionsModel.from_dict(d.pop("permissions"))

        _mount_server_id = d.pop("mountServerId", UNSET)
        mount_server_id: UUID | Unset
        if isinstance(_mount_server_id, Unset):
            mount_server_id = UNSET
        else:
            mount_server_id = UUID(_mount_server_id)

        unstructured_data_restore_options_model = cls(
            restore_point_id=restore_point_id,
            permissions=permissions,
            mount_server_id=mount_server_id,
        )

        unstructured_data_restore_options_model.additional_properties = d
        return unstructured_data_restore_options_model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
