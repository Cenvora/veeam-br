from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayServerSettingsModel")


@_attrs_define
class GatewayServerSettingsModel:
    """Gateway server settings.

    Attributes:
        auto_selection (bool | Unset): If `true`, Veeam Backup & Replication selects gateway servers automatically.
            Default: True.
        gateway_server_ids (list[UUID] | Unset): Array of gateway server IDs.
    """

    auto_selection: bool | Unset = True
    gateway_server_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_selection = self.auto_selection

        gateway_server_ids: list[str] | Unset = UNSET
        if not isinstance(self.gateway_server_ids, Unset):
            gateway_server_ids = []
            for gateway_server_ids_item_data in self.gateway_server_ids:
                gateway_server_ids_item = str(gateway_server_ids_item_data)
                gateway_server_ids.append(gateway_server_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_selection is not UNSET:
            field_dict["autoSelection"] = auto_selection
        if gateway_server_ids is not UNSET:
            field_dict["gatewayServerIds"] = gateway_server_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_selection = d.pop("autoSelection", UNSET)

        _gateway_server_ids = d.pop("gatewayServerIds", UNSET)
        gateway_server_ids: list[UUID] | Unset = UNSET
        if _gateway_server_ids is not UNSET:
            gateway_server_ids = []
            for gateway_server_ids_item_data in _gateway_server_ids:
                gateway_server_ids_item = UUID(gateway_server_ids_item_data)

                gateway_server_ids.append(gateway_server_ids_item)

        gateway_server_settings_model = cls(
            auto_selection=auto_selection,
            gateway_server_ids=gateway_server_ids,
        )

        gateway_server_settings_model.additional_properties = d
        return gateway_server_settings_model

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
