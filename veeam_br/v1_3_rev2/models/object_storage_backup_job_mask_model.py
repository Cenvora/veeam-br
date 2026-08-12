from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_object_storage_backup_mask_type import EObjectStorageBackupMaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorageBackupJobMaskModel")


@_attrs_define
class ObjectStorageBackupJobMaskModel:
    """Path masks for objects and prefixes in object storage.

    Attributes:
        path (str): The object path.
        type_ (EObjectStorageBackupMaskType | Unset): Mask types for object storage backups.
    """

    path: str
    type_: EObjectStorageBackupMaskType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        _type_ = d.pop("type", UNSET)
        type_: EObjectStorageBackupMaskType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EObjectStorageBackupMaskType(_type_)

        object_storage_backup_job_mask_model = cls(
            path=path,
            type_=type_,
        )

        object_storage_backup_job_mask_model.additional_properties = d
        return object_storage_backup_job_mask_model

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
