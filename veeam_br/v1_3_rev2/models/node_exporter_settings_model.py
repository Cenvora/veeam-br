from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node_exporter_authentication_model import NodeExporterAuthenticationModel


T = TypeVar("T", bound="NodeExporterSettingsModel")


@_attrs_define
class NodeExporterSettingsModel:
    """Node Exporter settings.

    Attributes:
        metrics_sharing_enabled (bool): If `true`, metrics sharing is enabled.
        tls_enabled (bool): If `true`, the secured connection over TLS is enabled.
        auth (NodeExporterAuthenticationModel): Node Exporter authentication.
    """

    metrics_sharing_enabled: bool
    tls_enabled: bool
    auth: NodeExporterAuthenticationModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metrics_sharing_enabled = self.metrics_sharing_enabled

        tls_enabled = self.tls_enabled

        auth = self.auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metricsSharingEnabled": metrics_sharing_enabled,
                "tlsEnabled": tls_enabled,
                "auth": auth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_exporter_authentication_model import NodeExporterAuthenticationModel

        d = dict(src_dict)
        metrics_sharing_enabled = d.pop("metricsSharingEnabled")

        tls_enabled = d.pop("tlsEnabled")

        auth = NodeExporterAuthenticationModel.from_dict(d.pop("auth"))

        node_exporter_settings_model = cls(
            metrics_sharing_enabled=metrics_sharing_enabled,
            tls_enabled=tls_enabled,
            auth=auth,
        )

        node_exporter_settings_model.additional_properties = d
        return node_exporter_settings_model

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
