from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_job_type import EJobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_job_guest_processing_model import BackupJobGuestProcessingModel
    from ..models.backup_schedule_model import BackupScheduleModel
    from ..models.hyper_v_backup_job_storage_model import HyperVBackupJobStorageModel
    from ..models.hyper_v_backup_job_virtual_machines_model import HyperVBackupJobVirtualMachinesModel


T = TypeVar("T", bound="HyperVBackupJobSpec")


@_attrs_define
class HyperVBackupJobSpec:
    """Backup job settings for Microsoft Hyper-V VMs.

    Attributes:
        name (str): Name of the job.
        type_ (EJobType): Type of the job.
        description (str): Description of the job.
        is_high_priority (bool | Unset): If `true`, the resource scheduler prioritizes this job over other similar jobs
            and allocates resources to it first. Default: False.
        virtual_machines (HyperVBackupJobVirtualMachinesModel | Unset): Included and excluded objects.
        storage (HyperVBackupJobStorageModel | Unset): Microsoft Hyper-V backup storage settings.
        guest_processing (BackupJobGuestProcessingModel | Unset): Guest processing settings.
        schedule (BackupScheduleModel | Unset): Job scheduling options.
    """

    name: str
    type_: EJobType
    description: str
    is_high_priority: bool | Unset = False
    virtual_machines: HyperVBackupJobVirtualMachinesModel | Unset = UNSET
    storage: HyperVBackupJobStorageModel | Unset = UNSET
    guest_processing: BackupJobGuestProcessingModel | Unset = UNSET
    schedule: BackupScheduleModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        description = self.description

        is_high_priority = self.is_high_priority

        virtual_machines: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_machines, Unset):
            virtual_machines = self.virtual_machines.to_dict()

        storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage.to_dict()

        guest_processing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_processing, Unset):
            guest_processing = self.guest_processing.to_dict()

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "description": description,
            }
        )
        if is_high_priority is not UNSET:
            field_dict["isHighPriority"] = is_high_priority
        if virtual_machines is not UNSET:
            field_dict["virtualMachines"] = virtual_machines
        if storage is not UNSET:
            field_dict["storage"] = storage
        if guest_processing is not UNSET:
            field_dict["guestProcessing"] = guest_processing
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_job_guest_processing_model import BackupJobGuestProcessingModel
        from ..models.backup_schedule_model import BackupScheduleModel
        from ..models.hyper_v_backup_job_storage_model import HyperVBackupJobStorageModel
        from ..models.hyper_v_backup_job_virtual_machines_model import HyperVBackupJobVirtualMachinesModel

        d = dict(src_dict)
        name = d.pop("name")

        type_ = EJobType(d.pop("type"))

        description = d.pop("description")

        is_high_priority = d.pop("isHighPriority", UNSET)

        _virtual_machines = d.pop("virtualMachines", UNSET)
        virtual_machines: HyperVBackupJobVirtualMachinesModel | Unset
        if isinstance(_virtual_machines, Unset):
            virtual_machines = UNSET
        else:
            virtual_machines = HyperVBackupJobVirtualMachinesModel.from_dict(_virtual_machines)

        _storage = d.pop("storage", UNSET)
        storage: HyperVBackupJobStorageModel | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = HyperVBackupJobStorageModel.from_dict(_storage)

        _guest_processing = d.pop("guestProcessing", UNSET)
        guest_processing: BackupJobGuestProcessingModel | Unset
        if isinstance(_guest_processing, Unset):
            guest_processing = UNSET
        else:
            guest_processing = BackupJobGuestProcessingModel.from_dict(_guest_processing)

        _schedule = d.pop("schedule", UNSET)
        schedule: BackupScheduleModel | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = BackupScheduleModel.from_dict(_schedule)

        hyper_v_backup_job_spec = cls(
            name=name,
            type_=type_,
            description=description,
            is_high_priority=is_high_priority,
            virtual_machines=virtual_machines,
            storage=storage,
            guest_processing=guest_processing,
            schedule=schedule,
        )

        hyper_v_backup_job_spec.additional_properties = d
        return hyper_v_backup_job_spec

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
