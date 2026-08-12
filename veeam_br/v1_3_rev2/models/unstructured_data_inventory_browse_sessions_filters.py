from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_unstructured_data_inventory_browse_sessions_filters_order_column import (
    EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredDataInventoryBrowseSessionsFilters")


@_attrs_define
class UnstructuredDataInventoryBrowseSessionsFilters:
    """
    Attributes:
        skip (int | Unset):
        limit (int | Unset):
        order_column (EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset):
        order_asc (bool | Unset):
        session_id_filter (UUID | Unset):
        server_id_filter (UUID | Unset):
        server_name_filter (str | Unset):
    """

    skip: int | Unset = UNSET
    limit: int | Unset = UNSET
    order_column: EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset = UNSET
    order_asc: bool | Unset = UNSET
    session_id_filter: UUID | Unset = UNSET
    server_id_filter: UUID | Unset = UNSET
    server_name_filter: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skip = self.skip

        limit = self.limit

        order_column: str | Unset = UNSET
        if not isinstance(self.order_column, Unset):
            order_column = self.order_column.value

        order_asc = self.order_asc

        session_id_filter: str | Unset = UNSET
        if not isinstance(self.session_id_filter, Unset):
            session_id_filter = str(self.session_id_filter)

        server_id_filter: str | Unset = UNSET
        if not isinstance(self.server_id_filter, Unset):
            server_id_filter = str(self.server_id_filter)

        server_name_filter = self.server_name_filter

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
        if session_id_filter is not UNSET:
            field_dict["sessionIdFilter"] = session_id_filter
        if server_id_filter is not UNSET:
            field_dict["serverIdFilter"] = server_id_filter
        if server_name_filter is not UNSET:
            field_dict["serverNameFilter"] = server_name_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        skip = d.pop("skip", UNSET)

        limit = d.pop("limit", UNSET)

        _order_column = d.pop("orderColumn", UNSET)
        order_column: EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn | Unset
        if isinstance(_order_column, Unset):
            order_column = UNSET
        else:
            order_column = EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn(_order_column)

        order_asc = d.pop("orderAsc", UNSET)

        _session_id_filter = d.pop("sessionIdFilter", UNSET)
        session_id_filter: UUID | Unset
        if isinstance(_session_id_filter, Unset):
            session_id_filter = UNSET
        else:
            session_id_filter = UUID(_session_id_filter)

        _server_id_filter = d.pop("serverIdFilter", UNSET)
        server_id_filter: UUID | Unset
        if isinstance(_server_id_filter, Unset):
            server_id_filter = UNSET
        else:
            server_id_filter = UUID(_server_id_filter)

        server_name_filter = d.pop("serverNameFilter", UNSET)

        unstructured_data_inventory_browse_sessions_filters = cls(
            skip=skip,
            limit=limit,
            order_column=order_column,
            order_asc=order_asc,
            session_id_filter=session_id_filter,
            server_id_filter=server_id_filter,
            server_name_filter=server_name_filter,
        )

        unstructured_data_inventory_browse_sessions_filters.additional_properties = d
        return unstructured_data_inventory_browse_sessions_filters

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
