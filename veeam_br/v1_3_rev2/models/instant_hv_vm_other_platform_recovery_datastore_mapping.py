from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.object_restore_point_disk_model import ObjectRestorePointDiskModel


T = TypeVar("T", bound="InstantHvVMOtherPlatformRecoveryDatastoreMapping")


@_attrs_define
class InstantHvVMOtherPlatformRecoveryDatastoreMapping:
    """Destination datastore.

    Attributes:
        disk (ObjectRestorePointDiskModel): Backup object disk.
        target_folder (str): Path to the target folder where the restored disk files are stored.
    """

    disk: ObjectRestorePointDiskModel
    target_folder: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disk = self.disk.to_dict()

        target_folder = self.target_folder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disk": disk,
                "targetFolder": target_folder,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_restore_point_disk_model import ObjectRestorePointDiskModel

        d = dict(src_dict)
        disk = ObjectRestorePointDiskModel.from_dict(d.pop("disk"))

        target_folder = d.pop("targetFolder")

        instant_hv_vm_other_platform_recovery_datastore_mapping = cls(
            disk=disk,
            target_folder=target_folder,
        )

        instant_hv_vm_other_platform_recovery_datastore_mapping.additional_properties = d
        return instant_hv_vm_other_platform_recovery_datastore_mapping

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
