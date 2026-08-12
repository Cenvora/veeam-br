from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_backup_scope_item_type import EBackupScopeItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupsBackupScopeItemModel")


@_attrs_define
class BackupsBackupScopeItemModel:
    """Backup scope item.

    Attributes:
        backup_id (UUID): Backup ID.
        backup_name (str | Unset): Backup name.
        type_ (EBackupScopeItemType | Unset): Backup type: `Backup` for a regular backup or `Snapshot` for a storage
            snapshot.
    """

    backup_id: UUID
    backup_name: str | Unset = UNSET
    type_: EBackupScopeItemType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_id = str(self.backup_id)

        backup_name = self.backup_name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backupId": backup_id,
            }
        )
        if backup_name is not UNSET:
            field_dict["backupName"] = backup_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_id = UUID(d.pop("backupId"))

        backup_name = d.pop("backupName", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EBackupScopeItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EBackupScopeItemType(_type_)

        backups_backup_scope_item_model = cls(
            backup_id=backup_id,
            backup_name=backup_name,
            type_=type_,
        )

        backups_backup_scope_item_model.additional_properties = d
        return backups_backup_scope_item_model

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
