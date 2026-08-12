from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_unstructured_data_inventory_browse_item_type import EUnstructuredDataInventoryBrowseItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_spec import PaginationSpec
    from ..models.unstructured_data_inventory_browse_filtration_model import (
        UnstructuredDataInventoryBrowseFiltrationModel,
    )
    from ..models.unstructured_data_inventory_browse_order_spec import UnstructuredDataInventoryBrowseOrderSpec


T = TypeVar("T", bound="UnstructuredDataInventoryBrowseFolderSpec")


@_attrs_define
class UnstructuredDataInventoryBrowseFolderSpec:
    """Browser settings.

    Attributes:
        path (str): Browsing path.
        path_type (EUnstructuredDataInventoryBrowseItemType | Unset): Unstructured data item type.
        filter_ (UnstructuredDataInventoryBrowseFiltrationModel | Unset): Filter settings.
        order (UnstructuredDataInventoryBrowseOrderSpec | Unset): Sorting settings.
        pagination (PaginationSpec | Unset): Pagination settings.
    """

    path: str
    path_type: EUnstructuredDataInventoryBrowseItemType | Unset = UNSET
    filter_: UnstructuredDataInventoryBrowseFiltrationModel | Unset = UNSET
    order: UnstructuredDataInventoryBrowseOrderSpec | Unset = UNSET
    pagination: PaginationSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        path_type: str | Unset = UNSET
        if not isinstance(self.path_type, Unset):
            path_type = self.path_type.value

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        order: dict[str, Any] | Unset = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if path_type is not UNSET:
            field_dict["pathType"] = path_type
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if order is not UNSET:
            field_dict["order"] = order
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_spec import PaginationSpec
        from ..models.unstructured_data_inventory_browse_filtration_model import (
            UnstructuredDataInventoryBrowseFiltrationModel,
        )
        from ..models.unstructured_data_inventory_browse_order_spec import UnstructuredDataInventoryBrowseOrderSpec

        d = dict(src_dict)
        path = d.pop("path")

        _path_type = d.pop("pathType", UNSET)
        path_type: EUnstructuredDataInventoryBrowseItemType | Unset
        if isinstance(_path_type, Unset):
            path_type = UNSET
        else:
            path_type = EUnstructuredDataInventoryBrowseItemType(_path_type)

        _filter_ = d.pop("filter", UNSET)
        filter_: UnstructuredDataInventoryBrowseFiltrationModel | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = UnstructuredDataInventoryBrowseFiltrationModel.from_dict(_filter_)

        _order = d.pop("order", UNSET)
        order: UnstructuredDataInventoryBrowseOrderSpec | Unset
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = UnstructuredDataInventoryBrowseOrderSpec.from_dict(_order)

        _pagination = d.pop("pagination", UNSET)
        pagination: PaginationSpec | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = PaginationSpec.from_dict(_pagination)

        unstructured_data_inventory_browse_folder_spec = cls(
            path=path,
            path_type=path_type,
            filter_=filter_,
            order=order,
            pagination=pagination,
        )

        unstructured_data_inventory_browse_folder_spec.additional_properties = d
        return unstructured_data_inventory_browse_folder_spec

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
