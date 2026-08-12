from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_azure_compute_network_security_group_mode import EAzureComputeNetworkSecurityGroupMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureComputeNetworkSecurityGroupModel")


@_attrs_define
class AzureComputeNetworkSecurityGroupModel:
    """Security group settings for the recovered workload.

    Attributes:
        mode (EAzureComputeNetworkSecurityGroupMode): Security group assignment mode for the restored workload.
        id (str | Unset): Azure resource ID of an existing network security group. Required when `mode` is `Existing`.
    """

    mode: EAzureComputeNetworkSecurityGroupMode
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = EAzureComputeNetworkSecurityGroupMode(d.pop("mode"))

        id = d.pop("id", UNSET)

        azure_compute_network_security_group_model = cls(
            mode=mode,
            id=id,
        )

        azure_compute_network_security_group_model.additional_properties = d
        return azure_compute_network_security_group_model

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
