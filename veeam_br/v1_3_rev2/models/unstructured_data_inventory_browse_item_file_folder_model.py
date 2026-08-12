from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.e_unstructured_data_inventory_browse_item_type import EUnstructuredDataInventoryBrowseItemType

T = TypeVar("T", bound="UnstructuredDataInventoryBrowseItemFileFolderModel")


@_attrs_define
class UnstructuredDataInventoryBrowseItemFileFolderModel:
    """Unstructured data file or folder item.

    Attributes:
        name (str): Name of the item.
        item_type (EUnstructuredDataInventoryBrowseItemType): Unstructured data item type.
        full_name (str): Item full name.
        is_symbolic_link (bool): If `true`, the item is a symbolic link.
        modified_date (datetime.datetime): Date and time when the item was last modified.
        size (int): Item size in bytes.
    """

    name: str
    item_type: EUnstructuredDataInventoryBrowseItemType
    full_name: str
    is_symbolic_link: bool
    modified_date: datetime.datetime
    size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        item_type = self.item_type.value

        full_name = self.full_name

        is_symbolic_link = self.is_symbolic_link

        modified_date = self.modified_date.isoformat()

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "itemType": item_type,
                "fullName": full_name,
                "isSymbolicLink": is_symbolic_link,
                "modifiedDate": modified_date,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        item_type = EUnstructuredDataInventoryBrowseItemType(d.pop("itemType"))

        full_name = d.pop("fullName")

        is_symbolic_link = d.pop("isSymbolicLink")

        modified_date = isoparse(d.pop("modifiedDate"))

        size = d.pop("size")

        unstructured_data_inventory_browse_item_file_folder_model = cls(
            name=name,
            item_type=item_type,
            full_name=full_name,
            is_symbolic_link=is_symbolic_link,
            modified_date=modified_date,
            size=size,
        )

        unstructured_data_inventory_browse_item_file_folder_model.additional_properties = d
        return unstructured_data_inventory_browse_item_file_folder_model

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
