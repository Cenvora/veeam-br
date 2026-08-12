from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.export_logs_scope_type import ExportLogsScopeType
from ..models.export_logs_type import ExportLogsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportSupportLogsSpec")


@_attrs_define
class ExportSupportLogsSpec:
    """Log collection settings.

    Attributes:
        export_type (ExportLogsType): Log collection scope.
        scope_type (ExportLogsScopeType): Log collection scope.
        date_from (datetime.datetime | Unset): Date and time marking the beginning of the period for which you want to
            export logs.
        date_to (datetime.datetime | Unset): Date and time marking the end of the period for which you want to export
            logs.
        host_ids (list[UUID] | Unset): Array of managed server IDs whose component logs need to be exported. If an empty
            list is provided, the backup server ID is used.
        job_ids (list[UUID] | Unset): Array of job IDs whose logs need to be exported. Required if the `scopeType`
            property is set to `Jobs`.
        export_local_pg_logs (bool | Unset): If `true`, local PostgreSQL instance logs are collected.
    """

    export_type: ExportLogsType
    scope_type: ExportLogsScopeType
    date_from: datetime.datetime | Unset = UNSET
    date_to: datetime.datetime | Unset = UNSET
    host_ids: list[UUID] | Unset = UNSET
    job_ids: list[UUID] | Unset = UNSET
    export_local_pg_logs: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        export_type = self.export_type.value

        scope_type = self.scope_type.value

        date_from: str | Unset = UNSET
        if not isinstance(self.date_from, Unset):
            date_from = self.date_from.isoformat()

        date_to: str | Unset = UNSET
        if not isinstance(self.date_to, Unset):
            date_to = self.date_to.isoformat()

        host_ids: list[str] | Unset = UNSET
        if not isinstance(self.host_ids, Unset):
            host_ids = []
            for host_ids_item_data in self.host_ids:
                host_ids_item = str(host_ids_item_data)
                host_ids.append(host_ids_item)

        job_ids: list[str] | Unset = UNSET
        if not isinstance(self.job_ids, Unset):
            job_ids = []
            for job_ids_item_data in self.job_ids:
                job_ids_item = str(job_ids_item_data)
                job_ids.append(job_ids_item)

        export_local_pg_logs = self.export_local_pg_logs

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "exportType": export_type,
                "scopeType": scope_type,
            }
        )
        if date_from is not UNSET:
            field_dict["dateFrom"] = date_from
        if date_to is not UNSET:
            field_dict["dateTo"] = date_to
        if host_ids is not UNSET:
            field_dict["hostIds"] = host_ids
        if job_ids is not UNSET:
            field_dict["jobIds"] = job_ids
        if export_local_pg_logs is not UNSET:
            field_dict["exportLocalPgLogs"] = export_local_pg_logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        export_type = ExportLogsType(d.pop("exportType"))

        scope_type = ExportLogsScopeType(d.pop("scopeType"))

        _date_from = d.pop("dateFrom", UNSET)
        date_from: datetime.datetime | Unset
        if isinstance(_date_from, Unset):
            date_from = UNSET
        else:
            date_from = isoparse(_date_from)

        _date_to = d.pop("dateTo", UNSET)
        date_to: datetime.datetime | Unset
        if isinstance(_date_to, Unset):
            date_to = UNSET
        else:
            date_to = isoparse(_date_to)

        _host_ids = d.pop("hostIds", UNSET)
        host_ids: list[UUID] | Unset = UNSET
        if _host_ids is not UNSET:
            host_ids = []
            for host_ids_item_data in _host_ids:
                host_ids_item = UUID(host_ids_item_data)

                host_ids.append(host_ids_item)

        _job_ids = d.pop("jobIds", UNSET)
        job_ids: list[UUID] | Unset = UNSET
        if _job_ids is not UNSET:
            job_ids = []
            for job_ids_item_data in _job_ids:
                job_ids_item = UUID(job_ids_item_data)

                job_ids.append(job_ids_item)

        export_local_pg_logs = d.pop("exportLocalPgLogs", UNSET)

        export_support_logs_spec = cls(
            export_type=export_type,
            scope_type=scope_type,
            date_from=date_from,
            date_to=date_to,
            host_ids=host_ids,
            job_ids=job_ids,
            export_local_pg_logs=export_local_pg_logs,
        )

        return export_support_logs_spec
