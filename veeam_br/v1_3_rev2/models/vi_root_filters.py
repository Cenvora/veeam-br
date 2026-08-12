from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_inventory_permission_scope import EInventoryPermissionScope
from ..models.e_vi_root_filters_order_column import EViRootFiltersOrderColumn
from ..types import UNSET, Unset

T = TypeVar("T", bound="ViRootFilters")


@_attrs_define
class ViRootFilters:
    """
    Attributes:
        skip (int | Unset): Number of VMware vSphere servers to skip.
        limit (int | Unset): Maximum number of VMware vSphere servers to return.
        order_column (EViRootFiltersOrderColumn | Unset): Sorts VMware vSphere servers by one of the VMware vSphere
            server parameters.
        order_asc (bool | Unset): If `true`, sorts VMware vSphere servers in ascending order by the `orderColumn`
            parameter.
        name_filter (str | Unset): Filters VMware vSphere servers by the `nameFilter` pattern. The pattern can match any
            VMware vSphere server parameter. To substitute one or more characters, use the asterisk (*) character at the
            beginning and/or at the end.
        permission_scope (EInventoryPermissionScope | Unset): Inventory permission scope.
    """

    skip: int | Unset = UNSET
    limit: int | Unset = UNSET
    order_column: EViRootFiltersOrderColumn | Unset = UNSET
    order_asc: bool | Unset = UNSET
    name_filter: str | Unset = UNSET
    permission_scope: EInventoryPermissionScope | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skip = self.skip

        limit = self.limit

        order_column: str | Unset = UNSET
        if not isinstance(self.order_column, Unset):
            order_column = self.order_column.value

        order_asc = self.order_asc

        name_filter = self.name_filter

        permission_scope: str | Unset = UNSET
        if not isinstance(self.permission_scope, Unset):
            permission_scope = self.permission_scope.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if skip is not UNSET:
            field_dict["skip"] = skip
        if limit is not UNSET:
            field_dict["limit"] = limit
        if order_column is not UNSET:
            field_dict["orderColumn"] = order_column
        if order_asc is not UNSET:
            field_dict["orderAsc"] = order_asc
        if name_filter is not UNSET:
            field_dict["nameFilter"] = name_filter
        if permission_scope is not UNSET:
            field_dict["permissionScope"] = permission_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        skip = d.pop("skip", UNSET)

        limit = d.pop("limit", UNSET)

        _order_column = d.pop("orderColumn", UNSET)
        order_column: EViRootFiltersOrderColumn | Unset
        if isinstance(_order_column, Unset):
            order_column = UNSET
        else:
            order_column = EViRootFiltersOrderColumn(_order_column)

        order_asc = d.pop("orderAsc", UNSET)

        name_filter = d.pop("nameFilter", UNSET)

        _permission_scope = d.pop("permissionScope", UNSET)
        permission_scope: EInventoryPermissionScope | Unset
        if isinstance(_permission_scope, Unset):
            permission_scope = UNSET
        else:
            permission_scope = EInventoryPermissionScope(_permission_scope)

        vi_root_filters = cls(
            skip=skip,
            limit=limit,
            order_column=order_column,
            order_asc=order_asc,
            name_filter=name_filter,
            permission_scope=permission_scope,
        )

        vi_root_filters.additional_properties = d
        return vi_root_filters

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
