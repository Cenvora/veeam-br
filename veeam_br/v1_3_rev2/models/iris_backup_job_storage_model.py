from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_job_retention_policy_settings_model import BackupJobRetentionPolicySettingsModel
    from ..models.snapshot_immutability_options_model import SnapshotImmutabilityOptionsModel


T = TypeVar("T", bound="IrisBackupJobStorageModel")


@_attrs_define
class IrisBackupJobStorageModel:
    """InterSystems IRIS backup storage settings.

    Attributes:
        backup_repository_id (UUID | Unset): Backup repository ID.
        source_backup_id (UUID | Unset): ID of a backup stored in the backup repository. Use this property to map the
            job to an existing backup.
        retention_policy (BackupJobRetentionPolicySettingsModel | Unset): Retention policy settings.
        snapshot_immutability_options (SnapshotImmutabilityOptionsModel | Unset): Snapshot immutability options.
    """

    backup_repository_id: UUID | Unset = UNSET
    source_backup_id: UUID | Unset = UNSET
    retention_policy: BackupJobRetentionPolicySettingsModel | Unset = UNSET
    snapshot_immutability_options: SnapshotImmutabilityOptionsModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_repository_id: str | Unset = UNSET
        if not isinstance(self.backup_repository_id, Unset):
            backup_repository_id = str(self.backup_repository_id)

        source_backup_id: str | Unset = UNSET
        if not isinstance(self.source_backup_id, Unset):
            source_backup_id = str(self.source_backup_id)

        retention_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention_policy, Unset):
            retention_policy = self.retention_policy.to_dict()

        snapshot_immutability_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot_immutability_options, Unset):
            snapshot_immutability_options = self.snapshot_immutability_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_repository_id is not UNSET:
            field_dict["backupRepositoryId"] = backup_repository_id
        if source_backup_id is not UNSET:
            field_dict["sourceBackupId"] = source_backup_id
        if retention_policy is not UNSET:
            field_dict["retentionPolicy"] = retention_policy
        if snapshot_immutability_options is not UNSET:
            field_dict["snapshotImmutabilityOptions"] = snapshot_immutability_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_job_retention_policy_settings_model import BackupJobRetentionPolicySettingsModel
        from ..models.snapshot_immutability_options_model import SnapshotImmutabilityOptionsModel

        d = dict(src_dict)
        _backup_repository_id = d.pop("backupRepositoryId", UNSET)
        backup_repository_id: UUID | Unset
        if isinstance(_backup_repository_id, Unset):
            backup_repository_id = UNSET
        else:
            backup_repository_id = UUID(_backup_repository_id)

        _source_backup_id = d.pop("sourceBackupId", UNSET)
        source_backup_id: UUID | Unset
        if isinstance(_source_backup_id, Unset):
            source_backup_id = UNSET
        else:
            source_backup_id = UUID(_source_backup_id)

        _retention_policy = d.pop("retentionPolicy", UNSET)
        retention_policy: BackupJobRetentionPolicySettingsModel | Unset
        if isinstance(_retention_policy, Unset):
            retention_policy = UNSET
        else:
            retention_policy = BackupJobRetentionPolicySettingsModel.from_dict(_retention_policy)

        _snapshot_immutability_options = d.pop("snapshotImmutabilityOptions", UNSET)
        snapshot_immutability_options: SnapshotImmutabilityOptionsModel | Unset
        if isinstance(_snapshot_immutability_options, Unset):
            snapshot_immutability_options = UNSET
        else:
            snapshot_immutability_options = SnapshotImmutabilityOptionsModel.from_dict(_snapshot_immutability_options)

        iris_backup_job_storage_model = cls(
            backup_repository_id=backup_repository_id,
            source_backup_id=source_backup_id,
            retention_policy=retention_policy,
            snapshot_immutability_options=snapshot_immutability_options,
        )

        iris_backup_job_storage_model.additional_properties = d
        return iris_backup_job_storage_model

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
