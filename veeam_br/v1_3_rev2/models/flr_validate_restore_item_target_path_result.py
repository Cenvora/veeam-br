from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FlrValidateRestoreItemTargetPathResult")


@_attrs_define
class FlrValidateRestoreItemTargetPathResult:
    """Result of a check whether a target path needs to be provided for a file-level restore item.

    Attributes:
        is_target_path_needed (bool): If `true`, a target path must be provided to restore the item.
        target_path (str): Path to which the item will be restored.
    """

    is_target_path_needed: bool
    target_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_target_path_needed = self.is_target_path_needed

        target_path = self.target_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isTargetPathNeeded": is_target_path_needed,
                "targetPath": target_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_target_path_needed = d.pop("isTargetPathNeeded")

        target_path = d.pop("targetPath")

        flr_validate_restore_item_target_path_result = cls(
            is_target_path_needed=is_target_path_needed,
            target_path=target_path,
        )

        flr_validate_restore_item_target_path_result.additional_properties = d
        return flr_validate_restore_item_target_path_result

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
