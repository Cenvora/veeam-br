from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveBackupObjectsSpec")


@_attrs_define
class MoveBackupObjectsSpec:
    """Spec for moving backup objects to another job.

    Attributes:
        target_job_id (UUID): ID of the target job to move the backup objects to.
        backup_objects (list[UUID] | Unset): Array of backup object IDs to move. If not specified, all objects in the
            backup are moved. To get the IDs, run the [Get Backup Objects](Backups#operation/GetBackupObjectsWithFiltering)
            request.
    """

    target_job_id: UUID
    backup_objects: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_job_id = str(self.target_job_id)

        backup_objects: list[str] | Unset = UNSET
        if not isinstance(self.backup_objects, Unset):
            backup_objects = []
            for backup_objects_item_data in self.backup_objects:
                backup_objects_item = str(backup_objects_item_data)
                backup_objects.append(backup_objects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetJobId": target_job_id,
            }
        )
        if backup_objects is not UNSET:
            field_dict["backupObjects"] = backup_objects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_job_id = UUID(d.pop("targetJobId"))

        _backup_objects = d.pop("backupObjects", UNSET)
        backup_objects: list[UUID] | Unset = UNSET
        if _backup_objects is not UNSET:
            backup_objects = []
            for backup_objects_item_data in _backup_objects:
                backup_objects_item = UUID(backup_objects_item_data)

                backup_objects.append(backup_objects_item)

        move_backup_objects_spec = cls(
            target_job_id=target_job_id,
            backup_objects=backup_objects,
        )

        move_backup_objects_spec.additional_properties = d
        return move_backup_objects_spec

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
