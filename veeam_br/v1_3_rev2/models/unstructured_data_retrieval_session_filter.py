from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_cold_storage_operation_type import EColdStorageOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredDataRetrievalSessionFilter")


@_attrs_define
class UnstructuredDataRetrievalSessionFilter:
    """Metadata migration filter.

    Attributes:
        server_id_filter (list[UUID] | Unset):
        backup_id_filter (list[UUID] | Unset):
        restore_point_id_filter (list[UUID] | Unset):
        operation_type_filter (list[EColdStorageOperationType] | Unset):
    """

    server_id_filter: list[UUID] | Unset = UNSET
    backup_id_filter: list[UUID] | Unset = UNSET
    restore_point_id_filter: list[UUID] | Unset = UNSET
    operation_type_filter: list[EColdStorageOperationType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_id_filter: list[str] | Unset = UNSET
        if not isinstance(self.server_id_filter, Unset):
            server_id_filter = []
            for server_id_filter_item_data in self.server_id_filter:
                server_id_filter_item = str(server_id_filter_item_data)
                server_id_filter.append(server_id_filter_item)

        backup_id_filter: list[str] | Unset = UNSET
        if not isinstance(self.backup_id_filter, Unset):
            backup_id_filter = []
            for backup_id_filter_item_data in self.backup_id_filter:
                backup_id_filter_item = str(backup_id_filter_item_data)
                backup_id_filter.append(backup_id_filter_item)

        restore_point_id_filter: list[str] | Unset = UNSET
        if not isinstance(self.restore_point_id_filter, Unset):
            restore_point_id_filter = []
            for restore_point_id_filter_item_data in self.restore_point_id_filter:
                restore_point_id_filter_item = str(restore_point_id_filter_item_data)
                restore_point_id_filter.append(restore_point_id_filter_item)

        operation_type_filter: list[str] | Unset = UNSET
        if not isinstance(self.operation_type_filter, Unset):
            operation_type_filter = []
            for operation_type_filter_item_data in self.operation_type_filter:
                operation_type_filter_item = operation_type_filter_item_data.value
                operation_type_filter.append(operation_type_filter_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_id_filter is not UNSET:
            field_dict["serverIdFilter"] = server_id_filter
        if backup_id_filter is not UNSET:
            field_dict["backupIdFilter"] = backup_id_filter
        if restore_point_id_filter is not UNSET:
            field_dict["restorePointIdFilter"] = restore_point_id_filter
        if operation_type_filter is not UNSET:
            field_dict["operationTypeFilter"] = operation_type_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _server_id_filter = d.pop("serverIdFilter", UNSET)
        server_id_filter: list[UUID] | Unset = UNSET
        if _server_id_filter is not UNSET:
            server_id_filter = []
            for server_id_filter_item_data in _server_id_filter:
                server_id_filter_item = UUID(server_id_filter_item_data)

                server_id_filter.append(server_id_filter_item)

        _backup_id_filter = d.pop("backupIdFilter", UNSET)
        backup_id_filter: list[UUID] | Unset = UNSET
        if _backup_id_filter is not UNSET:
            backup_id_filter = []
            for backup_id_filter_item_data in _backup_id_filter:
                backup_id_filter_item = UUID(backup_id_filter_item_data)

                backup_id_filter.append(backup_id_filter_item)

        _restore_point_id_filter = d.pop("restorePointIdFilter", UNSET)
        restore_point_id_filter: list[UUID] | Unset = UNSET
        if _restore_point_id_filter is not UNSET:
            restore_point_id_filter = []
            for restore_point_id_filter_item_data in _restore_point_id_filter:
                restore_point_id_filter_item = UUID(restore_point_id_filter_item_data)

                restore_point_id_filter.append(restore_point_id_filter_item)

        _operation_type_filter = d.pop("operationTypeFilter", UNSET)
        operation_type_filter: list[EColdStorageOperationType] | Unset = UNSET
        if _operation_type_filter is not UNSET:
            operation_type_filter = []
            for operation_type_filter_item_data in _operation_type_filter:
                operation_type_filter_item = EColdStorageOperationType(operation_type_filter_item_data)

                operation_type_filter.append(operation_type_filter_item)

        unstructured_data_retrieval_session_filter = cls(
            server_id_filter=server_id_filter,
            backup_id_filter=backup_id_filter,
            restore_point_id_filter=restore_point_id_filter,
            operation_type_filter=operation_type_filter,
        )

        unstructured_data_retrieval_session_filter.additional_properties = d
        return unstructured_data_retrieval_session_filter

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
