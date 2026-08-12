from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_job_type import EJobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_storage_settings_encryption_model import BackupStorageSettingsEncryptionModel
    from ..models.file_backup_copy_job_schedule_model import FileBackupCopyJobScheduleModel
    from ..models.file_backup_retention_policy_settings_model import FileBackupRetentionPolicySettingsModel
    from ..models.gfs_policy_settings_model import GFSPolicySettingsModel


T = TypeVar("T", bound="FileBackupCopyJobSpec")


@_attrs_define
class FileBackupCopyJobSpec:
    """Settings for backup copy job.

    Attributes:
        name (str): Name of the job.
        type_ (EJobType): Type of the job.
        backup_repository_id (UUID): Backup repository ID. To get the ID, run the [Get All
            Repositories](Repositories#operation/GetAllRepositories) request.
        primary_job_id (UUID | Unset): Primary job ID. To get the ID, run the [Get All Jobs](Jobs#operation/GetAllJobs)
            request.
        use_custom_retention (bool | Unset): If `true`, the backup copy job will use custom retention settings.
        retention_policy (FileBackupRetentionPolicySettingsModel | Unset): Retention policy settings.
        gfs_policy (GFSPolicySettingsModel | Unset): GFS retention policy settings.
        use_custom_encryption (bool | Unset): If `true`, the backup copy job will use custom encryption settings.
        encryption (BackupStorageSettingsEncryptionModel | Unset): Encryption of backup files.
        schedule (FileBackupCopyJobScheduleModel | Unset): Schedule for backup copy job.
    """

    name: str
    type_: EJobType
    backup_repository_id: UUID
    primary_job_id: UUID | Unset = UNSET
    use_custom_retention: bool | Unset = UNSET
    retention_policy: FileBackupRetentionPolicySettingsModel | Unset = UNSET
    gfs_policy: GFSPolicySettingsModel | Unset = UNSET
    use_custom_encryption: bool | Unset = UNSET
    encryption: BackupStorageSettingsEncryptionModel | Unset = UNSET
    schedule: FileBackupCopyJobScheduleModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        backup_repository_id = str(self.backup_repository_id)

        primary_job_id: str | Unset = UNSET
        if not isinstance(self.primary_job_id, Unset):
            primary_job_id = str(self.primary_job_id)

        use_custom_retention = self.use_custom_retention

        retention_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention_policy, Unset):
            retention_policy = self.retention_policy.to_dict()

        gfs_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gfs_policy, Unset):
            gfs_policy = self.gfs_policy.to_dict()

        use_custom_encryption = self.use_custom_encryption

        encryption: dict[str, Any] | Unset = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.to_dict()

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "backupRepositoryId": backup_repository_id,
            }
        )
        if primary_job_id is not UNSET:
            field_dict["primaryJobId"] = primary_job_id
        if use_custom_retention is not UNSET:
            field_dict["useCustomRetention"] = use_custom_retention
        if retention_policy is not UNSET:
            field_dict["retentionPolicy"] = retention_policy
        if gfs_policy is not UNSET:
            field_dict["gfsPolicy"] = gfs_policy
        if use_custom_encryption is not UNSET:
            field_dict["useCustomEncryption"] = use_custom_encryption
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_storage_settings_encryption_model import BackupStorageSettingsEncryptionModel
        from ..models.file_backup_copy_job_schedule_model import FileBackupCopyJobScheduleModel
        from ..models.file_backup_retention_policy_settings_model import FileBackupRetentionPolicySettingsModel
        from ..models.gfs_policy_settings_model import GFSPolicySettingsModel

        d = dict(src_dict)
        name = d.pop("name")

        type_ = EJobType(d.pop("type"))

        backup_repository_id = UUID(d.pop("backupRepositoryId"))

        _primary_job_id = d.pop("primaryJobId", UNSET)
        primary_job_id: UUID | Unset
        if isinstance(_primary_job_id, Unset):
            primary_job_id = UNSET
        else:
            primary_job_id = UUID(_primary_job_id)

        use_custom_retention = d.pop("useCustomRetention", UNSET)

        _retention_policy = d.pop("retentionPolicy", UNSET)
        retention_policy: FileBackupRetentionPolicySettingsModel | Unset
        if isinstance(_retention_policy, Unset):
            retention_policy = UNSET
        else:
            retention_policy = FileBackupRetentionPolicySettingsModel.from_dict(_retention_policy)

        _gfs_policy = d.pop("gfsPolicy", UNSET)
        gfs_policy: GFSPolicySettingsModel | Unset
        if isinstance(_gfs_policy, Unset):
            gfs_policy = UNSET
        else:
            gfs_policy = GFSPolicySettingsModel.from_dict(_gfs_policy)

        use_custom_encryption = d.pop("useCustomEncryption", UNSET)

        _encryption = d.pop("encryption", UNSET)
        encryption: BackupStorageSettingsEncryptionModel | Unset
        if isinstance(_encryption, Unset):
            encryption = UNSET
        else:
            encryption = BackupStorageSettingsEncryptionModel.from_dict(_encryption)

        _schedule = d.pop("schedule", UNSET)
        schedule: FileBackupCopyJobScheduleModel | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = FileBackupCopyJobScheduleModel.from_dict(_schedule)

        file_backup_copy_job_spec = cls(
            name=name,
            type_=type_,
            backup_repository_id=backup_repository_id,
            primary_job_id=primary_job_id,
            use_custom_retention=use_custom_retention,
            retention_policy=retention_policy,
            gfs_policy=gfs_policy,
            use_custom_encryption=use_custom_encryption,
            encryption=encryption,
            schedule=schedule,
        )

        file_backup_copy_job_spec.additional_properties = d
        return file_backup_copy_job_spec

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
