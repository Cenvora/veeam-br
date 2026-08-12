from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_instant_vi_vm_recovery_bios_uuid_policy_type import EInstantViVmRecoveryBiosUuidPolicyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instant_vi_vm_recovery_helper_appliance_spec import InstantViVMRecoveryHelperApplianceSpec
    from ..models.instant_vi_vm_recovery_network_mapping_spec import InstantViVMRecoveryNetworkMappingSpec
    from ..models.vmware_object_model import VmwareObjectModel


T = TypeVar("T", bound="InstantViVMOtherPlatformRecoveryDestinationSpec")


@_attrs_define
class InstantViVMOtherPlatformRecoveryDestinationSpec:
    """Destination where the recovered VM resides. To get objects of the destination host, folder and resource pool, use
    the [Get Inventory Objects](Inventory-Browser#operation/GetInventoryObjects) request.

        Attributes:
            destination_host (VmwareObjectModel): VMware vSphere object.
            restored_vm_name (str | Unset): Restored VM name.
            folder (VmwareObjectModel | Unset): VMware vSphere object.
            resource_pool (VmwareObjectModel | Unset): VMware vSphere object.
            network_mapping (list[InstantViVMRecoveryNetworkMappingSpec] | Unset): Array of network mapping rules between
                the source and target networks.
            helper_appliance (InstantViVMRecoveryHelperApplianceSpec | Unset): Helper appliance.
            bios_uuid_policy (EInstantViVmRecoveryBiosUuidPolicyType | Unset): BIOS UUID policy for the restored VM.
            enable_cluster_wide_mount (bool | Unset): If `true`, Veeam Backup & Replication mounts the vPowerNFS datastore
                to all ESXi hosts in the cluster specified in `destinationHost`.
    """

    destination_host: VmwareObjectModel
    restored_vm_name: str | Unset = UNSET
    folder: VmwareObjectModel | Unset = UNSET
    resource_pool: VmwareObjectModel | Unset = UNSET
    network_mapping: list[InstantViVMRecoveryNetworkMappingSpec] | Unset = UNSET
    helper_appliance: InstantViVMRecoveryHelperApplianceSpec | Unset = UNSET
    bios_uuid_policy: EInstantViVmRecoveryBiosUuidPolicyType | Unset = UNSET
    enable_cluster_wide_mount: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_host = self.destination_host.to_dict()

        restored_vm_name = self.restored_vm_name

        folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.folder, Unset):
            folder = self.folder.to_dict()

        resource_pool: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_pool, Unset):
            resource_pool = self.resource_pool.to_dict()

        network_mapping: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.network_mapping, Unset):
            network_mapping = []
            for network_mapping_item_data in self.network_mapping:
                network_mapping_item = network_mapping_item_data.to_dict()
                network_mapping.append(network_mapping_item)

        helper_appliance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helper_appliance, Unset):
            helper_appliance = self.helper_appliance.to_dict()

        bios_uuid_policy: str | Unset = UNSET
        if not isinstance(self.bios_uuid_policy, Unset):
            bios_uuid_policy = self.bios_uuid_policy.value

        enable_cluster_wide_mount = self.enable_cluster_wide_mount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destinationHost": destination_host,
            }
        )
        if restored_vm_name is not UNSET:
            field_dict["restoredVmName"] = restored_vm_name
        if folder is not UNSET:
            field_dict["folder"] = folder
        if resource_pool is not UNSET:
            field_dict["resourcePool"] = resource_pool
        if network_mapping is not UNSET:
            field_dict["networkMapping"] = network_mapping
        if helper_appliance is not UNSET:
            field_dict["helperAppliance"] = helper_appliance
        if bios_uuid_policy is not UNSET:
            field_dict["biosUuidPolicy"] = bios_uuid_policy
        if enable_cluster_wide_mount is not UNSET:
            field_dict["enableClusterWideMount"] = enable_cluster_wide_mount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instant_vi_vm_recovery_helper_appliance_spec import InstantViVMRecoveryHelperApplianceSpec
        from ..models.instant_vi_vm_recovery_network_mapping_spec import InstantViVMRecoveryNetworkMappingSpec
        from ..models.vmware_object_model import VmwareObjectModel

        d = dict(src_dict)
        destination_host = VmwareObjectModel.from_dict(d.pop("destinationHost"))

        restored_vm_name = d.pop("restoredVmName", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: VmwareObjectModel | Unset
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = VmwareObjectModel.from_dict(_folder)

        _resource_pool = d.pop("resourcePool", UNSET)
        resource_pool: VmwareObjectModel | Unset
        if isinstance(_resource_pool, Unset):
            resource_pool = UNSET
        else:
            resource_pool = VmwareObjectModel.from_dict(_resource_pool)

        _network_mapping = d.pop("networkMapping", UNSET)
        network_mapping: list[InstantViVMRecoveryNetworkMappingSpec] | Unset = UNSET
        if _network_mapping is not UNSET:
            network_mapping = []
            for network_mapping_item_data in _network_mapping:
                network_mapping_item = InstantViVMRecoveryNetworkMappingSpec.from_dict(network_mapping_item_data)

                network_mapping.append(network_mapping_item)

        _helper_appliance = d.pop("helperAppliance", UNSET)
        helper_appliance: InstantViVMRecoveryHelperApplianceSpec | Unset
        if isinstance(_helper_appliance, Unset):
            helper_appliance = UNSET
        else:
            helper_appliance = InstantViVMRecoveryHelperApplianceSpec.from_dict(_helper_appliance)

        _bios_uuid_policy = d.pop("biosUuidPolicy", UNSET)
        bios_uuid_policy: EInstantViVmRecoveryBiosUuidPolicyType | Unset
        if isinstance(_bios_uuid_policy, Unset):
            bios_uuid_policy = UNSET
        else:
            bios_uuid_policy = EInstantViVmRecoveryBiosUuidPolicyType(_bios_uuid_policy)

        enable_cluster_wide_mount = d.pop("enableClusterWideMount", UNSET)

        instant_vi_vm_other_platform_recovery_destination_spec = cls(
            destination_host=destination_host,
            restored_vm_name=restored_vm_name,
            folder=folder,
            resource_pool=resource_pool,
            network_mapping=network_mapping,
            helper_appliance=helper_appliance,
            bios_uuid_policy=bios_uuid_policy,
            enable_cluster_wide_mount=enable_cluster_wide_mount,
        )

        instant_vi_vm_other_platform_recovery_destination_spec.additional_properties = d
        return instant_vi_vm_other_platform_recovery_destination_spec

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
