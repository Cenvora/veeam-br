from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ha_certificate_upload_spec import HaCertificateUploadSpec


T = TypeVar("T", bound="HighAvailabilityClusterSpec")


@_attrs_define
class HighAvailabilityClusterSpec:
    """High Availability cluster settings.

    Attributes:
        primary_node_ip_address (str): Primary node IP address.
        secondary_node_ip_address (str): Secondary node IP address.
        secondary_node_credentials_id (UUID): Secondary node credentials ID.
        cluster_dns_name (str): Cluster DNS name.
        certificate (HaCertificateUploadSpec): PEM certificate settings for the HA cluster.
        cluster_endpoint (str | Unset): Cluster IP address.
        is_cross_subnet_mode (bool | Unset): If `true`, the cluster is created in cross-subnet mode.
        primary_node_external_endpoint (str | Unset): External endpoint of the primary node. Required when
            `isCrossSubnetMode` is `true`.
        secondary_node_external_endpoint (str | Unset): External endpoint of the secondary node. Required when
            `isCrossSubnetMode` is `true`.
    """

    primary_node_ip_address: str
    secondary_node_ip_address: str
    secondary_node_credentials_id: UUID
    cluster_dns_name: str
    certificate: HaCertificateUploadSpec
    cluster_endpoint: str | Unset = UNSET
    is_cross_subnet_mode: bool | Unset = UNSET
    primary_node_external_endpoint: str | Unset = UNSET
    secondary_node_external_endpoint: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary_node_ip_address = self.primary_node_ip_address

        secondary_node_ip_address = self.secondary_node_ip_address

        secondary_node_credentials_id = str(self.secondary_node_credentials_id)

        cluster_dns_name = self.cluster_dns_name

        certificate = self.certificate.to_dict()

        cluster_endpoint = self.cluster_endpoint

        is_cross_subnet_mode = self.is_cross_subnet_mode

        primary_node_external_endpoint = self.primary_node_external_endpoint

        secondary_node_external_endpoint = self.secondary_node_external_endpoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "primaryNodeIpAddress": primary_node_ip_address,
                "secondaryNodeIpAddress": secondary_node_ip_address,
                "secondaryNodeCredentialsId": secondary_node_credentials_id,
                "clusterDnsName": cluster_dns_name,
                "certificate": certificate,
            }
        )
        if cluster_endpoint is not UNSET:
            field_dict["clusterEndpoint"] = cluster_endpoint
        if is_cross_subnet_mode is not UNSET:
            field_dict["isCrossSubnetMode"] = is_cross_subnet_mode
        if primary_node_external_endpoint is not UNSET:
            field_dict["primaryNodeExternalEndpoint"] = primary_node_external_endpoint
        if secondary_node_external_endpoint is not UNSET:
            field_dict["secondaryNodeExternalEndpoint"] = secondary_node_external_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ha_certificate_upload_spec import HaCertificateUploadSpec

        d = dict(src_dict)
        primary_node_ip_address = d.pop("primaryNodeIpAddress")

        secondary_node_ip_address = d.pop("secondaryNodeIpAddress")

        secondary_node_credentials_id = UUID(d.pop("secondaryNodeCredentialsId"))

        cluster_dns_name = d.pop("clusterDnsName")

        certificate = HaCertificateUploadSpec.from_dict(d.pop("certificate"))

        cluster_endpoint = d.pop("clusterEndpoint", UNSET)

        is_cross_subnet_mode = d.pop("isCrossSubnetMode", UNSET)

        primary_node_external_endpoint = d.pop("primaryNodeExternalEndpoint", UNSET)

        secondary_node_external_endpoint = d.pop("secondaryNodeExternalEndpoint", UNSET)

        high_availability_cluster_spec = cls(
            primary_node_ip_address=primary_node_ip_address,
            secondary_node_ip_address=secondary_node_ip_address,
            secondary_node_credentials_id=secondary_node_credentials_id,
            cluster_dns_name=cluster_dns_name,
            certificate=certificate,
            cluster_endpoint=cluster_endpoint,
            is_cross_subnet_mode=is_cross_subnet_mode,
            primary_node_external_endpoint=primary_node_external_endpoint,
            secondary_node_external_endpoint=secondary_node_external_endpoint,
        )

        high_availability_cluster_spec.additional_properties = d
        return high_availability_cluster_spec

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
