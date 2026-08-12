from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unstructured_data_cold_storage_retrieval_settings import UnstructuredDataColdStorageRetrievalSettings


T = TypeVar("T", bound="HealthCheckRepairOptions")


@_attrs_define
class HealthCheckRepairOptions:
    """Settings for repair of unstructured data backup or backup job.

    Attributes:
        remove_non_repairable_data_if_needed (bool | Unset): If `true`, data that cannot be repaired will be removed.
        restore_primary_from_archive_if_needed (bool | Unset): If `true`, Veeam Backup & Replication will repair the
            primary data by restoring data from the archive.
        restore_archive_from_primary_if_needed (bool | Unset): If `true`, Veeam Backup & Replication will repair the
            archive data by restoring data from the primary backup.
        enable_cold_storage_retrieval (bool | Unset): If `true`, source data on cold object storage will be retrieved.
            If omitted, the server-side default applies; when defaulted off (the typical case), cold-stored content is not
            retrieved and content checks/repair steps that would need it are skipped.
        cold_storage_retrieval_settings (UnstructuredDataColdStorageRetrievalSettings | Unset): Settings for retrieving
            data from cold storage.
    """

    remove_non_repairable_data_if_needed: bool | Unset = UNSET
    restore_primary_from_archive_if_needed: bool | Unset = UNSET
    restore_archive_from_primary_if_needed: bool | Unset = UNSET
    enable_cold_storage_retrieval: bool | Unset = UNSET
    cold_storage_retrieval_settings: UnstructuredDataColdStorageRetrievalSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        remove_non_repairable_data_if_needed = self.remove_non_repairable_data_if_needed

        restore_primary_from_archive_if_needed = self.restore_primary_from_archive_if_needed

        restore_archive_from_primary_if_needed = self.restore_archive_from_primary_if_needed

        enable_cold_storage_retrieval = self.enable_cold_storage_retrieval

        cold_storage_retrieval_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cold_storage_retrieval_settings, Unset):
            cold_storage_retrieval_settings = self.cold_storage_retrieval_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if remove_non_repairable_data_if_needed is not UNSET:
            field_dict["removeNonRepairableDataIfNeeded"] = remove_non_repairable_data_if_needed
        if restore_primary_from_archive_if_needed is not UNSET:
            field_dict["restorePrimaryFromArchiveIfNeeded"] = restore_primary_from_archive_if_needed
        if restore_archive_from_primary_if_needed is not UNSET:
            field_dict["restoreArchiveFromPrimaryIfNeeded"] = restore_archive_from_primary_if_needed
        if enable_cold_storage_retrieval is not UNSET:
            field_dict["enableColdStorageRetrieval"] = enable_cold_storage_retrieval
        if cold_storage_retrieval_settings is not UNSET:
            field_dict["coldStorageRetrievalSettings"] = cold_storage_retrieval_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unstructured_data_cold_storage_retrieval_settings import (
            UnstructuredDataColdStorageRetrievalSettings,
        )

        d = dict(src_dict)
        remove_non_repairable_data_if_needed = d.pop("removeNonRepairableDataIfNeeded", UNSET)

        restore_primary_from_archive_if_needed = d.pop("restorePrimaryFromArchiveIfNeeded", UNSET)

        restore_archive_from_primary_if_needed = d.pop("restoreArchiveFromPrimaryIfNeeded", UNSET)

        enable_cold_storage_retrieval = d.pop("enableColdStorageRetrieval", UNSET)

        _cold_storage_retrieval_settings = d.pop("coldStorageRetrievalSettings", UNSET)
        cold_storage_retrieval_settings: UnstructuredDataColdStorageRetrievalSettings | Unset
        if isinstance(_cold_storage_retrieval_settings, Unset):
            cold_storage_retrieval_settings = UNSET
        else:
            cold_storage_retrieval_settings = UnstructuredDataColdStorageRetrievalSettings.from_dict(
                _cold_storage_retrieval_settings
            )

        health_check_repair_options = cls(
            remove_non_repairable_data_if_needed=remove_non_repairable_data_if_needed,
            restore_primary_from_archive_if_needed=restore_primary_from_archive_if_needed,
            restore_archive_from_primary_if_needed=restore_archive_from_primary_if_needed,
            enable_cold_storage_retrieval=enable_cold_storage_retrieval,
            cold_storage_retrieval_settings=cold_storage_retrieval_settings,
        )

        health_check_repair_options.additional_properties = d
        return health_check_repair_options

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
