from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HighAvailabilityClusterAddressSpec")


@_attrs_define
class HighAvailabilityClusterAddressSpec:
    """High Availability cluster address settings.

    Attributes:
        cluster_endpoint (str | Unset): Cluster IP address.
        cluster_dns_name (str | Unset): Cluster DNS name.
        primary_node_external_endpoint (str | Unset): External endpoint of the primary node. Used in cross-subnet mode.
        secondary_node_external_endpoint (str | Unset): External endpoint of the secondary node. Used in cross-subnet
            mode.
    """

    cluster_endpoint: str | Unset = UNSET
    cluster_dns_name: str | Unset = UNSET
    primary_node_external_endpoint: str | Unset = UNSET
    secondary_node_external_endpoint: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_endpoint = self.cluster_endpoint

        cluster_dns_name = self.cluster_dns_name

        primary_node_external_endpoint = self.primary_node_external_endpoint

        secondary_node_external_endpoint = self.secondary_node_external_endpoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_endpoint is not UNSET:
            field_dict["clusterEndpoint"] = cluster_endpoint
        if cluster_dns_name is not UNSET:
            field_dict["clusterDnsName"] = cluster_dns_name
        if primary_node_external_endpoint is not UNSET:
            field_dict["primaryNodeExternalEndpoint"] = primary_node_external_endpoint
        if secondary_node_external_endpoint is not UNSET:
            field_dict["secondaryNodeExternalEndpoint"] = secondary_node_external_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_endpoint = d.pop("clusterEndpoint", UNSET)

        cluster_dns_name = d.pop("clusterDnsName", UNSET)

        primary_node_external_endpoint = d.pop("primaryNodeExternalEndpoint", UNSET)

        secondary_node_external_endpoint = d.pop("secondaryNodeExternalEndpoint", UNSET)

        high_availability_cluster_address_spec = cls(
            cluster_endpoint=cluster_endpoint,
            cluster_dns_name=cluster_dns_name,
            primary_node_external_endpoint=primary_node_external_endpoint,
            secondary_node_external_endpoint=secondary_node_external_endpoint,
        )

        high_availability_cluster_address_spec.additional_properties = d
        return high_availability_cluster_address_spec

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
