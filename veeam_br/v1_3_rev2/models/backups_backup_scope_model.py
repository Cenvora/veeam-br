from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_inventory_scope_workload_type import EInventoryScopeWorkloadType

if TYPE_CHECKING:
    from ..models.backups_backup_scope_item_model import BackupsBackupScopeItemModel


T = TypeVar("T", bound="BackupsBackupScopeModel")


@_attrs_define
class BackupsBackupScopeModel:
    """Backup scope.

    Attributes:
        type_ (EInventoryScopeWorkloadType): Workload type.
        backups (list[BackupsBackupScopeItemModel]): Array of backups.
    """

    type_: EInventoryScopeWorkloadType
    backups: list[BackupsBackupScopeItemModel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        backups = []
        for backups_item_data in self.backups:
            backups_item = backups_item_data.to_dict()
            backups.append(backups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "backups": backups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backups_backup_scope_item_model import BackupsBackupScopeItemModel

        d = dict(src_dict)
        type_ = EInventoryScopeWorkloadType(d.pop("type"))

        backups = []
        _backups = d.pop("backups")
        for backups_item_data in _backups:
            backups_item = BackupsBackupScopeItemModel.from_dict(backups_item_data)

            backups.append(backups_item)

        backups_backup_scope_model = cls(
            type_=type_,
            backups=backups,
        )

        backups_backup_scope_model.additional_properties = d
        return backups_backup_scope_model

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
