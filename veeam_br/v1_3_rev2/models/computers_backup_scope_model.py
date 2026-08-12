from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_inventory_scope_workload_type import EInventoryScopeWorkloadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_object_model import AgentObjectModel


T = TypeVar("T", bound="ComputersBackupScopeModel")


@_attrs_define
class ComputersBackupScopeModel:
    """Computer backup scope.

    Attributes:
        type_ (EInventoryScopeWorkloadType): Workload type.
        computers (list[AgentObjectModel] | Unset): Array of computers.
    """

    type_: EInventoryScopeWorkloadType
    computers: list[AgentObjectModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        computers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.computers, Unset):
            computers = []
            for computers_item_data in self.computers:
                computers_item = computers_item_data.to_dict()
                computers.append(computers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if computers is not UNSET:
            field_dict["computers"] = computers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_object_model import AgentObjectModel

        d = dict(src_dict)
        type_ = EInventoryScopeWorkloadType(d.pop("type"))

        _computers = d.pop("computers", UNSET)
        computers: list[AgentObjectModel] | Unset = UNSET
        if _computers is not UNSET:
            computers = []
            for computers_item_data in _computers:
                computers_item = AgentObjectModel.from_dict(computers_item_data)

                computers.append(computers_item)

        computers_backup_scope_model = cls(
            type_=type_,
            computers=computers,
        )

        computers_backup_scope_model.additional_properties = d
        return computers_backup_scope_model

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
