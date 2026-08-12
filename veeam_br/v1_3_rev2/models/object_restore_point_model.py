from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.e_backup_file_gfs_period import EBackupFileGFSPeriod
from ..models.e_guest_os_family import EGuestOSFamily
from ..models.e_object_restore_point_operation import EObjectRestorePointOperation
from ..models.e_platform_type import EPlatformType
from ..models.e_restore_point_type import ERestorePointType
from ..models.e_suspicious_activity_severity import ESuspiciousActivitySeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectRestorePointModel")


@_attrs_define
class ObjectRestorePointModel:
    """Restore point.

    Attributes:
        id (UUID): ID of the restore point.
        name (str): Object name.
        platform_name (EPlatformType): Platform type.<p>`Test` is the platform of SureBackup content scan job
            (`SureBackupContentScan`) — backup verification and content scanning with antivirus software or YARA rules.</p>
        platform_id (UUID): ID of a platform where the object was created.
        creation_time (datetime.datetime): Date and time when the restore point was created.
        backup_id (UUID): ID of a backup that contains the restore point.
        allowed_operations (list[EObjectRestorePointOperation]): Array of operations allowed for the restore point.
        type_ (ERestorePointType | Unset): Restore point type.
        session_id (UUID | Unset): Session ID.
        malware_status (ESuspiciousActivitySeverity | Unset): Malware status.
        backup_file_id (UUID | Unset): Id of a file in which this restore point is stored.
        guest_os_family (EGuestOSFamily | Unset): Family of the guest OS.
        original_size (int | Unset): Original size of the workload.
        tag (str | Unset): Restore point tag.
        snapshot_type (int | Unset): Snapshot type for different platform service endpoints.
        gfs_periods (list[EBackupFileGFSPeriod] | Unset): Array of GFS flags assigned to the restore point. Applies to
            NAS backup restore points only.
    """

    id: UUID
    name: str
    platform_name: EPlatformType
    platform_id: UUID
    creation_time: datetime.datetime
    backup_id: UUID
    allowed_operations: list[EObjectRestorePointOperation]
    type_: ERestorePointType | Unset = UNSET
    session_id: UUID | Unset = UNSET
    malware_status: ESuspiciousActivitySeverity | Unset = UNSET
    backup_file_id: UUID | Unset = UNSET
    guest_os_family: EGuestOSFamily | Unset = UNSET
    original_size: int | Unset = UNSET
    tag: str | Unset = UNSET
    snapshot_type: int | Unset = UNSET
    gfs_periods: list[EBackupFileGFSPeriod] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        platform_name = self.platform_name.value

        platform_id = str(self.platform_id)

        creation_time = self.creation_time.isoformat()

        backup_id = str(self.backup_id)

        allowed_operations = []
        for allowed_operations_item_data in self.allowed_operations:
            allowed_operations_item = allowed_operations_item_data.value
            allowed_operations.append(allowed_operations_item)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        session_id: str | Unset = UNSET
        if not isinstance(self.session_id, Unset):
            session_id = str(self.session_id)

        malware_status: str | Unset = UNSET
        if not isinstance(self.malware_status, Unset):
            malware_status = self.malware_status.value

        backup_file_id: str | Unset = UNSET
        if not isinstance(self.backup_file_id, Unset):
            backup_file_id = str(self.backup_file_id)

        guest_os_family: str | Unset = UNSET
        if not isinstance(self.guest_os_family, Unset):
            guest_os_family = self.guest_os_family.value

        original_size = self.original_size

        tag = self.tag

        snapshot_type = self.snapshot_type

        gfs_periods: list[str] | Unset = UNSET
        if not isinstance(self.gfs_periods, Unset):
            gfs_periods = []
            for gfs_periods_item_data in self.gfs_periods:
                gfs_periods_item = gfs_periods_item_data.value
                gfs_periods.append(gfs_periods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "platformName": platform_name,
                "platformId": platform_id,
                "creationTime": creation_time,
                "backupId": backup_id,
                "allowedOperations": allowed_operations,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if malware_status is not UNSET:
            field_dict["malwareStatus"] = malware_status
        if backup_file_id is not UNSET:
            field_dict["backupFileId"] = backup_file_id
        if guest_os_family is not UNSET:
            field_dict["guestOsFamily"] = guest_os_family
        if original_size is not UNSET:
            field_dict["originalSize"] = original_size
        if tag is not UNSET:
            field_dict["tag"] = tag
        if snapshot_type is not UNSET:
            field_dict["snapshotType"] = snapshot_type
        if gfs_periods is not UNSET:
            field_dict["gfsPeriods"] = gfs_periods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        platform_name = EPlatformType(d.pop("platformName"))

        platform_id = UUID(d.pop("platformId"))

        creation_time = isoparse(d.pop("creationTime"))

        backup_id = UUID(d.pop("backupId"))

        allowed_operations = []
        _allowed_operations = d.pop("allowedOperations")
        for allowed_operations_item_data in _allowed_operations:
            allowed_operations_item = EObjectRestorePointOperation(allowed_operations_item_data)

            allowed_operations.append(allowed_operations_item)

        _type_ = d.pop("type", UNSET)
        type_: ERestorePointType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ERestorePointType(_type_)

        _session_id = d.pop("sessionId", UNSET)
        session_id: UUID | Unset
        if isinstance(_session_id, Unset):
            session_id = UNSET
        else:
            session_id = UUID(_session_id)

        _malware_status = d.pop("malwareStatus", UNSET)
        malware_status: ESuspiciousActivitySeverity | Unset
        if isinstance(_malware_status, Unset):
            malware_status = UNSET
        else:
            malware_status = ESuspiciousActivitySeverity(_malware_status)

        _backup_file_id = d.pop("backupFileId", UNSET)
        backup_file_id: UUID | Unset
        if isinstance(_backup_file_id, Unset):
            backup_file_id = UNSET
        else:
            backup_file_id = UUID(_backup_file_id)

        _guest_os_family = d.pop("guestOsFamily", UNSET)
        guest_os_family: EGuestOSFamily | Unset
        if isinstance(_guest_os_family, Unset):
            guest_os_family = UNSET
        else:
            guest_os_family = EGuestOSFamily(_guest_os_family)

        original_size = d.pop("originalSize", UNSET)

        tag = d.pop("tag", UNSET)

        snapshot_type = d.pop("snapshotType", UNSET)

        _gfs_periods = d.pop("gfsPeriods", UNSET)
        gfs_periods: list[EBackupFileGFSPeriod] | Unset = UNSET
        if _gfs_periods is not UNSET:
            gfs_periods = []
            for gfs_periods_item_data in _gfs_periods:
                gfs_periods_item = EBackupFileGFSPeriod(gfs_periods_item_data)

                gfs_periods.append(gfs_periods_item)

        object_restore_point_model = cls(
            id=id,
            name=name,
            platform_name=platform_name,
            platform_id=platform_id,
            creation_time=creation_time,
            backup_id=backup_id,
            allowed_operations=allowed_operations,
            type_=type_,
            session_id=session_id,
            malware_status=malware_status,
            backup_file_id=backup_file_id,
            guest_os_family=guest_os_family,
            original_size=original_size,
            tag=tag,
            snapshot_type=snapshot_type,
            gfs_periods=gfs_periods,
        )

        object_restore_point_model.additional_properties = d
        return object_restore_point_model

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
