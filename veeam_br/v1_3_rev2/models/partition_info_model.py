from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_partition_style import EPartitionStyle
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gpt_partition_props_model import GptPartitionPropsModel
    from ..models.mbr_partition_props_model import MbrPartitionPropsModel
    from ..models.size_model import SizeModel


T = TypeVar("T", bound="PartitionInfoModel")


@_attrs_define
class PartitionInfoModel:
    """Disk partition information.

    Attributes:
        disk_number (int): Disk number where the partition resides.
        part_number (int): Partition number on the disk.
        starting_offset (SizeModel): Size value with a measurement unit.
        partition_length (SizeModel): Size value with a measurement unit.
        display_name (str): Partition display name.
        partition_style (EPartitionStyle): Partition style of the disk.
        mbr_props (MbrPartitionPropsModel | Unset): MBR partition properties.
        gpt_props (GptPartitionPropsModel | Unset): GUID Partition Table (GPT) properties.
    """

    disk_number: int
    part_number: int
    starting_offset: SizeModel
    partition_length: SizeModel
    display_name: str
    partition_style: EPartitionStyle
    mbr_props: MbrPartitionPropsModel | Unset = UNSET
    gpt_props: GptPartitionPropsModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disk_number = self.disk_number

        part_number = self.part_number

        starting_offset = self.starting_offset.to_dict()

        partition_length = self.partition_length.to_dict()

        display_name = self.display_name

        partition_style = self.partition_style.value

        mbr_props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mbr_props, Unset):
            mbr_props = self.mbr_props.to_dict()

        gpt_props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpt_props, Unset):
            gpt_props = self.gpt_props.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "diskNumber": disk_number,
                "partNumber": part_number,
                "startingOffset": starting_offset,
                "partitionLength": partition_length,
                "displayName": display_name,
                "partitionStyle": partition_style,
            }
        )
        if mbr_props is not UNSET:
            field_dict["mbrProps"] = mbr_props
        if gpt_props is not UNSET:
            field_dict["gptProps"] = gpt_props

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gpt_partition_props_model import GptPartitionPropsModel
        from ..models.mbr_partition_props_model import MbrPartitionPropsModel
        from ..models.size_model import SizeModel

        d = dict(src_dict)
        disk_number = d.pop("diskNumber")

        part_number = d.pop("partNumber")

        starting_offset = SizeModel.from_dict(d.pop("startingOffset"))

        partition_length = SizeModel.from_dict(d.pop("partitionLength"))

        display_name = d.pop("displayName")

        partition_style = EPartitionStyle(d.pop("partitionStyle"))

        _mbr_props = d.pop("mbrProps", UNSET)
        mbr_props: MbrPartitionPropsModel | Unset
        if isinstance(_mbr_props, Unset):
            mbr_props = UNSET
        else:
            mbr_props = MbrPartitionPropsModel.from_dict(_mbr_props)

        _gpt_props = d.pop("gptProps", UNSET)
        gpt_props: GptPartitionPropsModel | Unset
        if isinstance(_gpt_props, Unset):
            gpt_props = UNSET
        else:
            gpt_props = GptPartitionPropsModel.from_dict(_gpt_props)

        partition_info_model = cls(
            disk_number=disk_number,
            part_number=part_number,
            starting_offset=starting_offset,
            partition_length=partition_length,
            display_name=display_name,
            partition_style=partition_style,
            mbr_props=mbr_props,
            gpt_props=gpt_props,
        )

        partition_info_model.additional_properties = d
        return partition_info_model

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
