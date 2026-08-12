from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.disk_model import DiskModel


T = TypeVar("T", bound="DiskMappingContext")


@_attrs_define
class DiskMappingContext:
    """Disk mapping context.

    Attributes:
        disks (list[DiskModel]): Array of disks on the machine.
        version (int): Mapping context version.
    """

    disks: list[DiskModel]
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disks = []
        for disks_item_data in self.disks:
            disks_item = disks_item_data.to_dict()
            disks.append(disks_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disks": disks,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disk_model import DiskModel

        d = dict(src_dict)
        disks = []
        _disks = d.pop("disks")
        for disks_item_data in _disks:
            disks_item = DiskModel.from_dict(disks_item_data)

            disks.append(disks_item)

        version = d.pop("version")

        disk_mapping_context = cls(
            disks=disks,
            version=version,
        )

        disk_mapping_context.additional_properties = d
        return disk_mapping_context

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
