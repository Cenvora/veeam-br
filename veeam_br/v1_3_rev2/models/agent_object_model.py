from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_agent_inventory_object_type import EAgentInventoryObjectType
from ..models.e_cloud_machines_type import ECloudMachinesType
from ..models.e_inventory_platform_type import EInventoryPlatformType
from ..models.e_protection_group_type import EProtectionGroupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_acl_info import ObjectAclInfo


T = TypeVar("T", bound="AgentObjectModel")


@_attrs_define
class AgentObjectModel:
    """Agent-managed object.

    Attributes:
        platform (EInventoryPlatformType): Platform type of inventory object.
        id (UUID): ID of agent-managed object.
        name (str): Name of agent-managed object.
        type_ (EAgentInventoryObjectType): Type of agent-managed object.
        protection_group_id (UUID): Protection group ID.
        size (str | Unset): Object size.
        path (str | Unset): Path of installed agent.
        parent_object_id (UUID | Unset): Parent object ID.
        protection_group_type (EProtectionGroupType | Unset): Protection group type
        cloud_machines_type (ECloudMachinesType | Unset): Cloud platform of a CloudMachines protection group. Populated
            only when `protectionGroupType` is `CloudMachines`.
        acl_info (ObjectAclInfo | Unset): ACL-based object availability information.
    """

    platform: EInventoryPlatformType
    id: UUID
    name: str
    type_: EAgentInventoryObjectType
    protection_group_id: UUID
    size: str | Unset = UNSET
    path: str | Unset = UNSET
    parent_object_id: UUID | Unset = UNSET
    protection_group_type: EProtectionGroupType | Unset = UNSET
    cloud_machines_type: ECloudMachinesType | Unset = UNSET
    acl_info: ObjectAclInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        id = str(self.id)

        name = self.name

        type_ = self.type_.value

        protection_group_id = str(self.protection_group_id)

        size = self.size

        path = self.path

        parent_object_id: str | Unset = UNSET
        if not isinstance(self.parent_object_id, Unset):
            parent_object_id = str(self.parent_object_id)

        protection_group_type: str | Unset = UNSET
        if not isinstance(self.protection_group_type, Unset):
            protection_group_type = self.protection_group_type.value

        cloud_machines_type: str | Unset = UNSET
        if not isinstance(self.cloud_machines_type, Unset):
            cloud_machines_type = self.cloud_machines_type.value

        acl_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.acl_info, Unset):
            acl_info = self.acl_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "id": id,
                "name": name,
                "type": type_,
                "protectionGroupId": protection_group_id,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if path is not UNSET:
            field_dict["path"] = path
        if parent_object_id is not UNSET:
            field_dict["parentObjectId"] = parent_object_id
        if protection_group_type is not UNSET:
            field_dict["protectionGroupType"] = protection_group_type
        if cloud_machines_type is not UNSET:
            field_dict["cloudMachinesType"] = cloud_machines_type
        if acl_info is not UNSET:
            field_dict["aclInfo"] = acl_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_acl_info import ObjectAclInfo

        d = dict(src_dict)
        platform = EInventoryPlatformType(d.pop("platform"))

        id = UUID(d.pop("id"))

        name = d.pop("name")

        type_ = EAgentInventoryObjectType(d.pop("type"))

        protection_group_id = UUID(d.pop("protectionGroupId"))

        size = d.pop("size", UNSET)

        path = d.pop("path", UNSET)

        _parent_object_id = d.pop("parentObjectId", UNSET)
        parent_object_id: UUID | Unset
        if isinstance(_parent_object_id, Unset):
            parent_object_id = UNSET
        else:
            parent_object_id = UUID(_parent_object_id)

        _protection_group_type = d.pop("protectionGroupType", UNSET)
        protection_group_type: EProtectionGroupType | Unset
        if isinstance(_protection_group_type, Unset):
            protection_group_type = UNSET
        else:
            protection_group_type = EProtectionGroupType(_protection_group_type)

        _cloud_machines_type = d.pop("cloudMachinesType", UNSET)
        cloud_machines_type: ECloudMachinesType | Unset
        if isinstance(_cloud_machines_type, Unset):
            cloud_machines_type = UNSET
        else:
            cloud_machines_type = ECloudMachinesType(_cloud_machines_type)

        _acl_info = d.pop("aclInfo", UNSET)
        acl_info: ObjectAclInfo | Unset
        if isinstance(_acl_info, Unset):
            acl_info = UNSET
        else:
            acl_info = ObjectAclInfo.from_dict(_acl_info)

        agent_object_model = cls(
            platform=platform,
            id=id,
            name=name,
            type_=type_,
            protection_group_id=protection_group_id,
            size=size,
            path=path,
            parent_object_id=parent_object_id,
            protection_group_type=protection_group_type,
            cloud_machines_type=cloud_machines_type,
            acl_info=acl_info,
        )

        agent_object_model.additional_properties = d
        return agent_object_model

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
