from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.e_cold_storage_operation_type import EColdStorageOperationType
from ..models.e_cold_storage_retrieval_session_state import EColdStorageRetrievalSessionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredDataArchiveRetrievalModel")


@_attrs_define
class UnstructuredDataArchiveRetrievalModel:
    """Settings for restoring entire file share.

    Attributes:
        operation_id (UUID): Id of the prolongable retrieval operation.
        server_id (UUID): Id of the unstructured data server that was backed-up by the restore point.
        backup_id (UUID): Id of backup the restore point belongs to.
        session_state (EColdStorageRetrievalSessionState): Cold Storage retrieval session state.
        operation_type (EColdStorageOperationType): Cold Storage retrieval operation type.
        restore_point_id (UUID | Unset): Restore point ID. To get the ID, run the [Get All Restore Points](Restore-
            Points#operation/GetAllObjectRestorePoints) request.
        retrieval_expiration_time (datetime.datetime | Unset): Time until the retrieval is kept.
    """

    operation_id: UUID
    server_id: UUID
    backup_id: UUID
    session_state: EColdStorageRetrievalSessionState
    operation_type: EColdStorageOperationType
    restore_point_id: UUID | Unset = UNSET
    retrieval_expiration_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_id = str(self.operation_id)

        server_id = str(self.server_id)

        backup_id = str(self.backup_id)

        session_state = self.session_state.value

        operation_type = self.operation_type.value

        restore_point_id: str | Unset = UNSET
        if not isinstance(self.restore_point_id, Unset):
            restore_point_id = str(self.restore_point_id)

        retrieval_expiration_time: str | Unset = UNSET
        if not isinstance(self.retrieval_expiration_time, Unset):
            retrieval_expiration_time = self.retrieval_expiration_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operationId": operation_id,
                "serverId": server_id,
                "backupId": backup_id,
                "sessionState": session_state,
                "operationType": operation_type,
            }
        )
        if restore_point_id is not UNSET:
            field_dict["restorePointId"] = restore_point_id
        if retrieval_expiration_time is not UNSET:
            field_dict["retrievalExpirationTime"] = retrieval_expiration_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = UUID(d.pop("operationId"))

        server_id = UUID(d.pop("serverId"))

        backup_id = UUID(d.pop("backupId"))

        session_state = EColdStorageRetrievalSessionState(d.pop("sessionState"))

        operation_type = EColdStorageOperationType(d.pop("operationType"))

        _restore_point_id = d.pop("restorePointId", UNSET)
        restore_point_id: UUID | Unset
        if isinstance(_restore_point_id, Unset):
            restore_point_id = UNSET
        else:
            restore_point_id = UUID(_restore_point_id)

        _retrieval_expiration_time = d.pop("retrievalExpirationTime", UNSET)
        retrieval_expiration_time: datetime.datetime | Unset
        if isinstance(_retrieval_expiration_time, Unset):
            retrieval_expiration_time = UNSET
        else:
            retrieval_expiration_time = isoparse(_retrieval_expiration_time)

        unstructured_data_archive_retrieval_model = cls(
            operation_id=operation_id,
            server_id=server_id,
            backup_id=backup_id,
            session_state=session_state,
            operation_type=operation_type,
            restore_point_id=restore_point_id,
            retrieval_expiration_time=retrieval_expiration_time,
        )

        unstructured_data_archive_retrieval_model.additional_properties = d
        return unstructured_data_archive_retrieval_model

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
