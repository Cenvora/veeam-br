from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_backup_layout_mapping_type import EBackupLayoutMappingType

T = TypeVar("T", bound="DiskLayoutAutoMappingRequest")


@_attrs_define
class DiskLayoutAutoMappingRequest:
    """Settings for automatically mapping the backup disk layout onto the live disk layout of the host.

    Attributes:
        disk_management_session_id (UUID): Disk management session ID.
        mapping_type (EBackupLayoutMappingType): Type of mapping the backup layout onto the current layout of the host.
    """

    disk_management_session_id: UUID
    mapping_type: EBackupLayoutMappingType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disk_management_session_id = str(self.disk_management_session_id)

        mapping_type = self.mapping_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "diskManagementSessionId": disk_management_session_id,
                "mappingType": mapping_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disk_management_session_id = UUID(d.pop("diskManagementSessionId"))

        mapping_type = EBackupLayoutMappingType(d.pop("mappingType"))

        disk_layout_auto_mapping_request = cls(
            disk_management_session_id=disk_management_session_id,
            mapping_type=mapping_type,
        )

        disk_layout_auto_mapping_request.additional_properties = d
        return disk_layout_auto_mapping_request

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
