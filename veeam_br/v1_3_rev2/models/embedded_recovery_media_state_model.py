from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.e_embedded_recovery_media_state import EEmbeddedRecoveryMediaState
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddedRecoveryMediaStateModel")


@_attrs_define
class EmbeddedRecoveryMediaStateModel:
    """Details of Embedded Recovery Media of a host.

    Attributes:
        state (EEmbeddedRecoveryMediaState): State of Embedded Recovery Media.
        last_update_date (datetime.datetime | Unset): Date and time when the Embedded Recovery Media was updated.
        message (str | Unset): Message describing the Embedded Recovery Media state.
    """

    state: EEmbeddedRecoveryMediaState
    last_update_date: datetime.datetime | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if last_update_date is not UNSET:
            field_dict["lastUpdateDate"] = last_update_date
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = EEmbeddedRecoveryMediaState(d.pop("state"))

        _last_update_date = d.pop("lastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        message = d.pop("message", UNSET)

        embedded_recovery_media_state_model = cls(
            state=state,
            last_update_date=last_update_date,
            message=message,
        )

        embedded_recovery_media_state_model.additional_properties = d
        return embedded_recovery_media_state_model

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
