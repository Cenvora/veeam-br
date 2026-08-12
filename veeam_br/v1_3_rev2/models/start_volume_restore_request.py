from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disk_mapping_context import DiskMappingContext


T = TypeVar("T", bound="StartVolumeRestoreRequest")


@_attrs_define
class StartVolumeRestoreRequest:
    """Request for starting volume restore operation.

    Attributes:
        disk_management_session_id (UUID): Disk management session ID.
        disk_mapping_context (DiskMappingContext): Disk mapping context.
        reason (str | Unset): Reason for starting volume restore operation.
        inject_drivers (bool | Unset): If `true`, drivers are injected during the volume restore operation.
    """

    disk_management_session_id: UUID
    disk_mapping_context: DiskMappingContext
    reason: str | Unset = UNSET
    inject_drivers: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disk_management_session_id = str(self.disk_management_session_id)

        disk_mapping_context = self.disk_mapping_context.to_dict()

        reason = self.reason

        inject_drivers = self.inject_drivers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "diskManagementSessionId": disk_management_session_id,
                "diskMappingContext": disk_mapping_context,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if inject_drivers is not UNSET:
            field_dict["injectDrivers"] = inject_drivers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disk_mapping_context import DiskMappingContext

        d = dict(src_dict)
        disk_management_session_id = UUID(d.pop("diskManagementSessionId"))

        disk_mapping_context = DiskMappingContext.from_dict(d.pop("diskMappingContext"))

        reason = d.pop("reason", UNSET)

        inject_drivers = d.pop("injectDrivers", UNSET)

        start_volume_restore_request = cls(
            disk_management_session_id=disk_management_session_id,
            disk_mapping_context=disk_mapping_context,
            reason=reason,
            inject_drivers=inject_drivers,
        )

        start_volume_restore_request.additional_properties = d
        return start_volume_restore_request

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
