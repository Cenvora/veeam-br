from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.e_entra_id_tenant_item_type import EEntraIdTenantItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EntraIdTenantDeviceBrowseModel")


@_attrs_define
class EntraIdTenantDeviceBrowseModel:
    """Microsoft Entra ID device.

    Attributes:
        id (UUID): Item ID.
        type_ (EEntraIdTenantItemType): Item type.
        display_name (str | Unset): Item display name.
        restore_point_id (UUID | Unset): Restore point ID. To get the ID, run the [Get All Restore Points](Restore-
            Points#operation/GetAllObjectRestorePoints) request.
        restore_point_date (datetime.datetime | Unset): Restore point date and time.
        operating_system (str | Unset): Operating system name.
        operating_system_version (str | Unset): Operating system version.
        device_version (str | Unset): Device version.
        account_enabled (bool | Unset): If `true`, the device is enabled.
        bit_locker_key_count (int | Unset): Number of BitLocker keys associated with the device.
    """

    id: UUID
    type_: EEntraIdTenantItemType
    display_name: str | Unset = UNSET
    restore_point_id: UUID | Unset = UNSET
    restore_point_date: datetime.datetime | Unset = UNSET
    operating_system: str | Unset = UNSET
    operating_system_version: str | Unset = UNSET
    device_version: str | Unset = UNSET
    account_enabled: bool | Unset = UNSET
    bit_locker_key_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_.value

        display_name = self.display_name

        restore_point_id: str | Unset = UNSET
        if not isinstance(self.restore_point_id, Unset):
            restore_point_id = str(self.restore_point_id)

        restore_point_date: str | Unset = UNSET
        if not isinstance(self.restore_point_date, Unset):
            restore_point_date = self.restore_point_date.isoformat()

        operating_system = self.operating_system

        operating_system_version = self.operating_system_version

        device_version = self.device_version

        account_enabled = self.account_enabled

        bit_locker_key_count = self.bit_locker_key_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if restore_point_id is not UNSET:
            field_dict["restorePointId"] = restore_point_id
        if restore_point_date is not UNSET:
            field_dict["restorePointDate"] = restore_point_date
        if operating_system is not UNSET:
            field_dict["operatingSystem"] = operating_system
        if operating_system_version is not UNSET:
            field_dict["operatingSystemVersion"] = operating_system_version
        if device_version is not UNSET:
            field_dict["deviceVersion"] = device_version
        if account_enabled is not UNSET:
            field_dict["accountEnabled"] = account_enabled
        if bit_locker_key_count is not UNSET:
            field_dict["bitLockerKeyCount"] = bit_locker_key_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = EEntraIdTenantItemType(d.pop("type"))

        display_name = d.pop("displayName", UNSET)

        _restore_point_id = d.pop("restorePointId", UNSET)
        restore_point_id: UUID | Unset
        if isinstance(_restore_point_id, Unset):
            restore_point_id = UNSET
        else:
            restore_point_id = UUID(_restore_point_id)

        _restore_point_date = d.pop("restorePointDate", UNSET)
        restore_point_date: datetime.datetime | Unset
        if isinstance(_restore_point_date, Unset):
            restore_point_date = UNSET
        else:
            restore_point_date = isoparse(_restore_point_date)

        operating_system = d.pop("operatingSystem", UNSET)

        operating_system_version = d.pop("operatingSystemVersion", UNSET)

        device_version = d.pop("deviceVersion", UNSET)

        account_enabled = d.pop("accountEnabled", UNSET)

        bit_locker_key_count = d.pop("bitLockerKeyCount", UNSET)

        entra_id_tenant_device_browse_model = cls(
            id=id,
            type_=type_,
            display_name=display_name,
            restore_point_id=restore_point_id,
            restore_point_date=restore_point_date,
            operating_system=operating_system,
            operating_system_version=operating_system_version,
            device_version=device_version,
            account_enabled=account_enabled,
            bit_locker_key_count=bit_locker_key_count,
        )

        entra_id_tenant_device_browse_model.additional_properties = d
        return entra_id_tenant_device_browse_model

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
