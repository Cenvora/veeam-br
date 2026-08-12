from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_unstructured_data_restore_overwrite_mode import EUnstructuredDataRestoreOverwriteMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unstructured_data_cold_storage_retrieval_settings import UnstructuredDataColdStorageRetrievalSettings


T = TypeVar("T", bound="UnstructuredDataOSRestoreOptionsModel")


@_attrs_define
class UnstructuredDataOSRestoreOptionsModel:
    """Restore options for restoring entire object storage bucket or container.

    Attributes:
        rollback (bool | Unset): If `true`, the bucket or container will be rolled back to the state as of a specific
            restore point.
        overwrite_mode (EUnstructuredDataRestoreOverwriteMode | Unset): Overwrite mode.
        overwrite_bucket_attributes (bool | Unset): If `true`, bucket attributes will be overwritten.
        cold_storage_retrieval_settings (UnstructuredDataColdStorageRetrievalSettings | Unset): Settings for retrieving
            data from cold storage.
    """

    rollback: bool | Unset = UNSET
    overwrite_mode: EUnstructuredDataRestoreOverwriteMode | Unset = UNSET
    overwrite_bucket_attributes: bool | Unset = UNSET
    cold_storage_retrieval_settings: UnstructuredDataColdStorageRetrievalSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rollback = self.rollback

        overwrite_mode: str | Unset = UNSET
        if not isinstance(self.overwrite_mode, Unset):
            overwrite_mode = self.overwrite_mode.value

        overwrite_bucket_attributes = self.overwrite_bucket_attributes

        cold_storage_retrieval_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cold_storage_retrieval_settings, Unset):
            cold_storage_retrieval_settings = self.cold_storage_retrieval_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rollback is not UNSET:
            field_dict["rollback"] = rollback
        if overwrite_mode is not UNSET:
            field_dict["overwriteMode"] = overwrite_mode
        if overwrite_bucket_attributes is not UNSET:
            field_dict["overwriteBucketAttributes"] = overwrite_bucket_attributes
        if cold_storage_retrieval_settings is not UNSET:
            field_dict["coldStorageRetrievalSettings"] = cold_storage_retrieval_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unstructured_data_cold_storage_retrieval_settings import (
            UnstructuredDataColdStorageRetrievalSettings,
        )

        d = dict(src_dict)
        rollback = d.pop("rollback", UNSET)

        _overwrite_mode = d.pop("overwriteMode", UNSET)
        overwrite_mode: EUnstructuredDataRestoreOverwriteMode | Unset
        if isinstance(_overwrite_mode, Unset):
            overwrite_mode = UNSET
        else:
            overwrite_mode = EUnstructuredDataRestoreOverwriteMode(_overwrite_mode)

        overwrite_bucket_attributes = d.pop("overwriteBucketAttributes", UNSET)

        _cold_storage_retrieval_settings = d.pop("coldStorageRetrievalSettings", UNSET)
        cold_storage_retrieval_settings: UnstructuredDataColdStorageRetrievalSettings | Unset
        if isinstance(_cold_storage_retrieval_settings, Unset):
            cold_storage_retrieval_settings = UNSET
        else:
            cold_storage_retrieval_settings = UnstructuredDataColdStorageRetrievalSettings.from_dict(
                _cold_storage_retrieval_settings
            )

        unstructured_data_os_restore_options_model = cls(
            rollback=rollback,
            overwrite_mode=overwrite_mode,
            overwrite_bucket_attributes=overwrite_bucket_attributes,
            cold_storage_retrieval_settings=cold_storage_retrieval_settings,
        )

        unstructured_data_os_restore_options_model.additional_properties = d
        return unstructured_data_os_restore_options_model

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
