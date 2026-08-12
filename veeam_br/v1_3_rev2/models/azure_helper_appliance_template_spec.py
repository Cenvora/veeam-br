from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_compute_vm_tag_model import AzureComputeVMTagModel


T = TypeVar("T", bound="AzureHelperApplianceTemplateSpec")


@_attrs_define
class AzureHelperApplianceTemplateSpec:
    """Azure helper appliance template.

    Attributes:
        subscription_id (UUID): Azure subscription ID.
        location (str): Azure region where the helper appliance template is deployed.
        resource_group (str | Unset): Name of the Azure resource group.
        storage_account_name (str | Unset): Name of the Azure storage account.
        virtual_network_id (str | Unset): ID of the Azure virtual network.
        subnet_id (str | Unset): ID of the Azure subnet.
        tags (list[AzureComputeVMTagModel] | Unset): Array of Azure tags assigned to the helper appliance.
    """

    subscription_id: UUID
    location: str
    resource_group: str | Unset = UNSET
    storage_account_name: str | Unset = UNSET
    virtual_network_id: str | Unset = UNSET
    subnet_id: str | Unset = UNSET
    tags: list[AzureComputeVMTagModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id = str(self.subscription_id)

        location = self.location

        resource_group = self.resource_group

        storage_account_name = self.storage_account_name

        virtual_network_id = self.virtual_network_id

        subnet_id = self.subnet_id

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionId": subscription_id,
                "location": location,
            }
        )
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if storage_account_name is not UNSET:
            field_dict["storageAccountName"] = storage_account_name
        if virtual_network_id is not UNSET:
            field_dict["virtualNetworkId"] = virtual_network_id
        if subnet_id is not UNSET:
            field_dict["subnetId"] = subnet_id
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_compute_vm_tag_model import AzureComputeVMTagModel

        d = dict(src_dict)
        subscription_id = UUID(d.pop("subscriptionId"))

        location = d.pop("location")

        resource_group = d.pop("resourceGroup", UNSET)

        storage_account_name = d.pop("storageAccountName", UNSET)

        virtual_network_id = d.pop("virtualNetworkId", UNSET)

        subnet_id = d.pop("subnetId", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[AzureComputeVMTagModel] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = AzureComputeVMTagModel.from_dict(tags_item_data)

                tags.append(tags_item)

        azure_helper_appliance_template_spec = cls(
            subscription_id=subscription_id,
            location=location,
            resource_group=resource_group,
            storage_account_name=storage_account_name,
            virtual_network_id=virtual_network_id,
            subnet_id=subnet_id,
            tags=tags,
        )

        azure_helper_appliance_template_spec.additional_properties = d
        return azure_helper_appliance_template_spec

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
