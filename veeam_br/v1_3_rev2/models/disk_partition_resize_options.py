from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.size_model import SizeModel


T = TypeVar("T", bound="DiskPartitionResizeOptions")


@_attrs_define
class DiskPartitionResizeOptions:
    """Disk partition resize options.

    Attributes:
        volume_label (str): Volume label.
        current_size (SizeModel): Size value with a measurement unit.
        maximum_size (SizeModel): Size value with a measurement unit.
        minimum_size (SizeModel): Size value with a measurement unit.
    """

    volume_label: str
    current_size: SizeModel
    maximum_size: SizeModel
    minimum_size: SizeModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_label = self.volume_label

        current_size = self.current_size.to_dict()

        maximum_size = self.maximum_size.to_dict()

        minimum_size = self.minimum_size.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "volumeLabel": volume_label,
                "currentSize": current_size,
                "maximumSize": maximum_size,
                "minimumSize": minimum_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.size_model import SizeModel

        d = dict(src_dict)
        volume_label = d.pop("volumeLabel")

        current_size = SizeModel.from_dict(d.pop("currentSize"))

        maximum_size = SizeModel.from_dict(d.pop("maximumSize"))

        minimum_size = SizeModel.from_dict(d.pop("minimumSize"))

        disk_partition_resize_options = cls(
            volume_label=volume_label,
            current_size=current_size,
            maximum_size=maximum_size,
            minimum_size=minimum_size,
        )

        disk_partition_resize_options.additional_properties = d
        return disk_partition_resize_options

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
