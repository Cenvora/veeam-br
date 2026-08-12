from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_instant_vm_recovery_mode_type import EInstantVMRecoveryModeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hv_restore_target_name_spec import HvRestoreTargetNameSpec
    from ..models.hv_restore_target_network_spec import HvRestoreTargetNetworkSpec
    from ..models.hyper_v_object_model import HyperVObjectModel
    from ..models.instant_hv_vm_other_platform_recovery_datastore_spec import (
        InstantHvVMOtherPlatformRecoveryDatastoreSpec,
    )
    from ..models.instant_hv_vm_recovery_helper_appliance_spec import InstantHvVMRecoveryHelperApplianceSpec
    from ..models.secure_restore_spec import SecureRestoreSpec


T = TypeVar("T", bound="InstantHvVMOtherPlatformRecoverySpec")


@_attrs_define
class InstantHvVMOtherPlatformRecoverySpec:
    """Instant Recovery to a new location or with different settings.

    Attributes:
        restore_point_id (UUID): ID of the restore point.
        type_ (EInstantVMRecoveryModeType): Instant Recovery restore mode.

            | Enum Value               | Description
            |
            |--------------------------|------------------------------------------------------------------------------------
            -------------------------------------------------------------------------------------|
            | OriginalLocation         | Veeam Backup & Replication will perform Instant Recovery to the original location.
            |
            | Customized               | Veeam Backup & Replication will perform Instant Recovery to a new location or to
            the original location with new settings.<br><br>Note: If you do not specify an optional property that defines
            target settings (such as VM name, destination host, resource pool, folder and so on), Veeam Backup & Replication
            will try to use the source settings for that property. |
        destination_host (HyperVObjectModel): Microsoft Hyper-V object.
        secure_restore (SecureRestoreSpec | Unset): Secure restore settings.
        power_up (bool | Unset): If `true`, Veeam Backup & Replication powers on the restored VM on the target host.
        reason (str | Unset): Reason for restoring the VM.
        share_credentials_id (UUID | Unset): Credentials to network share the restorePoint is located on. If needed.
        datastore (InstantHvVMOtherPlatformRecoveryDatastoreSpec | Unset): Datastore that keeps redo logs with changes
            that take place while a VM is running from a backup. To get a datastore object, run the [Get Inventory
            Objects](Inventory-Browser#operation/GetInventoryObjects) request.
        network (HvRestoreTargetNetworkSpec | Unset): Network to which the restored VM will be connected. To get
            information about source and target network objects, run the [Get Inventory Objects](Inventory-
            Browser#operation/GetInventoryObjects) request with the `Network` filter.
        target (HvRestoreTargetNameSpec | Unset): Destination VM folder.
        helper_appliance (InstantHvVMRecoveryHelperApplianceSpec | Unset): Helper appliance.
    """

    restore_point_id: UUID
    type_: EInstantVMRecoveryModeType
    destination_host: HyperVObjectModel
    secure_restore: SecureRestoreSpec | Unset = UNSET
    power_up: bool | Unset = UNSET
    reason: str | Unset = UNSET
    share_credentials_id: UUID | Unset = UNSET
    datastore: InstantHvVMOtherPlatformRecoveryDatastoreSpec | Unset = UNSET
    network: HvRestoreTargetNetworkSpec | Unset = UNSET
    target: HvRestoreTargetNameSpec | Unset = UNSET
    helper_appliance: InstantHvVMRecoveryHelperApplianceSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_point_id = str(self.restore_point_id)

        type_ = self.type_.value

        destination_host = self.destination_host.to_dict()

        secure_restore: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secure_restore, Unset):
            secure_restore = self.secure_restore.to_dict()

        power_up = self.power_up

        reason = self.reason

        share_credentials_id: str | Unset = UNSET
        if not isinstance(self.share_credentials_id, Unset):
            share_credentials_id = str(self.share_credentials_id)

        datastore: dict[str, Any] | Unset = UNSET
        if not isinstance(self.datastore, Unset):
            datastore = self.datastore.to_dict()

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        helper_appliance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helper_appliance, Unset):
            helper_appliance = self.helper_appliance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restorePointId": restore_point_id,
                "type": type_,
                "destinationHost": destination_host,
            }
        )
        if secure_restore is not UNSET:
            field_dict["secureRestore"] = secure_restore
        if power_up is not UNSET:
            field_dict["powerUp"] = power_up
        if reason is not UNSET:
            field_dict["reason"] = reason
        if share_credentials_id is not UNSET:
            field_dict["shareCredentialsId"] = share_credentials_id
        if datastore is not UNSET:
            field_dict["datastore"] = datastore
        if network is not UNSET:
            field_dict["network"] = network
        if target is not UNSET:
            field_dict["target"] = target
        if helper_appliance is not UNSET:
            field_dict["helperAppliance"] = helper_appliance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hv_restore_target_name_spec import HvRestoreTargetNameSpec
        from ..models.hv_restore_target_network_spec import HvRestoreTargetNetworkSpec
        from ..models.hyper_v_object_model import HyperVObjectModel
        from ..models.instant_hv_vm_other_platform_recovery_datastore_spec import (
            InstantHvVMOtherPlatformRecoveryDatastoreSpec,
        )
        from ..models.instant_hv_vm_recovery_helper_appliance_spec import InstantHvVMRecoveryHelperApplianceSpec
        from ..models.secure_restore_spec import SecureRestoreSpec

        d = dict(src_dict)
        restore_point_id = UUID(d.pop("restorePointId"))

        type_ = EInstantVMRecoveryModeType(d.pop("type"))

        destination_host = HyperVObjectModel.from_dict(d.pop("destinationHost"))

        _secure_restore = d.pop("secureRestore", UNSET)
        secure_restore: SecureRestoreSpec | Unset
        if isinstance(_secure_restore, Unset):
            secure_restore = UNSET
        else:
            secure_restore = SecureRestoreSpec.from_dict(_secure_restore)

        power_up = d.pop("powerUp", UNSET)

        reason = d.pop("reason", UNSET)

        _share_credentials_id = d.pop("shareCredentialsId", UNSET)
        share_credentials_id: UUID | Unset
        if isinstance(_share_credentials_id, Unset):
            share_credentials_id = UNSET
        else:
            share_credentials_id = UUID(_share_credentials_id)

        _datastore = d.pop("datastore", UNSET)
        datastore: InstantHvVMOtherPlatformRecoveryDatastoreSpec | Unset
        if isinstance(_datastore, Unset):
            datastore = UNSET
        else:
            datastore = InstantHvVMOtherPlatformRecoveryDatastoreSpec.from_dict(_datastore)

        _network = d.pop("network", UNSET)
        network: HvRestoreTargetNetworkSpec | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = HvRestoreTargetNetworkSpec.from_dict(_network)

        _target = d.pop("target", UNSET)
        target: HvRestoreTargetNameSpec | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = HvRestoreTargetNameSpec.from_dict(_target)

        _helper_appliance = d.pop("helperAppliance", UNSET)
        helper_appliance: InstantHvVMRecoveryHelperApplianceSpec | Unset
        if isinstance(_helper_appliance, Unset):
            helper_appliance = UNSET
        else:
            helper_appliance = InstantHvVMRecoveryHelperApplianceSpec.from_dict(_helper_appliance)

        instant_hv_vm_other_platform_recovery_spec = cls(
            restore_point_id=restore_point_id,
            type_=type_,
            destination_host=destination_host,
            secure_restore=secure_restore,
            power_up=power_up,
            reason=reason,
            share_credentials_id=share_credentials_id,
            datastore=datastore,
            network=network,
            target=target,
            helper_appliance=helper_appliance,
        )

        instant_hv_vm_other_platform_recovery_spec.additional_properties = d
        return instant_hv_vm_other_platform_recovery_spec

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
