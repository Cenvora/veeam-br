from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instant_hv_vm_other_platform_recovery_datastore_mapping import (
        InstantHvVMOtherPlatformRecoveryDatastoreMapping,
    )


T = TypeVar("T", bound="InstantHvVMOtherPlatformRecoveryDatastoreSpec")


@_attrs_define
class InstantHvVMOtherPlatformRecoveryDatastoreSpec:
    """Datastore that keeps redo logs with changes that take place while a VM is running from a backup. To get a datastore
    object, run the [Get Inventory Objects](Inventory-Browser#operation/GetInventoryObjects) request.

        Attributes:
            configuration_files_path (str | Unset): Absolute path where the configuration files must be placed on the target
                host.
            disk_mappings (list[InstantHvVMOtherPlatformRecoveryDatastoreMapping] | Unset): Array of disks and their
                locations in the target datastore. To get information about disks, run the [Get Inventory Objects](Inventory-
                Browser#operation/GetInventoryObjects) request with the `HostsAndVolumes` filter.
            allocate_required_disk_space (bool | Unset): If `true`, the disk space required for the VM migration is
                preallocated.
    """

    configuration_files_path: str | Unset = UNSET
    disk_mappings: list[InstantHvVMOtherPlatformRecoveryDatastoreMapping] | Unset = UNSET
    allocate_required_disk_space: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration_files_path = self.configuration_files_path

        disk_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.disk_mappings, Unset):
            disk_mappings = []
            for disk_mappings_item_data in self.disk_mappings:
                disk_mappings_item = disk_mappings_item_data.to_dict()
                disk_mappings.append(disk_mappings_item)

        allocate_required_disk_space = self.allocate_required_disk_space

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_files_path is not UNSET:
            field_dict["configurationFilesPath"] = configuration_files_path
        if disk_mappings is not UNSET:
            field_dict["diskMappings"] = disk_mappings
        if allocate_required_disk_space is not UNSET:
            field_dict["allocateRequiredDiskSpace"] = allocate_required_disk_space

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instant_hv_vm_other_platform_recovery_datastore_mapping import (
            InstantHvVMOtherPlatformRecoveryDatastoreMapping,
        )

        d = dict(src_dict)
        configuration_files_path = d.pop("configurationFilesPath", UNSET)

        _disk_mappings = d.pop("diskMappings", UNSET)
        disk_mappings: list[InstantHvVMOtherPlatformRecoveryDatastoreMapping] | Unset = UNSET
        if _disk_mappings is not UNSET:
            disk_mappings = []
            for disk_mappings_item_data in _disk_mappings:
                disk_mappings_item = InstantHvVMOtherPlatformRecoveryDatastoreMapping.from_dict(disk_mappings_item_data)

                disk_mappings.append(disk_mappings_item)

        allocate_required_disk_space = d.pop("allocateRequiredDiskSpace", UNSET)

        instant_hv_vm_other_platform_recovery_datastore_spec = cls(
            configuration_files_path=configuration_files_path,
            disk_mappings=disk_mappings,
            allocate_required_disk_space=allocate_required_disk_space,
        )

        instant_hv_vm_other_platform_recovery_datastore_spec.additional_properties = d
        return instant_hv_vm_other_platform_recovery_datastore_spec

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
