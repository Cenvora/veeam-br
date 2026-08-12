from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_inventory_scope_workload_type import EInventoryScopeWorkloadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vmware_object_model import VmwareObjectModel


T = TypeVar("T", bound="VSphereBackupScopeModel")


@_attrs_define
class VSphereBackupScopeModel:
    """VMware vSphere backup scope.

    Attributes:
        type_ (EInventoryScopeWorkloadType): Workload type.
        inventory_objects (list[VmwareObjectModel] | Unset): Array of VMware vSphere inventory objects.
    """

    type_: EInventoryScopeWorkloadType
    inventory_objects: list[VmwareObjectModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        inventory_objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inventory_objects, Unset):
            inventory_objects = []
            for inventory_objects_item_data in self.inventory_objects:
                inventory_objects_item = inventory_objects_item_data.to_dict()
                inventory_objects.append(inventory_objects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if inventory_objects is not UNSET:
            field_dict["inventoryObjects"] = inventory_objects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vmware_object_model import VmwareObjectModel

        d = dict(src_dict)
        type_ = EInventoryScopeWorkloadType(d.pop("type"))

        _inventory_objects = d.pop("inventoryObjects", UNSET)
        inventory_objects: list[VmwareObjectModel] | Unset = UNSET
        if _inventory_objects is not UNSET:
            inventory_objects = []
            for inventory_objects_item_data in _inventory_objects:
                inventory_objects_item = VmwareObjectModel.from_dict(inventory_objects_item_data)

                inventory_objects.append(inventory_objects_item)

        v_sphere_backup_scope_model = cls(
            type_=type_,
            inventory_objects=inventory_objects,
        )

        v_sphere_backup_scope_model.additional_properties = d
        return v_sphere_backup_scope_model

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
