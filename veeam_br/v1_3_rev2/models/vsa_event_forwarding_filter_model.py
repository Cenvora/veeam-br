from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_vsa_event_severity import EVsaEventSeverity

T = TypeVar("T", bound="VsaEventForwardingFilterModel")


@_attrs_define
class VsaEventForwardingFilterModel:
    """Infrastructure metrics - VSA Syslog events forwarding filter

    Attributes:
        application (str): Application/daemon name.
        levels (list[EVsaEventSeverity]): Event levels to include.
    """

    application: str
    levels: list[EVsaEventSeverity]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application = self.application

        levels = []
        for levels_item_data in self.levels:
            levels_item = levels_item_data.value
            levels.append(levels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "application": application,
                "levels": levels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application = d.pop("application")

        levels = []
        _levels = d.pop("levels")
        for levels_item_data in _levels:
            levels_item = EVsaEventSeverity(levels_item_data)

            levels.append(levels_item)

        vsa_event_forwarding_filter_model = cls(
            application=application,
            levels=levels,
        )

        vsa_event_forwarding_filter_model.additional_properties = d
        return vsa_event_forwarding_filter_model

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
