from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scopes_workload_model import ScopesWorkloadModel


T = TypeVar("T", bound="RestoreScopeBackupModel")


@_attrs_define
class RestoreScopeBackupModel:
    """Backup restore scope.

    Attributes:
        entire_backup_scope (bool): If `true`, the role can restore from all available backups regardless of ownership.
            If `false`, the role can only restore from backups created by users assigned to this role plus the additional
            backup sources listed in the `backupSources` property.
        backup_sources (list[ScopesWorkloadModel] | Unset): Array of additional backup sources from which the role can
            restore.
    """

    entire_backup_scope: bool
    backup_sources: list[ScopesWorkloadModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entire_backup_scope = self.entire_backup_scope

        backup_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.backup_sources, Unset):
            backup_sources = []
            for backup_sources_item_data in self.backup_sources:
                backup_sources_item = backup_sources_item_data.to_dict()
                backup_sources.append(backup_sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entireBackupScope": entire_backup_scope,
            }
        )
        if backup_sources is not UNSET:
            field_dict["backupSources"] = backup_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scopes_workload_model import ScopesWorkloadModel

        d = dict(src_dict)
        entire_backup_scope = d.pop("entireBackupScope")

        _backup_sources = d.pop("backupSources", UNSET)
        backup_sources: list[ScopesWorkloadModel] | Unset = UNSET
        if _backup_sources is not UNSET:
            backup_sources = []
            for backup_sources_item_data in _backup_sources:
                backup_sources_item = ScopesWorkloadModel.from_dict(backup_sources_item_data)

                backup_sources.append(backup_sources_item)

        restore_scope_backup_model = cls(
            entire_backup_scope=entire_backup_scope,
            backup_sources=backup_sources,
        )

        restore_scope_backup_model.additional_properties = d
        return restore_scope_backup_model

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
