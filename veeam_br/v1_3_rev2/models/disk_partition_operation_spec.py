from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DiskPartitionOperationSpec")


@_attrs_define
class DiskPartitionOperationSpec:
    """Settings for a disk partition operation.

    Attributes:
        target_disk_id (UUID): Unique identifier of the disk.
        target_partition_id (UUID): Unique identifier of the partition to operate on.
    """

    target_disk_id: UUID
    target_partition_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_disk_id = str(self.target_disk_id)

        target_partition_id = str(self.target_partition_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetDiskId": target_disk_id,
                "targetPartitionId": target_partition_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_disk_id = UUID(d.pop("targetDiskId"))

        target_partition_id = UUID(d.pop("targetPartitionId"))

        disk_partition_operation_spec = cls(
            target_disk_id=target_disk_id,
            target_partition_id=target_partition_id,
        )

        disk_partition_operation_spec.additional_properties = d
        return disk_partition_operation_spec

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
