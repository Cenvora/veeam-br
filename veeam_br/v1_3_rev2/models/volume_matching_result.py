from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_partition_role import EPartitionRole

T = TypeVar("T", bound="VolumeMatchingResult")


@_attrs_define
class VolumeMatchingResult:
    """Automatically matched volume of a host.

    Attributes:
        id (UUID): Volume unique identifier.
        display_name (str): Volume mount point or path.
        disk_number (int): Disk number.
        matched (bool): If `true`, the volume was matched automatically.
        role (EPartitionRole): Role of partition.
    """

    id: UUID
    display_name: str
    disk_number: int
    matched: bool
    role: EPartitionRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        display_name = self.display_name

        disk_number = self.disk_number

        matched = self.matched

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
                "diskNumber": disk_number,
                "matched": matched,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        display_name = d.pop("displayName")

        disk_number = d.pop("diskNumber")

        matched = d.pop("matched")

        role = EPartitionRole(d.pop("role"))

        volume_matching_result = cls(
            id=id,
            display_name=display_name,
            disk_number=disk_number,
            matched=matched,
            role=role,
        )

        volume_matching_result.additional_properties = d
        return volume_matching_result

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
