from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_server_settings_model import GatewayServerSettingsModel


T = TypeVar("T", bound="HPEStoreOnceStorageSettingsModel")


@_attrs_define
class HPEStoreOnceStorageSettingsModel:
    """HPE StoreOnce storage settings.

    Attributes:
        store_once_server_name (str): HPE StoreOnce server name.
        credentials_id (UUID): ID of the credentials record used to connect to the HPE StoreOnce server.
        use_fc_connectivity (bool | Unset): If `true`, Fibre Channel (FC) connectivity is used to connect to the
            storage. Default: False.
        gateway_server (GatewayServerSettingsModel | Unset): Gateway server settings.
        use_store_once_wan_link (bool | Unset): If `true`, the StoreOnce appliance is connected over a low-bandwidth WAN
            link. Default: False.
    """

    store_once_server_name: str
    credentials_id: UUID
    use_fc_connectivity: bool | Unset = False
    gateway_server: GatewayServerSettingsModel | Unset = UNSET
    use_store_once_wan_link: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        store_once_server_name = self.store_once_server_name

        credentials_id = str(self.credentials_id)

        use_fc_connectivity = self.use_fc_connectivity

        gateway_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gateway_server, Unset):
            gateway_server = self.gateway_server.to_dict()

        use_store_once_wan_link = self.use_store_once_wan_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storeOnceServerName": store_once_server_name,
                "credentialsId": credentials_id,
            }
        )
        if use_fc_connectivity is not UNSET:
            field_dict["useFCConnectivity"] = use_fc_connectivity
        if gateway_server is not UNSET:
            field_dict["gatewayServer"] = gateway_server
        if use_store_once_wan_link is not UNSET:
            field_dict["useStoreOnceWanLink"] = use_store_once_wan_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_server_settings_model import GatewayServerSettingsModel

        d = dict(src_dict)
        store_once_server_name = d.pop("storeOnceServerName")

        credentials_id = UUID(d.pop("credentialsId"))

        use_fc_connectivity = d.pop("useFCConnectivity", UNSET)

        _gateway_server = d.pop("gatewayServer", UNSET)
        gateway_server: GatewayServerSettingsModel | Unset
        if isinstance(_gateway_server, Unset):
            gateway_server = UNSET
        else:
            gateway_server = GatewayServerSettingsModel.from_dict(_gateway_server)

        use_store_once_wan_link = d.pop("useStoreOnceWanLink", UNSET)

        hpe_store_once_storage_settings_model = cls(
            store_once_server_name=store_once_server_name,
            credentials_id=credentials_id,
            use_fc_connectivity=use_fc_connectivity,
            gateway_server=gateway_server,
            use_store_once_wan_link=use_store_once_wan_link,
        )

        hpe_store_once_storage_settings_model.additional_properties = d
        return hpe_store_once_storage_settings_model

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
