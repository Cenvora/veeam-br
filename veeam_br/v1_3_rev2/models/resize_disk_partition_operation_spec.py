from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.partition_info_model import PartitionInfoModel
    from ..models.size_model import SizeModel


T = TypeVar("T", bound="ResizeDiskPartitionOperationSpec")


@_attrs_define
class ResizeDiskPartitionOperationSpec:
    """Settings for resizing a disk partition.

    Attributes:
        partition_info (PartitionInfoModel): Disk partition information.
        new_size (SizeModel): Size value with a measurement unit.
    """

    partition_info: PartitionInfoModel
    new_size: SizeModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partition_info = self.partition_info.to_dict()

        new_size = self.new_size.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partitionInfo": partition_info,
                "newSize": new_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partition_info_model import PartitionInfoModel
        from ..models.size_model import SizeModel

        d = dict(src_dict)
        partition_info = PartitionInfoModel.from_dict(d.pop("partitionInfo"))

        new_size = SizeModel.from_dict(d.pop("newSize"))

        resize_disk_partition_operation_spec = cls(
            partition_info=partition_info,
            new_size=new_size,
        )

        resize_disk_partition_operation_spec.additional_properties = d
        return resize_disk_partition_operation_spec

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
