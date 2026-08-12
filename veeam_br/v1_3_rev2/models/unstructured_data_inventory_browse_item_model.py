from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_unstructured_data_inventory_browse_item_type import EUnstructuredDataInventoryBrowseItemType

T = TypeVar("T", bound="UnstructuredDataInventoryBrowseItemModel")


@_attrs_define
class UnstructuredDataInventoryBrowseItemModel:
    """Unstructured data item.

    Attributes:
        name (str): Name of the item.
        item_type (EUnstructuredDataInventoryBrowseItemType): Unstructured data item type.
    """

    name: str
    item_type: EUnstructuredDataInventoryBrowseItemType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        item_type = self.item_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "itemType": item_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        item_type = EUnstructuredDataInventoryBrowseItemType(d.pop("itemType"))

        unstructured_data_inventory_browse_item_model = cls(
            name=name,
            item_type=item_type,
        )

        unstructured_data_inventory_browse_item_model.additional_properties = d
        return unstructured_data_inventory_browse_item_model

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
