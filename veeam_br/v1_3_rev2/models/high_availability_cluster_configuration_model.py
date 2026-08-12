from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.high_availability_cluster_node_model import HighAvailabilityClusterNodeModel
    from ..models.high_availability_cluster_states_model import HighAvailabilityClusterStatesModel


T = TypeVar("T", bound="HighAvailabilityClusterConfigurationModel")


@_attrs_define
class HighAvailabilityClusterConfigurationModel:
    """High Availability cluster configuration.

    Attributes:
        id (UUID): High Availability cluster ID.
        primary_node (HighAvailabilityClusterNodeModel): High Availability cluster node.
        secondary_node (HighAvailabilityClusterNodeModel): High Availability cluster node.
        name (str): Patroni cluster name.
        cluster_endpoint (str): Cluster IP address.
        cluster_dns_name (str): Cluster DNS name.
        is_cross_subnet_mode (bool): If `true`, the cluster is in cross-subnet mode.
        states (HighAvailabilityClusterStatesModel | Unset): High Availability cluster states.
    """

    id: UUID
    primary_node: HighAvailabilityClusterNodeModel
    secondary_node: HighAvailabilityClusterNodeModel
    name: str
    cluster_endpoint: str
    cluster_dns_name: str
    is_cross_subnet_mode: bool
    states: HighAvailabilityClusterStatesModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        primary_node = self.primary_node.to_dict()

        secondary_node = self.secondary_node.to_dict()

        name = self.name

        cluster_endpoint = self.cluster_endpoint

        cluster_dns_name = self.cluster_dns_name

        is_cross_subnet_mode = self.is_cross_subnet_mode

        states: dict[str, Any] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = self.states.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "primaryNode": primary_node,
                "secondaryNode": secondary_node,
                "name": name,
                "clusterEndpoint": cluster_endpoint,
                "clusterDnsName": cluster_dns_name,
                "isCrossSubnetMode": is_cross_subnet_mode,
            }
        )
        if states is not UNSET:
            field_dict["states"] = states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.high_availability_cluster_node_model import HighAvailabilityClusterNodeModel
        from ..models.high_availability_cluster_states_model import HighAvailabilityClusterStatesModel

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        primary_node = HighAvailabilityClusterNodeModel.from_dict(d.pop("primaryNode"))

        secondary_node = HighAvailabilityClusterNodeModel.from_dict(d.pop("secondaryNode"))

        name = d.pop("name")

        cluster_endpoint = d.pop("clusterEndpoint")

        cluster_dns_name = d.pop("clusterDnsName")

        is_cross_subnet_mode = d.pop("isCrossSubnetMode")

        _states = d.pop("states", UNSET)
        states: HighAvailabilityClusterStatesModel | Unset
        if isinstance(_states, Unset):
            states = UNSET
        else:
            states = HighAvailabilityClusterStatesModel.from_dict(_states)

        high_availability_cluster_configuration_model = cls(
            id=id,
            primary_node=primary_node,
            secondary_node=secondary_node,
            name=name,
            cluster_endpoint=cluster_endpoint,
            cluster_dns_name=cluster_dns_name,
            is_cross_subnet_mode=is_cross_subnet_mode,
            states=states,
        )

        high_availability_cluster_configuration_model.additional_properties = d
        return high_availability_cluster_configuration_model

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
