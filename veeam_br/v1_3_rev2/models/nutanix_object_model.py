from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_inventory_platform_type import EInventoryPlatformType
from ..models.e_nutanix_inventory_type import ENutanixInventoryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_acl_info import ObjectAclInfo


T = TypeVar("T", bound="NutanixObjectModel")


@_attrs_define
class NutanixObjectModel:
    """Nutanix AHV object.

    Attributes:
        platform (EInventoryPlatformType): Platform type of inventory object.
        name (str): Nutanix AHV object name.
        type_ (ENutanixInventoryType): Type of Nutanix AHV object.
        object_id (str): Nutanix AHV object ID.
        size (str | Unset): Object size.
        host_name (str | Unset): Nutanix AHV object hostname.
        cluster_id (str | Unset): Nutanix AHV object cluster ID.
        prism_central_id (str | Unset): Prism Central ID of the Nutanix AHV object.
        acl_info (ObjectAclInfo | Unset): ACL-based object availability information.
    """

    platform: EInventoryPlatformType
    name: str
    type_: ENutanixInventoryType
    object_id: str
    size: str | Unset = UNSET
    host_name: str | Unset = UNSET
    cluster_id: str | Unset = UNSET
    prism_central_id: str | Unset = UNSET
    acl_info: ObjectAclInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        name = self.name

        type_ = self.type_.value

        object_id = self.object_id

        size = self.size

        host_name = self.host_name

        cluster_id = self.cluster_id

        prism_central_id = self.prism_central_id

        acl_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.acl_info, Unset):
            acl_info = self.acl_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "name": name,
                "type": type_,
                "objectId": object_id,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if cluster_id is not UNSET:
            field_dict["clusterId"] = cluster_id
        if prism_central_id is not UNSET:
            field_dict["prismCentralId"] = prism_central_id
        if acl_info is not UNSET:
            field_dict["aclInfo"] = acl_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_acl_info import ObjectAclInfo

        d = dict(src_dict)
        platform = EInventoryPlatformType(d.pop("platform"))

        name = d.pop("name")

        type_ = ENutanixInventoryType(d.pop("type"))

        object_id = d.pop("objectId")

        size = d.pop("size", UNSET)

        host_name = d.pop("hostName", UNSET)

        cluster_id = d.pop("clusterId", UNSET)

        prism_central_id = d.pop("prismCentralId", UNSET)

        _acl_info = d.pop("aclInfo", UNSET)
        acl_info: ObjectAclInfo | Unset
        if isinstance(_acl_info, Unset):
            acl_info = UNSET
        else:
            acl_info = ObjectAclInfo.from_dict(_acl_info)

        nutanix_object_model = cls(
            platform=platform,
            name=name,
            type_=type_,
            object_id=object_id,
            size=size,
            host_name=host_name,
            cluster_id=cluster_id,
            prism_central_id=prism_central_id,
            acl_info=acl_info,
        )

        nutanix_object_model.additional_properties = d
        return nutanix_object_model

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
