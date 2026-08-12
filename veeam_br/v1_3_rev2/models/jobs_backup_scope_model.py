from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_inventory_scope_workload_type import EInventoryScopeWorkloadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jobs_backup_scope_item_model import JobsBackupScopeItemModel


T = TypeVar("T", bound="JobsBackupScopeModel")


@_attrs_define
class JobsBackupScopeModel:
    """Job backup scope.

    Attributes:
        type_ (EInventoryScopeWorkloadType): Workload type.
        jobs (list[JobsBackupScopeItemModel] | Unset): Array of jobs.
    """

    type_: EInventoryScopeWorkloadType
    jobs: list[JobsBackupScopeItemModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        jobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()
                jobs.append(jobs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if jobs is not UNSET:
            field_dict["jobs"] = jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jobs_backup_scope_item_model import JobsBackupScopeItemModel

        d = dict(src_dict)
        type_ = EInventoryScopeWorkloadType(d.pop("type"))

        _jobs = d.pop("jobs", UNSET)
        jobs: list[JobsBackupScopeItemModel] | Unset = UNSET
        if _jobs is not UNSET:
            jobs = []
            for jobs_item_data in _jobs:
                jobs_item = JobsBackupScopeItemModel.from_dict(jobs_item_data)

                jobs.append(jobs_item)

        jobs_backup_scope_model = cls(
            type_=type_,
            jobs=jobs,
        )

        jobs_backup_scope_model.additional_properties = d
        return jobs_backup_scope_model

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
