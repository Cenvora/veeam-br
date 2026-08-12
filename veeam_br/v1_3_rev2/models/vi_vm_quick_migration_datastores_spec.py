from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vi_vm_quick_migration_datastore_spec import ViVMQuickMigrationDatastoreSpec
    from ..models.vmware_object_model import VmwareObjectModel


T = TypeVar("T", bound="ViVMQuickMigrationDatastoresSpec")


@_attrs_define
class ViVMQuickMigrationDatastoresSpec:
    """Destination datastore.

    Attributes:
        default_datastore (VmwareObjectModel | Unset): VMware vSphere object.
        configuration_file_datastore (VmwareObjectModel | Unset): VMware vSphere object.
        disk_mappings (list[ViVMQuickMigrationDatastoreSpec] | Unset): Array of disks and their locations in the target
            datastore.
    """

    default_datastore: VmwareObjectModel | Unset = UNSET
    configuration_file_datastore: VmwareObjectModel | Unset = UNSET
    disk_mappings: list[ViVMQuickMigrationDatastoreSpec] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_datastore: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_datastore, Unset):
            default_datastore = self.default_datastore.to_dict()

        configuration_file_datastore: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration_file_datastore, Unset):
            configuration_file_datastore = self.configuration_file_datastore.to_dict()

        disk_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.disk_mappings, Unset):
            disk_mappings = []
            for disk_mappings_item_data in self.disk_mappings:
                disk_mappings_item = disk_mappings_item_data.to_dict()
                disk_mappings.append(disk_mappings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_datastore is not UNSET:
            field_dict["defaultDatastore"] = default_datastore
        if configuration_file_datastore is not UNSET:
            field_dict["configurationFileDatastore"] = configuration_file_datastore
        if disk_mappings is not UNSET:
            field_dict["diskMappings"] = disk_mappings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vi_vm_quick_migration_datastore_spec import ViVMQuickMigrationDatastoreSpec
        from ..models.vmware_object_model import VmwareObjectModel

        d = dict(src_dict)
        _default_datastore = d.pop("defaultDatastore", UNSET)
        default_datastore: VmwareObjectModel | Unset
        if isinstance(_default_datastore, Unset):
            default_datastore = UNSET
        else:
            default_datastore = VmwareObjectModel.from_dict(_default_datastore)

        _configuration_file_datastore = d.pop("configurationFileDatastore", UNSET)
        configuration_file_datastore: VmwareObjectModel | Unset
        if isinstance(_configuration_file_datastore, Unset):
            configuration_file_datastore = UNSET
        else:
            configuration_file_datastore = VmwareObjectModel.from_dict(_configuration_file_datastore)

        _disk_mappings = d.pop("diskMappings", UNSET)
        disk_mappings: list[ViVMQuickMigrationDatastoreSpec] | Unset = UNSET
        if _disk_mappings is not UNSET:
            disk_mappings = []
            for disk_mappings_item_data in _disk_mappings:
                disk_mappings_item = ViVMQuickMigrationDatastoreSpec.from_dict(disk_mappings_item_data)

                disk_mappings.append(disk_mappings_item)

        vi_vm_quick_migration_datastores_spec = cls(
            default_datastore=default_datastore,
            configuration_file_datastore=configuration_file_datastore,
            disk_mappings=disk_mappings,
        )

        vi_vm_quick_migration_datastores_spec.additional_properties = d
        return vi_vm_quick_migration_datastores_spec

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
