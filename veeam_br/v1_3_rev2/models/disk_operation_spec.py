from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiskOperationSpec")


@_attrs_define
class DiskOperationSpec:
    """Settings for a disk operation.

    Attributes:
        target_disk_number (int): Disk number of the destination disk to apply the layout to.
        source_disk_number (int | Unset): Disk number of the backup disk layout to apply from.
    """

    target_disk_number: int
    source_disk_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_disk_number = self.target_disk_number

        source_disk_number = self.source_disk_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetDiskNumber": target_disk_number,
            }
        )
        if source_disk_number is not UNSET:
            field_dict["sourceDiskNumber"] = source_disk_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_disk_number = d.pop("targetDiskNumber")

        source_disk_number = d.pop("sourceDiskNumber", UNSET)

        disk_operation_spec = cls(
            target_disk_number=target_disk_number,
            source_disk_number=source_disk_number,
        )

        disk_operation_spec.additional_properties = d
        return disk_operation_spec

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
