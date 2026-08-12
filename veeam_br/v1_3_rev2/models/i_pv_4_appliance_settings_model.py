from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_pv_4_settings_model import IPv4SettingsModel


T = TypeVar("T", bound="IPv4ApplianceSettingsModel")


@_attrs_define
class IPv4ApplianceSettingsModel:
    """IPv4 address settings.

    Attributes:
        obtain_ip_automatically (bool | Unset): If `true`, the IPv4 address is obtained automatically.
        obtain_dns_automatically (bool | Unset): If `true`, the DNS server address is obtained automatically.
        ip_address (IPv4SettingsModel | Unset): IPv4 settings.
    """

    obtain_ip_automatically: bool | Unset = UNSET
    obtain_dns_automatically: bool | Unset = UNSET
    ip_address: IPv4SettingsModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        obtain_ip_automatically = self.obtain_ip_automatically

        obtain_dns_automatically = self.obtain_dns_automatically

        ip_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_address, Unset):
            ip_address = self.ip_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obtain_ip_automatically is not UNSET:
            field_dict["obtainIPAutomatically"] = obtain_ip_automatically
        if obtain_dns_automatically is not UNSET:
            field_dict["obtainDNSAutomatically"] = obtain_dns_automatically
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.i_pv_4_settings_model import IPv4SettingsModel

        d = dict(src_dict)
        obtain_ip_automatically = d.pop("obtainIPAutomatically", UNSET)

        obtain_dns_automatically = d.pop("obtainDNSAutomatically", UNSET)

        _ip_address = d.pop("ipAddress", UNSET)
        ip_address: IPv4SettingsModel | Unset
        if isinstance(_ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = IPv4SettingsModel.from_dict(_ip_address)

        i_pv_4_appliance_settings_model = cls(
            obtain_ip_automatically=obtain_ip_automatically,
            obtain_dns_automatically=obtain_dns_automatically,
            ip_address=ip_address,
        )

        i_pv_4_appliance_settings_model.additional_properties = d
        return i_pv_4_appliance_settings_model

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
