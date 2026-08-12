from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_entra_id_tenant_export_to_json_result_response_status import (
    GetEntraIdTenantExportToJsonResultResponseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetEntraIdTenantExportToJsonResultResponse")


@_attrs_define
class GetEntraIdTenantExportToJsonResultResponse:
    """Status and result of a Microsoft Entra ID export-to-JSON operation.

    Attributes:
        status (GetEntraIdTenantExportToJsonResultResponseStatus): Session status.
        sas_link (str | Unset): SAS URI to download the exported items.
        error_message (str | Unset): Error message.
    """

    status: GetEntraIdTenantExportToJsonResultResponseStatus
    sas_link: str | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        sas_link = self.sas_link

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if sas_link is not UNSET:
            field_dict["sasLink"] = sas_link
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = GetEntraIdTenantExportToJsonResultResponseStatus(d.pop("status"))

        sas_link = d.pop("sasLink", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        get_entra_id_tenant_export_to_json_result_response = cls(
            status=status,
            sas_link=sas_link,
            error_message=error_message,
        )

        get_entra_id_tenant_export_to_json_result_response.additional_properties = d
        return get_entra_id_tenant_export_to_json_result_response

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
