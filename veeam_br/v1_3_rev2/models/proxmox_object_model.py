from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_inventory_platform_type import EInventoryPlatformType
from ..models.e_proxmox_inventory_type import EProxmoxInventoryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_acl_info import ObjectAclInfo


T = TypeVar("T", bound="ProxmoxObjectModel")


@_attrs_define
class ProxmoxObjectModel:
    """Proxmox VE object.

    Attributes:
        platform (EInventoryPlatformType): Platform type of inventory object.
        name (str): Proxmox VE object name.
        type_ (EProxmoxInventoryType): Type of Proxmox VE object.
        object_id (str): Proxmox VE object ID.
        size (str | Unset): Object size.
        host_name (str | Unset): Proxmox VE object hostname.
        node_id (str | Unset): Proxmox VE object node ID.
        cluster_id (str | Unset): Proxmox VE object cluster ID.
        acl_info (ObjectAclInfo | Unset): ACL-based object availability information.
    """

    platform: EInventoryPlatformType
    name: str
    type_: EProxmoxInventoryType
    object_id: str
    size: str | Unset = UNSET
    host_name: str | Unset = UNSET
    node_id: str | Unset = UNSET
    cluster_id: str | Unset = UNSET
    acl_info: ObjectAclInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        name = self.name

        type_ = self.type_.value

        object_id = self.object_id

        size = self.size

        host_name = self.host_name

        node_id = self.node_id

        cluster_id = self.cluster_id

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
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if cluster_id is not UNSET:
            field_dict["clusterId"] = cluster_id
        if acl_info is not UNSET:
            field_dict["aclInfo"] = acl_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_acl_info import ObjectAclInfo

        d = dict(src_dict)
        platform = EInventoryPlatformType(d.pop("platform"))

        name = d.pop("name")

        type_ = EProxmoxInventoryType(d.pop("type"))

        object_id = d.pop("objectId")

        size = d.pop("size", UNSET)

        host_name = d.pop("hostName", UNSET)

        node_id = d.pop("nodeId", UNSET)

        cluster_id = d.pop("clusterId", UNSET)

        _acl_info = d.pop("aclInfo", UNSET)
        acl_info: ObjectAclInfo | Unset
        if isinstance(_acl_info, Unset):
            acl_info = UNSET
        else:
            acl_info = ObjectAclInfo.from_dict(_acl_info)

        proxmox_object_model = cls(
            platform=platform,
            name=name,
            type_=type_,
            object_id=object_id,
            size=size,
            host_name=host_name,
            node_id=node_id,
            cluster_id=cluster_id,
            acl_info=acl_info,
        )

        proxmox_object_model.additional_properties = d
        return proxmox_object_model

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
