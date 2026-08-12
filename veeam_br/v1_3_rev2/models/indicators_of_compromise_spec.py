from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IndicatorsOfCompromiseSpec")


@_attrs_define
class IndicatorsOfCompromiseSpec:
    """Details on indicators of compromise.

    Attributes:
        indicators_of_compromise (list[str]): Array of objects containing details on indicators of compromise.
    """

    indicators_of_compromise: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indicators_of_compromise = self.indicators_of_compromise

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "indicatorsOfCompromise": indicators_of_compromise,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        indicators_of_compromise = cast(list[str], d.pop("indicatorsOfCompromise"))

        indicators_of_compromise_spec = cls(
            indicators_of_compromise=indicators_of_compromise,
        )

        indicators_of_compromise_spec.additional_properties = d
        return indicators_of_compromise_spec

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
