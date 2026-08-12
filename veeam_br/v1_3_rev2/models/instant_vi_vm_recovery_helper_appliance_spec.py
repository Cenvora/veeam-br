from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_pv_4_appliance_settings_model import IPv4ApplianceSettingsModel
    from ..models.i_pv_6_appliance_settings_model import IPv6ApplianceSettingsModel
    from ..models.vmware_object_model import VmwareObjectModel


T = TypeVar("T", bound="InstantViVMRecoveryHelperApplianceSpec")


@_attrs_define
class InstantViVMRecoveryHelperApplianceSpec:
    """Helper appliance.

    Attributes:
        production_network (VmwareObjectModel): VMware vSphere object.
        ipv_4_address (IPv4ApplianceSettingsModel | Unset): IPv4 address settings.
        ipv_6_address (IPv6ApplianceSettingsModel | Unset): IPv6 address settings.
    """

    production_network: VmwareObjectModel
    ipv_4_address: IPv4ApplianceSettingsModel | Unset = UNSET
    ipv_6_address: IPv6ApplianceSettingsModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        production_network = self.production_network.to_dict()

        ipv_4_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_address, Unset):
            ipv_4_address = self.ipv_4_address.to_dict()

        ipv_6_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_6_address, Unset):
            ipv_6_address = self.ipv_6_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productionNetwork": production_network,
            }
        )
        if ipv_4_address is not UNSET:
            field_dict["ipv4Address"] = ipv_4_address
        if ipv_6_address is not UNSET:
            field_dict["ipv6Address"] = ipv_6_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.i_pv_4_appliance_settings_model import IPv4ApplianceSettingsModel
        from ..models.i_pv_6_appliance_settings_model import IPv6ApplianceSettingsModel
        from ..models.vmware_object_model import VmwareObjectModel

        d = dict(src_dict)
        production_network = VmwareObjectModel.from_dict(d.pop("productionNetwork"))

        _ipv_4_address = d.pop("ipv4Address", UNSET)
        ipv_4_address: IPv4ApplianceSettingsModel | Unset
        if isinstance(_ipv_4_address, Unset):
            ipv_4_address = UNSET
        else:
            ipv_4_address = IPv4ApplianceSettingsModel.from_dict(_ipv_4_address)

        _ipv_6_address = d.pop("ipv6Address", UNSET)
        ipv_6_address: IPv6ApplianceSettingsModel | Unset
        if isinstance(_ipv_6_address, Unset):
            ipv_6_address = UNSET
        else:
            ipv_6_address = IPv6ApplianceSettingsModel.from_dict(_ipv_6_address)

        instant_vi_vm_recovery_helper_appliance_spec = cls(
            production_network=production_network,
            ipv_4_address=ipv_4_address,
            ipv_6_address=ipv_6_address,
        )

        instant_vi_vm_recovery_helper_appliance_spec.additional_properties = d
        return instant_vi_vm_recovery_helper_appliance_spec

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
