from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_ha_patroni_node_role import EHaPatroniNodeRole
from ..models.e_ha_patroni_node_state import EHaPatroniNodeState
from ..types import UNSET, Unset

T = TypeVar("T", bound="HighAvailabilityClusterNodeModel")


@_attrs_define
class HighAvailabilityClusterNodeModel:
    """High Availability cluster node.

    Attributes:
        id (UUID): Cluster node ID.
        name (str): Patroni node name.
        ip_address (str): Node IP address.
        fqdn (str): Node FQDN.
        role (EHaPatroniNodeRole): Patroni node role.
        state (EHaPatroniNodeState): Patroni node state.
        timeline (str): Patroni timeline.
        lag_mb (int): Lag between secondary and primary nodes in MB.
        external_endpoint (None | str | Unset): External endpoint of the node. Populated in cross-subnet mode.
    """

    id: UUID
    name: str
    ip_address: str
    fqdn: str
    role: EHaPatroniNodeRole
    state: EHaPatroniNodeState
    timeline: str
    lag_mb: int
    external_endpoint: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        ip_address = self.ip_address

        fqdn = self.fqdn

        role = self.role.value

        state = self.state.value

        timeline = self.timeline

        lag_mb = self.lag_mb

        external_endpoint: None | str | Unset
        if isinstance(self.external_endpoint, Unset):
            external_endpoint = UNSET
        else:
            external_endpoint = self.external_endpoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ipAddress": ip_address,
                "fqdn": fqdn,
                "role": role,
                "state": state,
                "timeline": timeline,
                "lagMb": lag_mb,
            }
        )
        if external_endpoint is not UNSET:
            field_dict["externalEndpoint"] = external_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        ip_address = d.pop("ipAddress")

        fqdn = d.pop("fqdn")

        role = EHaPatroniNodeRole(d.pop("role"))

        state = EHaPatroniNodeState(d.pop("state"))

        timeline = d.pop("timeline")

        lag_mb = d.pop("lagMb")

        def _parse_external_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_endpoint = _parse_external_endpoint(d.pop("externalEndpoint", UNSET))

        high_availability_cluster_node_model = cls(
            id=id,
            name=name,
            ip_address=ip_address,
            fqdn=fqdn,
            role=role,
            state=state,
            timeline=timeline,
            lag_mb=lag_mb,
            external_endpoint=external_endpoint,
        )

        high_availability_cluster_node_model.additional_properties = d
        return high_availability_cluster_node_model

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
