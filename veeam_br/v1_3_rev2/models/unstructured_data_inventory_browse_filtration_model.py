from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_unstructured_data_inventory_browse_item_type import EUnstructuredDataInventoryBrowseItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredDataInventoryBrowseFiltrationModel")


@_attrs_define
class UnstructuredDataInventoryBrowseFiltrationModel:
    """Filter settings.

    Attributes:
        item_types (list[EUnstructuredDataInventoryBrowseItemType] | Unset): Filters items by their types.
    """

    item_types: list[EUnstructuredDataInventoryBrowseItemType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_types: list[str] | Unset = UNSET
        if not isinstance(self.item_types, Unset):
            item_types = []
            for item_types_item_data in self.item_types:
                item_types_item = item_types_item_data.value
                item_types.append(item_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_types is not UNSET:
            field_dict["itemTypes"] = item_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _item_types = d.pop("itemTypes", UNSET)
        item_types: list[EUnstructuredDataInventoryBrowseItemType] | Unset = UNSET
        if _item_types is not UNSET:
            item_types = []
            for item_types_item_data in _item_types:
                item_types_item = EUnstructuredDataInventoryBrowseItemType(item_types_item_data)

                item_types.append(item_types_item)

        unstructured_data_inventory_browse_filtration_model = cls(
            item_types=item_types,
        )

        unstructured_data_inventory_browse_filtration_model.additional_properties = d
        return unstructured_data_inventory_browse_filtration_model

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
