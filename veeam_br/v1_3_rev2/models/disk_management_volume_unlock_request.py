from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiskManagementVolumeUnlockRequest")


@_attrs_define
class DiskManagementVolumeUnlockRequest:
    """Settings for unlocking a BitLocker-protected volume.

    Attributes:
        disk_management_session_id (UUID): Disk management session ID.
        volume_id (UUID): Selected volume ID.
        key_or_password (str): Numeric key or password for the locked volume.
        volume_name (str | Unset): Volume name.
    """

    disk_management_session_id: UUID
    volume_id: UUID
    key_or_password: str
    volume_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disk_management_session_id = str(self.disk_management_session_id)

        volume_id = str(self.volume_id)

        key_or_password = self.key_or_password

        volume_name = self.volume_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "diskManagementSessionId": disk_management_session_id,
                "volumeId": volume_id,
                "keyOrPassword": key_or_password,
            }
        )
        if volume_name is not UNSET:
            field_dict["volumeName"] = volume_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disk_management_session_id = UUID(d.pop("diskManagementSessionId"))

        volume_id = UUID(d.pop("volumeId"))

        key_or_password = d.pop("keyOrPassword")

        volume_name = d.pop("volumeName", UNSET)

        disk_management_volume_unlock_request = cls(
            disk_management_session_id=disk_management_session_id,
            volume_id=volume_id,
            key_or_password=key_or_password,
            volume_name=volume_name,
        )

        disk_management_volume_unlock_request.additional_properties = d
        return disk_management_volume_unlock_request

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
