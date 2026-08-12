from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_helper_appliance_templates_filters_order_column import EHelperApplianceTemplatesFiltersOrderColumn
from ..types import UNSET, Unset

T = TypeVar("T", bound="HelperApplianceTemplatesFilters")


@_attrs_define
class HelperApplianceTemplatesFilters:
    """
    Attributes:
        skip (int | Unset): Number of mounts to skip.
        limit (int | Unset): Maximum number of mounts to return.
        order_column (EHelperApplianceTemplatesFiltersOrderColumn | Unset):
        order_asc (bool | Unset): If `true`, sorts helper appliance templates in the ascending order by the
            `orderColumn` parameter.
        location_filter (str | Unset): Filters helper appliance templates by the `locationFilter` pattern. The pattern
            can match any helper appliance template parameter.
        resource_group_filter (str | Unset): Filters helper appliance templates by the `resourceGroupFilter` pattern.
            The pattern can match any helper appliance template parameter. To substitute one or more characters, use the
            asterisk (*) character at the beginning, at the end or both.
    """

    skip: int | Unset = UNSET
    limit: int | Unset = UNSET
    order_column: EHelperApplianceTemplatesFiltersOrderColumn | Unset = UNSET
    order_asc: bool | Unset = UNSET
    location_filter: str | Unset = UNSET
    resource_group_filter: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skip = self.skip

        limit = self.limit

        order_column: str | Unset = UNSET
        if not isinstance(self.order_column, Unset):
            order_column = self.order_column.value

        order_asc = self.order_asc

        location_filter = self.location_filter

        resource_group_filter = self.resource_group_filter

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
        if location_filter is not UNSET:
            field_dict["locationFilter"] = location_filter
        if resource_group_filter is not UNSET:
            field_dict["resourceGroupFilter"] = resource_group_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        skip = d.pop("skip", UNSET)

        limit = d.pop("limit", UNSET)

        _order_column = d.pop("orderColumn", UNSET)
        order_column: EHelperApplianceTemplatesFiltersOrderColumn | Unset
        if isinstance(_order_column, Unset):
            order_column = UNSET
        else:
            order_column = EHelperApplianceTemplatesFiltersOrderColumn(_order_column)

        order_asc = d.pop("orderAsc", UNSET)

        location_filter = d.pop("locationFilter", UNSET)

        resource_group_filter = d.pop("resourceGroupFilter", UNSET)

        helper_appliance_templates_filters = cls(
            skip=skip,
            limit=limit,
            order_column=order_column,
            order_asc=order_asc,
            location_filter=location_filter,
            resource_group_filter=resource_group_filter,
        )

        helper_appliance_templates_filters.additional_properties = d
        return helper_appliance_templates_filters

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
