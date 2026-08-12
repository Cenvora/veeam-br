from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_job_type import EJobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_schedule_model import BackupScheduleModel
    from ..models.file_backup_copy_job_spec import FileBackupCopyJobSpec
    from ..models.object_storage_backup_job_primary_repository_model import ObjectStorageBackupJobPrimaryRepositoryModel
    from ..models.unstructured_backup_job_object_model import UnstructuredBackupJobObjectModel
    from ..models.unstructured_data_backup_job_archive_repository_model import (
        UnstructuredDataBackupJobArchiveRepositoryModel,
    )


T = TypeVar("T", bound="ObjectStorageBackupJobSpec")


@_attrs_define
class ObjectStorageBackupJobSpec:
    """Settings for object storage backup job.

    Attributes:
        name (str): Name of the job.
        type_ (EJobType): Type of the job.
        objects (list[UnstructuredBackupJobObjectModel]): Array of objects processed by the backup job.
        description (str | Unset): Description of the job.
        is_high_priority (bool | Unset): If `true`, the resource scheduler prioritizes this job higher than other
            similar jobs and allocates resources to it in the first place.
        backup_repository (ObjectStorageBackupJobPrimaryRepositoryModel | Unset): Primary repository settings for object
            storage backup jobs.
        archive_repository (UnstructuredDataBackupJobArchiveRepositoryModel | Unset): Archive repository settings for
            unstructured data backup job.
        secondary_targets (list[FileBackupCopyJobSpec] | Unset): Array of secondary target jobs (backup copy and backup
            to tape jobs) linked to the backup job.
        schedule (BackupScheduleModel | Unset): Job scheduling options.
    """

    name: str
    type_: EJobType
    objects: list[UnstructuredBackupJobObjectModel]
    description: str | Unset = UNSET
    is_high_priority: bool | Unset = UNSET
    backup_repository: ObjectStorageBackupJobPrimaryRepositoryModel | Unset = UNSET
    archive_repository: UnstructuredDataBackupJobArchiveRepositoryModel | Unset = UNSET
    secondary_targets: list[FileBackupCopyJobSpec] | Unset = UNSET
    schedule: BackupScheduleModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        objects = []
        for objects_item_data in self.objects:
            objects_item = objects_item_data.to_dict()
            objects.append(objects_item)

        description = self.description

        is_high_priority = self.is_high_priority

        backup_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_repository, Unset):
            backup_repository = self.backup_repository.to_dict()

        archive_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.archive_repository, Unset):
            archive_repository = self.archive_repository.to_dict()

        secondary_targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secondary_targets, Unset):
            secondary_targets = []
            for secondary_targets_item_data in self.secondary_targets:
                secondary_targets_item = secondary_targets_item_data.to_dict()
                secondary_targets.append(secondary_targets_item)

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "objects": objects,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_high_priority is not UNSET:
            field_dict["isHighPriority"] = is_high_priority
        if backup_repository is not UNSET:
            field_dict["backupRepository"] = backup_repository
        if archive_repository is not UNSET:
            field_dict["archiveRepository"] = archive_repository
        if secondary_targets is not UNSET:
            field_dict["secondaryTargets"] = secondary_targets
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_schedule_model import BackupScheduleModel
        from ..models.file_backup_copy_job_spec import FileBackupCopyJobSpec
        from ..models.object_storage_backup_job_primary_repository_model import (
            ObjectStorageBackupJobPrimaryRepositoryModel,
        )
        from ..models.unstructured_backup_job_object_model import UnstructuredBackupJobObjectModel
        from ..models.unstructured_data_backup_job_archive_repository_model import (
            UnstructuredDataBackupJobArchiveRepositoryModel,
        )

        d = dict(src_dict)
        name = d.pop("name")

        type_ = EJobType(d.pop("type"))

        objects = []
        _objects = d.pop("objects")
        for objects_item_data in _objects:
            objects_item = UnstructuredBackupJobObjectModel.from_dict(objects_item_data)

            objects.append(objects_item)

        description = d.pop("description", UNSET)

        is_high_priority = d.pop("isHighPriority", UNSET)

        _backup_repository = d.pop("backupRepository", UNSET)
        backup_repository: ObjectStorageBackupJobPrimaryRepositoryModel | Unset
        if isinstance(_backup_repository, Unset):
            backup_repository = UNSET
        else:
            backup_repository = ObjectStorageBackupJobPrimaryRepositoryModel.from_dict(_backup_repository)

        _archive_repository = d.pop("archiveRepository", UNSET)
        archive_repository: UnstructuredDataBackupJobArchiveRepositoryModel | Unset
        if isinstance(_archive_repository, Unset):
            archive_repository = UNSET
        else:
            archive_repository = UnstructuredDataBackupJobArchiveRepositoryModel.from_dict(_archive_repository)

        _secondary_targets = d.pop("secondaryTargets", UNSET)
        secondary_targets: list[FileBackupCopyJobSpec] | Unset = UNSET
        if _secondary_targets is not UNSET:
            secondary_targets = []
            for secondary_targets_item_data in _secondary_targets:
                secondary_targets_item = FileBackupCopyJobSpec.from_dict(secondary_targets_item_data)

                secondary_targets.append(secondary_targets_item)

        _schedule = d.pop("schedule", UNSET)
        schedule: BackupScheduleModel | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = BackupScheduleModel.from_dict(_schedule)

        object_storage_backup_job_spec = cls(
            name=name,
            type_=type_,
            objects=objects,
            description=description,
            is_high_priority=is_high_priority,
            backup_repository=backup_repository,
            archive_repository=archive_repository,
            secondary_targets=secondary_targets,
            schedule=schedule,
        )

        object_storage_backup_job_spec.additional_properties = d
        return object_storage_backup_job_spec

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
