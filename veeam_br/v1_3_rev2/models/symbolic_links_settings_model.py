from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SymbolicLinksSettingsModel")


@_attrs_define
class SymbolicLinksSettingsModel:
    """Symbolic links settings.

    Attributes:
        include_symbolic_link_content (bool | Unset): If `true`, the backup job includes the content of symbolic links.
    """

    include_symbolic_link_content: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_symbolic_link_content = self.include_symbolic_link_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_symbolic_link_content is not UNSET:
            field_dict["includeSymbolicLinkContent"] = include_symbolic_link_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_symbolic_link_content = d.pop("includeSymbolicLinkContent", UNSET)

        symbolic_links_settings_model = cls(
            include_symbolic_link_content=include_symbolic_link_content,
        )

        symbolic_links_settings_model.additional_properties = d
        return symbolic_links_settings_model

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
