from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_cold_storage_retrieval_mode import EColdStorageRetrievalMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredDataColdStorageRetrievalSettings")


@_attrs_define
class UnstructuredDataColdStorageRetrievalSettings:
    """Settings for retrieving data from cold storage.

    Attributes:
        cold_storage_retrieval_mode (EColdStorageRetrievalMode | Unset): Cold Storage retrieval mode.
        availability_period_days (int | Unset): Number of days the retrieved files must be kept available. If no value
            is specified, the availability period is not extended, and the files remain available only for as long as the
            operation that retrieved them requires.
        send_notification_mail (bool | Unset): If `true`, a notification email is sent when the retrieval is about to
            expire. Default: False.
        notification_hours (int | Unset): Notification threshold, in hours. The expiration notification email is sent
            when the retrieved files have this many hours left before they become unavailable. Applies only if
            `sendNotificationMail` is `true`.
    """

    cold_storage_retrieval_mode: EColdStorageRetrievalMode | Unset = UNSET
    availability_period_days: int | Unset = UNSET
    send_notification_mail: bool | Unset = False
    notification_hours: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cold_storage_retrieval_mode: str | Unset = UNSET
        if not isinstance(self.cold_storage_retrieval_mode, Unset):
            cold_storage_retrieval_mode = self.cold_storage_retrieval_mode.value

        availability_period_days = self.availability_period_days

        send_notification_mail = self.send_notification_mail

        notification_hours = self.notification_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cold_storage_retrieval_mode is not UNSET:
            field_dict["coldStorageRetrievalMode"] = cold_storage_retrieval_mode
        if availability_period_days is not UNSET:
            field_dict["availabilityPeriodDays"] = availability_period_days
        if send_notification_mail is not UNSET:
            field_dict["sendNotificationMail"] = send_notification_mail
        if notification_hours is not UNSET:
            field_dict["notificationHours"] = notification_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _cold_storage_retrieval_mode = d.pop("coldStorageRetrievalMode", UNSET)
        cold_storage_retrieval_mode: EColdStorageRetrievalMode | Unset
        if isinstance(_cold_storage_retrieval_mode, Unset):
            cold_storage_retrieval_mode = UNSET
        else:
            cold_storage_retrieval_mode = EColdStorageRetrievalMode(_cold_storage_retrieval_mode)

        availability_period_days = d.pop("availabilityPeriodDays", UNSET)

        send_notification_mail = d.pop("sendNotificationMail", UNSET)

        notification_hours = d.pop("notificationHours", UNSET)

        unstructured_data_cold_storage_retrieval_settings = cls(
            cold_storage_retrieval_mode=cold_storage_retrieval_mode,
            availability_period_days=availability_period_days,
            send_notification_mail=send_notification_mail,
            notification_hours=notification_hours,
        )

        unstructured_data_cold_storage_retrieval_settings.additional_properties = d
        return unstructured_data_cold_storage_retrieval_settings

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
