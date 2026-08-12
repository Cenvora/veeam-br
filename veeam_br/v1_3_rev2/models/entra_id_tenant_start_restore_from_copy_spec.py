from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unstructured_data_cold_storage_retrieval_settings import UnstructuredDataColdStorageRetrievalSettings


T = TypeVar("T", bound="EntraIdTenantStartRestoreFromCopySpec")


@_attrs_define
class EntraIdTenantStartRestoreFromCopySpec:
    """Settings for restore from backup copy.

    Attributes:
        restore_point_id (UUID): ID of a Microsoft Entra ID tenant restore point.
        cold_storage_retrieval_settings (UnstructuredDataColdStorageRetrievalSettings | Unset): Settings for retrieving
            data from cold storage.
    """

    restore_point_id: UUID
    cold_storage_retrieval_settings: UnstructuredDataColdStorageRetrievalSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_point_id = str(self.restore_point_id)

        cold_storage_retrieval_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cold_storage_retrieval_settings, Unset):
            cold_storage_retrieval_settings = self.cold_storage_retrieval_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restorePointId": restore_point_id,
            }
        )
        if cold_storage_retrieval_settings is not UNSET:
            field_dict["coldStorageRetrievalSettings"] = cold_storage_retrieval_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unstructured_data_cold_storage_retrieval_settings import (
            UnstructuredDataColdStorageRetrievalSettings,
        )

        d = dict(src_dict)
        restore_point_id = UUID(d.pop("restorePointId"))

        _cold_storage_retrieval_settings = d.pop("coldStorageRetrievalSettings", UNSET)
        cold_storage_retrieval_settings: UnstructuredDataColdStorageRetrievalSettings | Unset
        if isinstance(_cold_storage_retrieval_settings, Unset):
            cold_storage_retrieval_settings = UNSET
        else:
            cold_storage_retrieval_settings = UnstructuredDataColdStorageRetrievalSettings.from_dict(
                _cold_storage_retrieval_settings
            )

        entra_id_tenant_start_restore_from_copy_spec = cls(
            restore_point_id=restore_point_id,
            cold_storage_retrieval_settings=cold_storage_retrieval_settings,
        )

        entra_id_tenant_start_restore_from_copy_spec.additional_properties = d
        return entra_id_tenant_start_restore_from_copy_spec

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
