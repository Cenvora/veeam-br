from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MbrPartitionPropsModel")


@_attrs_define
class MbrPartitionPropsModel:
    """MBR partition properties.

    Attributes:
        partition_type (int): MBR partition type identifier.
        boot (bool): If `true`, the partition is a boot partition.
        recognized_partition (bool): If `true`, the partition is a recognized partition type.
        hidden_sectors (int): Number of hidden sectors preceding the partition.
    """

    partition_type: int
    boot: bool
    recognized_partition: bool
    hidden_sectors: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partition_type = self.partition_type

        boot = self.boot

        recognized_partition = self.recognized_partition

        hidden_sectors = self.hidden_sectors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partitionType": partition_type,
                "boot": boot,
                "recognizedPartition": recognized_partition,
                "hiddenSectors": hidden_sectors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        partition_type = d.pop("partitionType")

        boot = d.pop("boot")

        recognized_partition = d.pop("recognizedPartition")

        hidden_sectors = d.pop("hiddenSectors")

        mbr_partition_props_model = cls(
            partition_type=partition_type,
            boot=boot,
            recognized_partition=recognized_partition,
            hidden_sectors=hidden_sectors,
        )

        mbr_partition_props_model.additional_properties = d
        return mbr_partition_props_model

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
