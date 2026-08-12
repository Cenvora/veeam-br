from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StartEntraIdTenantExportToJsonResponse")


@_attrs_define
class StartEntraIdTenantExportToJsonResponse:
    """Result of starting a Microsoft Entra ID export-to-JSON operation.

    Attributes:
        export_session_id (UUID): Export session ID.
    """

    export_session_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        export_session_id = str(self.export_session_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exportSessionId": export_session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        export_session_id = UUID(d.pop("exportSessionId"))

        start_entra_id_tenant_export_to_json_response = cls(
            export_session_id=export_session_id,
        )

        start_entra_id_tenant_export_to_json_response.additional_properties = d
        return start_entra_id_tenant_export_to_json_response

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
