from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_volume_restore_host_type import EVolumeRestoreHostType

T = TypeVar("T", bound="DiskManagementInitializationRequest")


@_attrs_define
class DiskManagementInitializationRequest:
    """Settings for initializing disk management for a host.

    Attributes:
        id (UUID): Agent or recovery appliance ID.
        oib_id (UUID): Restore point ID.
        host_type (EVolumeRestoreHostType): Type of host on which the volumes will be restored.
    """

    id: UUID
    oib_id: UUID
    host_type: EVolumeRestoreHostType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        oib_id = str(self.oib_id)

        host_type = self.host_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "oibId": oib_id,
                "hostType": host_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        oib_id = UUID(d.pop("oibId"))

        host_type = EVolumeRestoreHostType(d.pop("hostType"))

        disk_management_initialization_request = cls(
            id=id,
            oib_id=oib_id,
            host_type=host_type,
        )

        disk_management_initialization_request.additional_properties = d
        return disk_management_initialization_request

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
