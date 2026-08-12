from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntraIdTenantRevealBitlockerRecoveryKeyRequest")


@_attrs_define
class EntraIdTenantRevealBitlockerRecoveryKeyRequest:
    """Settings for revealing BitLocker recovery key.

    Attributes:
        device_id (str): Infrastructure ID of the device.
        restore_point_id (UUID | Unset): Restore point ID.
    """

    device_id: str
    restore_point_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        restore_point_id: str | Unset = UNSET
        if not isinstance(self.restore_point_id, Unset):
            restore_point_id = str(self.restore_point_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceId": device_id,
            }
        )
        if restore_point_id is not UNSET:
            field_dict["restorePointId"] = restore_point_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = d.pop("deviceId")

        _restore_point_id = d.pop("restorePointId", UNSET)
        restore_point_id: UUID | Unset
        if isinstance(_restore_point_id, Unset):
            restore_point_id = UNSET
        else:
            restore_point_id = UUID(_restore_point_id)

        entra_id_tenant_reveal_bitlocker_recovery_key_request = cls(
            device_id=device_id,
            restore_point_id=restore_point_id,
        )

        entra_id_tenant_reveal_bitlocker_recovery_key_request.additional_properties = d
        return entra_id_tenant_reveal_bitlocker_recovery_key_request

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
