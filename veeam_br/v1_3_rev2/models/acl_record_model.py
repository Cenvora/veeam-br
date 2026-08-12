from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.acl_object_model import AclObjectModel
    from ..models.acl_principal_model import AclPrincipalModel


T = TypeVar("T", bound="AclRecordModel")


@_attrs_define
class AclRecordModel:
    """ACL record. Contains the resource and its ACL settings.

    Attributes:
        object_ (AclObjectModel): ACL object.
        principal (AclPrincipalModel): ACL principal.
    """

    object_: AclObjectModel
    principal: AclPrincipalModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.to_dict()

        principal = self.principal.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "principal": principal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acl_object_model import AclObjectModel
        from ..models.acl_principal_model import AclPrincipalModel

        d = dict(src_dict)
        object_ = AclObjectModel.from_dict(d.pop("object"))

        principal = AclPrincipalModel.from_dict(d.pop("principal"))

        acl_record_model = cls(
            object_=object_,
            principal=principal,
        )

        acl_record_model.additional_properties = d
        return acl_record_model

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
