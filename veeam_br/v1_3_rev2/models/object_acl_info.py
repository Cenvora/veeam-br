from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ObjectAclInfo")


@_attrs_define
class ObjectAclInfo:
    """ACL-based object availability information.

    Attributes:
        is_allowed (bool): If `true`, the object is available for selection based on the user's ACL permissions and the
            user can select and use it. If `false`, the object is displayed but cannot be selected. If not present, defaults
            to `true`.
    """

    is_allowed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_allowed = self.is_allowed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isAllowed": is_allowed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_allowed = d.pop("isAllowed")

        object_acl_info = cls(
            is_allowed=is_allowed,
        )

        object_acl_info.additional_properties = d
        return object_acl_info

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
