from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_disk_creation_mode import EDiskCreationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vi_vm_disk_model import ViVMDiskModel
    from ..models.vmware_object_model import VmwareObjectModel


T = TypeVar("T", bound="ViVMQuickMigrationDatastoreSpec")


@_attrs_define
class ViVMQuickMigrationDatastoreSpec:
    """Destination datastore.

    Attributes:
        disk (ViVMDiskModel): VMware vSphere virtual machine disk.
        datastore (VmwareObjectModel): VMware vSphere object.
        disk_type (EDiskCreationMode | Unset): Disk provisioning type for the recovered VM.
    """

    disk: ViVMDiskModel
    datastore: VmwareObjectModel
    disk_type: EDiskCreationMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disk = self.disk.to_dict()

        datastore = self.datastore.to_dict()

        disk_type: str | Unset = UNSET
        if not isinstance(self.disk_type, Unset):
            disk_type = self.disk_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disk": disk,
                "datastore": datastore,
            }
        )
        if disk_type is not UNSET:
            field_dict["diskType"] = disk_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vi_vm_disk_model import ViVMDiskModel
        from ..models.vmware_object_model import VmwareObjectModel

        d = dict(src_dict)
        disk = ViVMDiskModel.from_dict(d.pop("disk"))

        datastore = VmwareObjectModel.from_dict(d.pop("datastore"))

        _disk_type = d.pop("diskType", UNSET)
        disk_type: EDiskCreationMode | Unset
        if isinstance(_disk_type, Unset):
            disk_type = UNSET
        else:
            disk_type = EDiskCreationMode(_disk_type)

        vi_vm_quick_migration_datastore_spec = cls(
            disk=disk,
            datastore=datastore,
            disk_type=disk_type,
        )

        vi_vm_quick_migration_datastore_spec.additional_properties = d
        return vi_vm_quick_migration_datastore_spec

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
