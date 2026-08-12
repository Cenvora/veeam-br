from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_inventory_platform_type import EInventoryPlatformType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vi_vm_disk_model import ViVMDiskModel


T = TypeVar("T", bound="VmwareMachineDetailsModel")


@_attrs_define
class VmwareMachineDetailsModel:
    """VMware vSphere inventory machine details.

    Attributes:
        platform (EInventoryPlatformType): Platform type of inventory object.
        disks (list[ViVMDiskModel] | Unset): Array of disks of the VMware vSphere machine.
    """

    platform: EInventoryPlatformType
    disks: list[ViVMDiskModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        disks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.disks, Unset):
            disks = []
            for disks_item_data in self.disks:
                disks_item = disks_item_data.to_dict()
                disks.append(disks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
            }
        )
        if disks is not UNSET:
            field_dict["disks"] = disks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vi_vm_disk_model import ViVMDiskModel

        d = dict(src_dict)
        platform = EInventoryPlatformType(d.pop("platform"))

        _disks = d.pop("disks", UNSET)
        disks: list[ViVMDiskModel] | Unset = UNSET
        if _disks is not UNSET:
            disks = []
            for disks_item_data in _disks:
                disks_item = ViVMDiskModel.from_dict(disks_item_data)

                disks.append(disks_item)

        vmware_machine_details_model = cls(
            platform=platform,
            disks=disks,
        )

        vmware_machine_details_model.additional_properties = d
        return vmware_machine_details_model

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
