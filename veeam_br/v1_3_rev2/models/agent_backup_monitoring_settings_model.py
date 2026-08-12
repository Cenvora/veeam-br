from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentBackupMonitoringSettingsModel")


@_attrs_define
class AgentBackupMonitoringSettingsModel:
    """Backup monitoring settings. If specified, a warning notification is sent when the agent has not reported any
    successful backups within the specified period.

        Attributes:
            is_enabled (bool): If `true`, a warning notification is sent when the agent has not reported any successful
                backups during the specified period.
            quantity (int | Unset): Number of days without a successful backup after which a warning notification is sent.
                Allowed values: 1–999.
    """

    is_enabled: bool
    quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        quantity = d.pop("quantity", UNSET)

        agent_backup_monitoring_settings_model = cls(
            is_enabled=is_enabled,
            quantity=quantity,
        )

        agent_backup_monitoring_settings_model.additional_properties = d
        return agent_backup_monitoring_settings_model

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
