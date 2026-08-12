from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_job_type import EJobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_job_guest_processing_model import BackupJobGuestProcessingModel
    from ..models.backup_schedule_model import BackupScheduleModel
    from ..models.hyper_v_backup_job_storage_model import HyperVBackupJobStorageModel
    from ..models.hyper_v_backup_job_virtual_machines_model import HyperVBackupJobVirtualMachinesModel


T = TypeVar("T", bound="HyperVBackupJobModel")


@_attrs_define
class HyperVBackupJobModel:
    """Microsoft Hyper-V backup job.

    Attributes:
        id (UUID): Job ID.
        name (str): Name of the job.
        type_ (EJobType): Type of the job.
        description (str): Description of the job.
        is_high_priority (bool): If `true`, the resource scheduler prioritizes this job over other similar jobs and
            allocates resources to it first.
        storage (HyperVBackupJobStorageModel): Microsoft Hyper-V backup storage settings.
        guest_processing (BackupJobGuestProcessingModel): Guest processing settings.
        schedule (BackupScheduleModel): Job scheduling options.
        is_disabled (bool | Unset): If `true`, the job is disabled.
        virtual_machines (HyperVBackupJobVirtualMachinesModel | Unset): Included and excluded objects.
    """

    id: UUID
    name: str
    type_: EJobType
    description: str
    is_high_priority: bool
    storage: HyperVBackupJobStorageModel
    guest_processing: BackupJobGuestProcessingModel
    schedule: BackupScheduleModel
    is_disabled: bool | Unset = UNSET
    virtual_machines: HyperVBackupJobVirtualMachinesModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        type_ = self.type_.value

        description = self.description

        is_high_priority = self.is_high_priority

        storage = self.storage.to_dict()

        guest_processing = self.guest_processing.to_dict()

        schedule = self.schedule.to_dict()

        is_disabled = self.is_disabled

        virtual_machines: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_machines, Unset):
            virtual_machines = self.virtual_machines.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "description": description,
                "isHighPriority": is_high_priority,
                "storage": storage,
                "guestProcessing": guest_processing,
                "schedule": schedule,
            }
        )
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled
        if virtual_machines is not UNSET:
            field_dict["virtualMachines"] = virtual_machines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_job_guest_processing_model import BackupJobGuestProcessingModel
        from ..models.backup_schedule_model import BackupScheduleModel
        from ..models.hyper_v_backup_job_storage_model import HyperVBackupJobStorageModel
        from ..models.hyper_v_backup_job_virtual_machines_model import HyperVBackupJobVirtualMachinesModel

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        type_ = EJobType(d.pop("type"))

        description = d.pop("description")

        is_high_priority = d.pop("isHighPriority")

        storage = HyperVBackupJobStorageModel.from_dict(d.pop("storage"))

        guest_processing = BackupJobGuestProcessingModel.from_dict(d.pop("guestProcessing"))

        schedule = BackupScheduleModel.from_dict(d.pop("schedule"))

        is_disabled = d.pop("isDisabled", UNSET)

        _virtual_machines = d.pop("virtualMachines", UNSET)
        virtual_machines: HyperVBackupJobVirtualMachinesModel | Unset
        if isinstance(_virtual_machines, Unset):
            virtual_machines = UNSET
        else:
            virtual_machines = HyperVBackupJobVirtualMachinesModel.from_dict(_virtual_machines)

        hyper_v_backup_job_model = cls(
            id=id,
            name=name,
            type_=type_,
            description=description,
            is_high_priority=is_high_priority,
            storage=storage,
            guest_processing=guest_processing,
            schedule=schedule,
            is_disabled=is_disabled,
            virtual_machines=virtual_machines,
        )

        hyper_v_backup_job_model.additional_properties = d
        return hyper_v_backup_job_model

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
