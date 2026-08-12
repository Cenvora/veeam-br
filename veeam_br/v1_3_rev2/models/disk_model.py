from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.disk_partition_model import DiskPartitionModel
    from ..models.size_model import SizeModel


T = TypeVar("T", bound="DiskModel")


@_attrs_define
class DiskModel:
    """Disk.

    Attributes:
        number (int): Disk number.
        size (SizeModel): Size value with a measurement unit.
        is_dynamic (bool): If `true`, the disk is dynamic.
        logical_sector_size (int): Logical sector size of the disk.
        partitions (list[DiskPartitionModel]): Array of partitions on the disk.
    """

    number: int
    size: SizeModel
    is_dynamic: bool
    logical_sector_size: int
    partitions: list[DiskPartitionModel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        size = self.size.to_dict()

        is_dynamic = self.is_dynamic

        logical_sector_size = self.logical_sector_size

        partitions = []
        for partitions_item_data in self.partitions:
            partitions_item = partitions_item_data.to_dict()
            partitions.append(partitions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "size": size,
                "isDynamic": is_dynamic,
                "logicalSectorSize": logical_sector_size,
                "partitions": partitions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disk_partition_model import DiskPartitionModel
        from ..models.size_model import SizeModel

        d = dict(src_dict)
        number = d.pop("number")

        size = SizeModel.from_dict(d.pop("size"))

        is_dynamic = d.pop("isDynamic")

        logical_sector_size = d.pop("logicalSectorSize")

        partitions = []
        _partitions = d.pop("partitions")
        for partitions_item_data in _partitions:
            partitions_item = DiskPartitionModel.from_dict(partitions_item_data)

            partitions.append(partitions_item)

        disk_model = cls(
            number=number,
            size=size,
            is_dynamic=is_dynamic,
            logical_sector_size=logical_sector_size,
            partitions=partitions,
        )

        disk_model.additional_properties = d
        return disk_model

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
