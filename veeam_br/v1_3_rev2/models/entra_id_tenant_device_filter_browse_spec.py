from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntraIdTenantDeviceFilterBrowseSpec")


@_attrs_define
class EntraIdTenantDeviceFilterBrowseSpec:
    """Filtering options.

    Attributes:
        display_name (str | Unset): Device display name.
        operating_system (str | Unset): Operating system name.
        operating_system_version (str | Unset): Operating system version.
        device_version (str | Unset): Device version.
        account_enabled (bool | Unset): If `true`, the device is enabled.
    """

    display_name: str | Unset = UNSET
    operating_system: str | Unset = UNSET
    operating_system_version: str | Unset = UNSET
    device_version: str | Unset = UNSET
    account_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        operating_system = self.operating_system

        operating_system_version = self.operating_system_version

        device_version = self.device_version

        account_enabled = self.account_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if operating_system is not UNSET:
            field_dict["operatingSystem"] = operating_system
        if operating_system_version is not UNSET:
            field_dict["operatingSystemVersion"] = operating_system_version
        if device_version is not UNSET:
            field_dict["deviceVersion"] = device_version
        if account_enabled is not UNSET:
            field_dict["accountEnabled"] = account_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        operating_system = d.pop("operatingSystem", UNSET)

        operating_system_version = d.pop("operatingSystemVersion", UNSET)

        device_version = d.pop("deviceVersion", UNSET)

        account_enabled = d.pop("accountEnabled", UNSET)

        entra_id_tenant_device_filter_browse_spec = cls(
            display_name=display_name,
            operating_system=operating_system,
            operating_system_version=operating_system_version,
            device_version=device_version,
            account_enabled=account_enabled,
        )

        entra_id_tenant_device_filter_browse_spec.additional_properties = d
        return entra_id_tenant_device_filter_browse_spec

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
