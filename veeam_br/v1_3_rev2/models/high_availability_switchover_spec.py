from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HighAvailabilitySwitchoverSpec")


@_attrs_define
class HighAvailabilitySwitchoverSpec:
    """High Availability cluster switchover settings.

    Attributes:
        ignore_lag (bool | Unset): If `true`, proceeds with switchover despite replication lag, accepting potential data
            loss. Default: False.
    """

    ignore_lag: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ignore_lag = self.ignore_lag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ignore_lag is not UNSET:
            field_dict["ignoreLag"] = ignore_lag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ignore_lag = d.pop("ignoreLag", UNSET)

        high_availability_switchover_spec = cls(
            ignore_lag=ignore_lag,
        )

        high_availability_switchover_spec.additional_properties = d
        return high_availability_switchover_spec

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
