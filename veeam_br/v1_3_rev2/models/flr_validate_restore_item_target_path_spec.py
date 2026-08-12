from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FlrValidateRestoreItemTargetPathSpec")


@_attrs_define
class FlrValidateRestoreItemTargetPathSpec:
    """Settings to check whether a target path needs to be provided for a file-level restore item.

    Attributes:
        item_path (str): Path to the item to be restored.
        is_restore_to_original (bool): If `true`, the item is restored to its original location.
    """

    item_path: str
    is_restore_to_original: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_path = self.item_path

        is_restore_to_original = self.is_restore_to_original

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemPath": item_path,
                "isRestoreToOriginal": is_restore_to_original,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_path = d.pop("itemPath")

        is_restore_to_original = d.pop("isRestoreToOriginal")

        flr_validate_restore_item_target_path_spec = cls(
            item_path=item_path,
            is_restore_to_original=is_restore_to_original,
        )

        flr_validate_restore_item_target_path_spec.additional_properties = d
        return flr_validate_restore_item_target_path_spec

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
