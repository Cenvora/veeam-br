from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_size_unit import ESizeUnit

T = TypeVar("T", bound="SizeModel")


@_attrs_define
class SizeModel:
    """Size value with a measurement unit.

    Attributes:
        size (int): Size value.
        unit (ESizeUnit): Measurement unit of the size value.
    """

    size: int
    unit: ESizeUnit
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size

        unit = self.unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "size": size,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        size = d.pop("size")

        unit = ESizeUnit(d.pop("unit"))

        size_model = cls(
            size=size,
            unit=unit,
        )

        size_model.additional_properties = d
        return size_model

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
