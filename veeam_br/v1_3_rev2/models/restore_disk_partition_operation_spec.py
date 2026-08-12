from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.size_model import SizeModel


T = TypeVar("T", bound="RestoreDiskPartitionOperationSpec")


@_attrs_define
class RestoreDiskPartitionOperationSpec:
    """Settings for restoring a disk partition.

    Attributes:
        target_disk_number (int): Disk number of the target disk.
        target_disk_logical_sector_size (int): Logical sector size of the target disk.
        is_target_disk_dynamic (bool): If `true`, the target disk is dynamic.
        target_partition_starting_offset (SizeModel): Size value with a measurement unit.
        source_disk_number (int): Disk number of the original disk to restore from.
        source_partition_number (int): Partition number of the original partition to restore from.
    """

    target_disk_number: int
    target_disk_logical_sector_size: int
    is_target_disk_dynamic: bool
    target_partition_starting_offset: SizeModel
    source_disk_number: int
    source_partition_number: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_disk_number = self.target_disk_number

        target_disk_logical_sector_size = self.target_disk_logical_sector_size

        is_target_disk_dynamic = self.is_target_disk_dynamic

        target_partition_starting_offset = self.target_partition_starting_offset.to_dict()

        source_disk_number = self.source_disk_number

        source_partition_number = self.source_partition_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetDiskNumber": target_disk_number,
                "targetDiskLogicalSectorSize": target_disk_logical_sector_size,
                "isTargetDiskDynamic": is_target_disk_dynamic,
                "targetPartitionStartingOffset": target_partition_starting_offset,
                "sourceDiskNumber": source_disk_number,
                "sourcePartitionNumber": source_partition_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.size_model import SizeModel

        d = dict(src_dict)
        target_disk_number = d.pop("targetDiskNumber")

        target_disk_logical_sector_size = d.pop("targetDiskLogicalSectorSize")

        is_target_disk_dynamic = d.pop("isTargetDiskDynamic")

        target_partition_starting_offset = SizeModel.from_dict(d.pop("targetPartitionStartingOffset"))

        source_disk_number = d.pop("sourceDiskNumber")

        source_partition_number = d.pop("sourcePartitionNumber")

        restore_disk_partition_operation_spec = cls(
            target_disk_number=target_disk_number,
            target_disk_logical_sector_size=target_disk_logical_sector_size,
            is_target_disk_dynamic=is_target_disk_dynamic,
            target_partition_starting_offset=target_partition_starting_offset,
            source_disk_number=source_disk_number,
            source_partition_number=source_partition_number,
        )

        restore_disk_partition_operation_spec.additional_properties = d
        return restore_disk_partition_operation_spec

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
