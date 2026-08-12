from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.acl_principal_delegation_model import AclPrincipalDelegationModel


T = TypeVar("T", bound="AclChangeEffectiveAccessSpec")


@_attrs_define
class AclChangeEffectiveAccessSpec:
    """Settings for changing effective access.

    Attributes:
        effective_access (list[AclPrincipalDelegationModel]): Array of delegated rules. Visible only to the owner &
            admin.
    """

    effective_access: list[AclPrincipalDelegationModel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_access = []
        for effective_access_item_data in self.effective_access:
            effective_access_item = effective_access_item_data.to_dict()
            effective_access.append(effective_access_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effectiveAccess": effective_access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acl_principal_delegation_model import AclPrincipalDelegationModel

        d = dict(src_dict)
        effective_access = []
        _effective_access = d.pop("effectiveAccess")
        for effective_access_item_data in _effective_access:
            effective_access_item = AclPrincipalDelegationModel.from_dict(effective_access_item_data)

            effective_access.append(effective_access_item)

        acl_change_effective_access_spec = cls(
            effective_access=effective_access,
        )

        acl_change_effective_access_spec.additional_properties = d
        return acl_change_effective_access_spec

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
