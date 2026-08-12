from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scopes_workload_model import ScopesWorkloadModel


T = TypeVar("T", bound="RestoreTargetInventoryScopeModel")


@_attrs_define
class RestoreTargetInventoryScopeModel:
    """Restore target scope for inventory.

    Attributes:
        original_location (bool | Unset): If `true`, restores are restricted to the original location of each backed-up
            workload. If `false`, restores can target any of the workloads listed in the `workloads` property.
        workloads (list[ScopesWorkloadModel] | Unset): Workloads where the role can perform restores. Required if
            `originalLocation` is `false`.
    """

    original_location: bool | Unset = UNSET
    workloads: list[ScopesWorkloadModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        original_location = self.original_location

        workloads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workloads, Unset):
            workloads = []
            for workloads_item_data in self.workloads:
                workloads_item = workloads_item_data.to_dict()
                workloads.append(workloads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original_location is not UNSET:
            field_dict["originalLocation"] = original_location
        if workloads is not UNSET:
            field_dict["workloads"] = workloads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scopes_workload_model import ScopesWorkloadModel

        d = dict(src_dict)
        original_location = d.pop("originalLocation", UNSET)

        _workloads = d.pop("workloads", UNSET)
        workloads: list[ScopesWorkloadModel] | Unset = UNSET
        if _workloads is not UNSET:
            workloads = []
            for workloads_item_data in _workloads:
                workloads_item = ScopesWorkloadModel.from_dict(workloads_item_data)

                workloads.append(workloads_item)

        restore_target_inventory_scope_model = cls(
            original_location=original_location,
            workloads=workloads,
        )

        restore_target_inventory_scope_model.additional_properties = d
        return restore_target_inventory_scope_model

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
