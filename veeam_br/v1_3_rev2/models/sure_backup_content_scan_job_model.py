from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_job_type import EJobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sure_backup_job_schedule_model import SureBackupJobScheduleModel
    from ..models.sure_backup_job_verification_options_model import SureBackupJobVerificationOptionsModel
    from ..models.sure_backup_linked_jobs_model import SureBackupLinkedJobsModel
    from ..models.unstructured_linked_jobs_model import UnstructuredLinkedJobsModel


T = TypeVar("T", bound="SureBackupContentScanJobModel")


@_attrs_define
class SureBackupContentScanJobModel:
    """SureBackup Lite job.

    Attributes:
        id (UUID): Job ID.
        name (str): Name of the job.
        type_ (EJobType): Type of the job.
        verification_options (SureBackupJobVerificationOptionsModel): SureBackup job verification options.
        is_disabled (bool | Unset): If `true`, the job is disabled.
        description (str | Unset): SureBackup job description.
        linked_jobs (SureBackupLinkedJobsModel | Unset): Veeam Backup for Microsoft Azure, Veeam Backup for AWS, or
            Veeam Backup for Google Cloud backup policies with machines that you want to verify with the SureBackup job.
        unstructured_linked_jobs (UnstructuredLinkedJobsModel | Unset): NAS/unstructured backup jobs to verify with the
            SureBackup job.
        schedule (SureBackupJobScheduleModel | Unset): SureBackup job schedule.
    """

    id: UUID
    name: str
    type_: EJobType
    verification_options: SureBackupJobVerificationOptionsModel
    is_disabled: bool | Unset = UNSET
    description: str | Unset = UNSET
    linked_jobs: SureBackupLinkedJobsModel | Unset = UNSET
    unstructured_linked_jobs: UnstructuredLinkedJobsModel | Unset = UNSET
    schedule: SureBackupJobScheduleModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        type_ = self.type_.value

        verification_options = self.verification_options.to_dict()

        is_disabled = self.is_disabled

        description = self.description

        linked_jobs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.linked_jobs, Unset):
            linked_jobs = self.linked_jobs.to_dict()

        unstructured_linked_jobs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unstructured_linked_jobs, Unset):
            unstructured_linked_jobs = self.unstructured_linked_jobs.to_dict()

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "verificationOptions": verification_options,
            }
        )
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled
        if description is not UNSET:
            field_dict["description"] = description
        if linked_jobs is not UNSET:
            field_dict["linkedJobs"] = linked_jobs
        if unstructured_linked_jobs is not UNSET:
            field_dict["unstructuredLinkedJobs"] = unstructured_linked_jobs
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sure_backup_job_schedule_model import SureBackupJobScheduleModel
        from ..models.sure_backup_job_verification_options_model import SureBackupJobVerificationOptionsModel
        from ..models.sure_backup_linked_jobs_model import SureBackupLinkedJobsModel
        from ..models.unstructured_linked_jobs_model import UnstructuredLinkedJobsModel

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        type_ = EJobType(d.pop("type"))

        verification_options = SureBackupJobVerificationOptionsModel.from_dict(d.pop("verificationOptions"))

        is_disabled = d.pop("isDisabled", UNSET)

        description = d.pop("description", UNSET)

        _linked_jobs = d.pop("linkedJobs", UNSET)
        linked_jobs: SureBackupLinkedJobsModel | Unset
        if isinstance(_linked_jobs, Unset):
            linked_jobs = UNSET
        else:
            linked_jobs = SureBackupLinkedJobsModel.from_dict(_linked_jobs)

        _unstructured_linked_jobs = d.pop("unstructuredLinkedJobs", UNSET)
        unstructured_linked_jobs: UnstructuredLinkedJobsModel | Unset
        if isinstance(_unstructured_linked_jobs, Unset):
            unstructured_linked_jobs = UNSET
        else:
            unstructured_linked_jobs = UnstructuredLinkedJobsModel.from_dict(_unstructured_linked_jobs)

        _schedule = d.pop("schedule", UNSET)
        schedule: SureBackupJobScheduleModel | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = SureBackupJobScheduleModel.from_dict(_schedule)

        sure_backup_content_scan_job_model = cls(
            id=id,
            name=name,
            type_=type_,
            verification_options=verification_options,
            is_disabled=is_disabled,
            description=description,
            linked_jobs=linked_jobs,
            unstructured_linked_jobs=unstructured_linked_jobs,
            schedule=schedule,
        )

        sure_backup_content_scan_job_model.additional_properties = d
        return sure_backup_content_scan_job_model

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
