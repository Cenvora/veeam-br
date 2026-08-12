from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GptPartitionPropsModel")


@_attrs_define
class GptPartitionPropsModel:
    """GUID Partition Table (GPT) properties.

    Attributes:
        part_id (UUID): GUID that uniquely identifies the GPT partition.
        part_type (UUID): GUID that identifies the partition type.
        attrs (str): Attributes of the GPT partition.
        name (str | Unset): GPT partition name.
    """

    part_id: UUID
    part_type: UUID
    attrs: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        part_id = str(self.part_id)

        part_type = str(self.part_type)

        attrs = self.attrs

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partId": part_id,
                "partType": part_type,
                "attrs": attrs,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        part_id = UUID(d.pop("partId"))

        part_type = UUID(d.pop("partType"))

        attrs = d.pop("attrs")

        name = d.pop("name", UNSET)

        gpt_partition_props_model = cls(
            part_id=part_id,
            part_type=part_type,
            attrs=attrs,
            name=name,
        )

        gpt_partition_props_model.additional_properties = d
        return gpt_partition_props_model

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
