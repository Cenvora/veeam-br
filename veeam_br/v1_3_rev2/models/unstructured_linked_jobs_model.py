from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_object_model import JobObjectModel


T = TypeVar("T", bound="UnstructuredLinkedJobsModel")


@_attrs_define
class UnstructuredLinkedJobsModel:
    """NAS/unstructured backup jobs to verify with the SureBackup job.

    Attributes:
        includes (list[JobObjectModel]): Array of unstructured backup jobs to link. To get information about supported
            jobs, run the [Get All Job States](Jobs#operation/GetAllJobsStates) request and filter the results by job
            type&#58; `FileBackup` or `ObjectStorageBackup`.
    """

    includes: list[JobObjectModel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        includes = []
        for includes_item_data in self.includes:
            includes_item = includes_item_data.to_dict()
            includes.append(includes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "includes": includes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_object_model import JobObjectModel

        d = dict(src_dict)
        includes = []
        _includes = d.pop("includes")
        for includes_item_data in _includes:
            includes_item = JobObjectModel.from_dict(includes_item_data)

            includes.append(includes_item)

        unstructured_linked_jobs_model = cls(
            includes=includes,
        )

        unstructured_linked_jobs_model.additional_properties = d
        return unstructured_linked_jobs_model

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
