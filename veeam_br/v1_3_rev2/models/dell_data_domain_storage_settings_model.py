from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edd_boost_encryption_type import EDDBoostEncryptionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_server_settings_model import GatewayServerSettingsModel


T = TypeVar("T", bound="DellDataDomainStorageSettingsModel")


@_attrs_define
class DellDataDomainStorageSettingsModel:
    """Dell Data Domain storage settings.

    Attributes:
        credentials_id (UUID): ID of the credentials record used to connect to the Dell Data Domain server.
        dd_servername (str | Unset): Dell Data Domain server name.
        use_fc_connectivity (bool | Unset): If `true`, Fibre Channel (FC) connectivity is used to connect to the
            storage. Default: False.
        gateway_server (GatewayServerSettingsModel | Unset): Gateway server settings.
        dd_boost_encryption_enabled (bool | Unset): If `true`, DD Boost in-flight encryption is enabled. Default: False.
        dd_boost_encryption_type (EDDBoostEncryptionType | Unset): Dell Data Domain Boost encryption type.
    """

    credentials_id: UUID
    dd_servername: str | Unset = UNSET
    use_fc_connectivity: bool | Unset = False
    gateway_server: GatewayServerSettingsModel | Unset = UNSET
    dd_boost_encryption_enabled: bool | Unset = False
    dd_boost_encryption_type: EDDBoostEncryptionType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials_id = str(self.credentials_id)

        dd_servername = self.dd_servername

        use_fc_connectivity = self.use_fc_connectivity

        gateway_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gateway_server, Unset):
            gateway_server = self.gateway_server.to_dict()

        dd_boost_encryption_enabled = self.dd_boost_encryption_enabled

        dd_boost_encryption_type: str | Unset = UNSET
        if not isinstance(self.dd_boost_encryption_type, Unset):
            dd_boost_encryption_type = self.dd_boost_encryption_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialsId": credentials_id,
            }
        )
        if dd_servername is not UNSET:
            field_dict["ddServername"] = dd_servername
        if use_fc_connectivity is not UNSET:
            field_dict["useFCConnectivity"] = use_fc_connectivity
        if gateway_server is not UNSET:
            field_dict["gatewayServer"] = gateway_server
        if dd_boost_encryption_enabled is not UNSET:
            field_dict["ddBoostEncryptionEnabled"] = dd_boost_encryption_enabled
        if dd_boost_encryption_type is not UNSET:
            field_dict["ddBoostEncryptionType"] = dd_boost_encryption_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_server_settings_model import GatewayServerSettingsModel

        d = dict(src_dict)
        credentials_id = UUID(d.pop("credentialsId"))

        dd_servername = d.pop("ddServername", UNSET)

        use_fc_connectivity = d.pop("useFCConnectivity", UNSET)

        _gateway_server = d.pop("gatewayServer", UNSET)
        gateway_server: GatewayServerSettingsModel | Unset
        if isinstance(_gateway_server, Unset):
            gateway_server = UNSET
        else:
            gateway_server = GatewayServerSettingsModel.from_dict(_gateway_server)

        dd_boost_encryption_enabled = d.pop("ddBoostEncryptionEnabled", UNSET)

        _dd_boost_encryption_type = d.pop("ddBoostEncryptionType", UNSET)
        dd_boost_encryption_type: EDDBoostEncryptionType | Unset
        if isinstance(_dd_boost_encryption_type, Unset):
            dd_boost_encryption_type = UNSET
        else:
            dd_boost_encryption_type = EDDBoostEncryptionType(_dd_boost_encryption_type)

        dell_data_domain_storage_settings_model = cls(
            credentials_id=credentials_id,
            dd_servername=dd_servername,
            use_fc_connectivity=use_fc_connectivity,
            gateway_server=gateway_server,
            dd_boost_encryption_enabled=dd_boost_encryption_enabled,
            dd_boost_encryption_type=dd_boost_encryption_type,
        )

        dell_data_domain_storage_settings_model.additional_properties = d
        return dell_data_domain_storage_settings_model

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
