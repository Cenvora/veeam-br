from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_acl_rights import EAclRights
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_principal_delegation_model import AclPrincipalDelegationModel
    from ..models.object_owner_model import ObjectOwnerModel


T = TypeVar("T", bound="AclPrincipalModel")


@_attrs_define
class AclPrincipalModel:
    """ACL principal.

    Attributes:
        owner (ObjectOwnerModel): Object owner details.
        rights (list[EAclRights]): ACL rights assigned to the object owner.
        effective_access (list[AclPrincipalDelegationModel] | Unset): Array of delegated rules. Visible only to the
            owner & admin.
    """

    owner: ObjectOwnerModel
    rights: list[EAclRights]
    effective_access: list[AclPrincipalDelegationModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner = self.owner.to_dict()

        rights = []
        for rights_item_data in self.rights:
            rights_item = rights_item_data.value
            rights.append(rights_item)

        effective_access: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.effective_access, Unset):
            effective_access = []
            for effective_access_item_data in self.effective_access:
                effective_access_item = effective_access_item_data.to_dict()
                effective_access.append(effective_access_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "rights": rights,
            }
        )
        if effective_access is not UNSET:
            field_dict["effectiveAccess"] = effective_access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acl_principal_delegation_model import AclPrincipalDelegationModel
        from ..models.object_owner_model import ObjectOwnerModel

        d = dict(src_dict)
        owner = ObjectOwnerModel.from_dict(d.pop("owner"))

        rights = []
        _rights = d.pop("rights")
        for rights_item_data in _rights:
            rights_item = EAclRights(rights_item_data)

            rights.append(rights_item)

        _effective_access = d.pop("effectiveAccess", UNSET)
        effective_access: list[AclPrincipalDelegationModel] | Unset = UNSET
        if _effective_access is not UNSET:
            effective_access = []
            for effective_access_item_data in _effective_access:
                effective_access_item = AclPrincipalDelegationModel.from_dict(effective_access_item_data)

                effective_access.append(effective_access_item)

        acl_principal_model = cls(
            owner=owner,
            rights=rights,
            effective_access=effective_access,
        )

        acl_principal_model.additional_properties = d
        return acl_principal_model

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
