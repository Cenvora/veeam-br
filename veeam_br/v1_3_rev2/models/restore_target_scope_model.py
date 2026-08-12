from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.restore_target_inventory_scope_model import RestoreTargetInventoryScopeModel


T = TypeVar("T", bound="RestoreTargetScopeModel")


@_attrs_define
class RestoreTargetScopeModel:
    """Restore target scope.

    Attributes:
        entire_backup_scope (bool): If `true`, restores can target any location in the infrastructure. If `false`,
            restores are restricted to the targets listed in the `restoreTargets` property.
        restore_targets (RestoreTargetInventoryScopeModel | Unset): Restore target scope for inventory.
    """

    entire_backup_scope: bool
    restore_targets: RestoreTargetInventoryScopeModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entire_backup_scope = self.entire_backup_scope

        restore_targets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restore_targets, Unset):
            restore_targets = self.restore_targets.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entireBackupScope": entire_backup_scope,
            }
        )
        if restore_targets is not UNSET:
            field_dict["restoreTargets"] = restore_targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.restore_target_inventory_scope_model import RestoreTargetInventoryScopeModel

        d = dict(src_dict)
        entire_backup_scope = d.pop("entireBackupScope")

        _restore_targets = d.pop("restoreTargets", UNSET)
        restore_targets: RestoreTargetInventoryScopeModel | Unset
        if isinstance(_restore_targets, Unset):
            restore_targets = UNSET
        else:
            restore_targets = RestoreTargetInventoryScopeModel.from_dict(_restore_targets)

        restore_target_scope_model = cls(
            entire_backup_scope=entire_backup_scope,
            restore_targets=restore_targets,
        )

        restore_target_scope_model.additional_properties = d
        return restore_target_scope_model

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
