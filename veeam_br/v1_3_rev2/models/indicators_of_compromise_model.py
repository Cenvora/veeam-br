from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_indicator_of_compromise_monitoring_status import EIndicatorOfCompromiseMonitoringStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndicatorsOfCompromiseModel")


@_attrs_define
class IndicatorsOfCompromiseModel:
    """Indicators of compromise to monitor

    Attributes:
        name (str | Unset): Name of the indicator of compromise.
        description (str | Unset): Description of the indicator of compromise.
        status (EIndicatorOfCompromiseMonitoringStatus | Unset): Indicator of compromise monitoring status.
        attack_tactic (str | Unset): Attack tactic associated with the indicator of compromise.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    status: EIndicatorOfCompromiseMonitoringStatus | Unset = UNSET
    attack_tactic: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        attack_tactic = self.attack_tactic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if attack_tactic is not UNSET:
            field_dict["attackTactic"] = attack_tactic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: EIndicatorOfCompromiseMonitoringStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EIndicatorOfCompromiseMonitoringStatus(_status)

        attack_tactic = d.pop("attackTactic", UNSET)

        indicators_of_compromise_model = cls(
            name=name,
            description=description,
            status=status,
            attack_tactic=attack_tactic,
        )

        indicators_of_compromise_model.additional_properties = d
        return indicators_of_compromise_model

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
