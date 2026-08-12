from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiskSlotsResult")


@_attrs_define
class DiskSlotsResult:
    """Details on disk slots supported for the platform.

    Attributes:
        disk_slots (list[str] | Unset): Array of supported disk slots for platform.
    """

    disk_slots: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disk_slots: list[str] | Unset = UNSET
        if not isinstance(self.disk_slots, Unset):
            disk_slots = self.disk_slots

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disk_slots is not UNSET:
            field_dict["diskSlots"] = disk_slots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disk_slots = cast(list[str], d.pop("diskSlots", UNSET))

        disk_slots_result = cls(
            disk_slots=disk_slots,
        )

        disk_slots_result.additional_properties = d
        return disk_slots_result

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
