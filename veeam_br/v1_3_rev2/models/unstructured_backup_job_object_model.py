from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_unstructured_backup_job_object_type import EUnstructuredBackupJobObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredBackupJobObjectModel")


@_attrs_define
class UnstructuredBackupJobObjectModel:
    """Object processed by the job.

    Attributes:
        type_ (EUnstructuredBackupJobObjectType): Task type.
        path (str | Unset): Path to folders and files.
    """

    type_: EUnstructuredBackupJobObjectType
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = EUnstructuredBackupJobObjectType(d.pop("type"))

        path = d.pop("path", UNSET)

        unstructured_backup_job_object_model = cls(
            type_=type_,
            path=path,
        )

        unstructured_backup_job_object_model.additional_properties = d
        return unstructured_backup_job_object_model

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
