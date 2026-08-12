from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.restore_layout import RestoreLayout


T = TypeVar("T", bound="DiskLayoutAutoMappingResult")


@_attrs_define
class DiskLayoutAutoMappingResult:
    """Restore layout produced by the auto-mapping attempt.

    Attributes:
        success (bool): If `true`, the disk layout was mapped automatically.
        restore_layout (RestoreLayout): Restore layout for agent or recovery appliance.
    """

    success: bool
    restore_layout: RestoreLayout
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        restore_layout = self.restore_layout.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "restoreLayout": restore_layout,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.restore_layout import RestoreLayout

        d = dict(src_dict)
        success = d.pop("success")

        restore_layout = RestoreLayout.from_dict(d.pop("restoreLayout"))

        disk_layout_auto_mapping_result = cls(
            success=success,
            restore_layout=restore_layout,
        )

        disk_layout_auto_mapping_result.additional_properties = d
        return disk_layout_auto_mapping_result

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
