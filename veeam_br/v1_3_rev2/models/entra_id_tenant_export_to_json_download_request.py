from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entra_id_tenant_export_to_json_download_request_item import (
        EntraIdTenantExportToJsonDownloadRequestItem,
    )


T = TypeVar("T", bound="EntraIdTenantExportToJsonDownloadRequest")


@_attrs_define
class EntraIdTenantExportToJsonDownloadRequest:
    """Export Microsoft Entra ID items to JSON.

    Attributes:
        items (list[EntraIdTenantExportToJsonDownloadRequestItem]): Array of Microsoft Entra ID items to export to JSON.
        reason (str | Unset): Reason for the export.
    """

    items: list[EntraIdTenantExportToJsonDownloadRequestItem]
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entra_id_tenant_export_to_json_download_request_item import (
            EntraIdTenantExportToJsonDownloadRequestItem,
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = EntraIdTenantExportToJsonDownloadRequestItem.from_dict(items_item_data)

            items.append(items_item)

        reason = d.pop("reason", UNSET)

        entra_id_tenant_export_to_json_download_request = cls(
            items=items,
            reason=reason,
        )

        entra_id_tenant_export_to_json_download_request.additional_properties = d
        return entra_id_tenant_export_to_json_download_request

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
