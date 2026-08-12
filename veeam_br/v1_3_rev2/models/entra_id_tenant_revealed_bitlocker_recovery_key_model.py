from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.entra_id_tenant_revealed_bitlocker_recovery_key_model_volume_type import (
    EntraIdTenantRevealedBitlockerRecoveryKeyModelVolumeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EntraIdTenantRevealedBitlockerRecoveryKeyModel")


@_attrs_define
class EntraIdTenantRevealedBitlockerRecoveryKeyModel:
    """Revealed BitLocker recovery key.

    Attributes:
        bitlocker_recovery_key_id (str): BitLocker recovery key ID.
        device_id (str): Infrastructure ID of the device.
        recovery_key (str): Recovery key.
        created_date_time (datetime.datetime | Unset): Date and time when the BitLocker recovery key was created.
        volume_type (EntraIdTenantRevealedBitlockerRecoveryKeyModelVolumeType | Unset): Type of the volume protected by
            the BitLocker recovery key.
    """

    bitlocker_recovery_key_id: str
    device_id: str
    recovery_key: str
    created_date_time: datetime.datetime | Unset = UNSET
    volume_type: EntraIdTenantRevealedBitlockerRecoveryKeyModelVolumeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bitlocker_recovery_key_id = self.bitlocker_recovery_key_id

        device_id = self.device_id

        recovery_key = self.recovery_key

        created_date_time: str | Unset = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat()

        volume_type: str | Unset = UNSET
        if not isinstance(self.volume_type, Unset):
            volume_type = self.volume_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bitlockerRecoveryKeyId": bitlocker_recovery_key_id,
                "deviceId": device_id,
                "recoveryKey": recovery_key,
            }
        )
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if volume_type is not UNSET:
            field_dict["volumeType"] = volume_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bitlocker_recovery_key_id = d.pop("bitlockerRecoveryKeyId")

        device_id = d.pop("deviceId")

        recovery_key = d.pop("recoveryKey")

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: datetime.datetime | Unset
        if isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        _volume_type = d.pop("volumeType", UNSET)
        volume_type: EntraIdTenantRevealedBitlockerRecoveryKeyModelVolumeType | Unset
        if isinstance(_volume_type, Unset):
            volume_type = UNSET
        else:
            volume_type = EntraIdTenantRevealedBitlockerRecoveryKeyModelVolumeType(_volume_type)

        entra_id_tenant_revealed_bitlocker_recovery_key_model = cls(
            bitlocker_recovery_key_id=bitlocker_recovery_key_id,
            device_id=device_id,
            recovery_key=recovery_key,
            created_date_time=created_date_time,
            volume_type=volume_type,
        )

        entra_id_tenant_revealed_bitlocker_recovery_key_model.additional_properties = d
        return entra_id_tenant_revealed_bitlocker_recovery_key_model

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
