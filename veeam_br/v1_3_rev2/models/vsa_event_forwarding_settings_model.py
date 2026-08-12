from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_vsa_event_severity import EVsaEventSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vsa_event_forwarding_filter_model import VsaEventForwardingFilterModel
    from ..models.vsa_event_server_model import VsaEventServerModel


T = TypeVar("T", bound="VsaEventForwardingSettingsModel")


@_attrs_define
class VsaEventForwardingSettingsModel:
    """Infrastructure metrics - VSA Syslog event forwarding settings.

    Attributes:
        enabled (bool): If `true`, metrics forwarding is enabled.
        severity (list[EVsaEventSeverity]): Event levels to include by default.
        advanced_filters (list[VsaEventForwardingFilterModel]): Application and logging level filters.
        use_general_syslog_options (bool | Unset): If `true`, on save the persisted server settings (name, port,
            transport protocol) are overwritten with a snapshot of the backup server's general Syslog options; the inbound
            `server` field is ignored. Reads always return the persisted snapshot. Saving while this flag is true and the
            general Syslog options are disabled results in a 400 response.
        server (VsaEventServerModel | Unset): Infrastructure metrics - VSA Syslog server settings.
    """

    enabled: bool
    severity: list[EVsaEventSeverity]
    advanced_filters: list[VsaEventForwardingFilterModel]
    use_general_syslog_options: bool | Unset = UNSET
    server: VsaEventServerModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        severity = []
        for severity_item_data in self.severity:
            severity_item = severity_item_data.value
            severity.append(severity_item)

        advanced_filters = []
        for advanced_filters_item_data in self.advanced_filters:
            advanced_filters_item = advanced_filters_item_data.to_dict()
            advanced_filters.append(advanced_filters_item)

        use_general_syslog_options = self.use_general_syslog_options

        server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "severity": severity,
                "advancedFilters": advanced_filters,
            }
        )
        if use_general_syslog_options is not UNSET:
            field_dict["useGeneralSyslogOptions"] = use_general_syslog_options
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vsa_event_forwarding_filter_model import VsaEventForwardingFilterModel
        from ..models.vsa_event_server_model import VsaEventServerModel

        d = dict(src_dict)
        enabled = d.pop("enabled")

        severity = []
        _severity = d.pop("severity")
        for severity_item_data in _severity:
            severity_item = EVsaEventSeverity(severity_item_data)

            severity.append(severity_item)

        advanced_filters = []
        _advanced_filters = d.pop("advancedFilters")
        for advanced_filters_item_data in _advanced_filters:
            advanced_filters_item = VsaEventForwardingFilterModel.from_dict(advanced_filters_item_data)

            advanced_filters.append(advanced_filters_item)

        use_general_syslog_options = d.pop("useGeneralSyslogOptions", UNSET)

        _server = d.pop("server", UNSET)
        server: VsaEventServerModel | Unset
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = VsaEventServerModel.from_dict(_server)

        vsa_event_forwarding_settings_model = cls(
            enabled=enabled,
            severity=severity,
            advanced_filters=advanced_filters,
            use_general_syslog_options=use_general_syslog_options,
            server=server,
        )

        vsa_event_forwarding_settings_model.additional_properties = d
        return vsa_event_forwarding_settings_model

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
