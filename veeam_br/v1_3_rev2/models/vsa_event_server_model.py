from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_syslog_server_protocol import ESyslogServerProtocol

T = TypeVar("T", bound="VsaEventServerModel")


@_attrs_define
class VsaEventServerModel:
    """Infrastructure metrics - VSA Syslog server settings.

    Attributes:
        name (str): Full DNS name or IP address of the syslog server.
        port (int): Port on the syslog server used by the specified protocol.
        transport_protocol (ESyslogServerProtocol): Transport mode.
    """

    name: str
    port: int
    transport_protocol: ESyslogServerProtocol
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        port = self.port

        transport_protocol = self.transport_protocol.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "port": port,
                "transportProtocol": transport_protocol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        port = d.pop("port")

        transport_protocol = ESyslogServerProtocol(d.pop("transportProtocol"))

        vsa_event_server_model = cls(
            name=name,
            port=port,
            transport_protocol=transport_protocol,
        )

        vsa_event_server_model.additional_properties = d
        return vsa_event_server_model

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
