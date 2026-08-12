from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_protection_group_type import EProtectionGroupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.individual_computer_container_model import IndividualComputerContainerModel
    from ..models.protection_group_options_model import ProtectionGroupOptionsModel


T = TypeVar("T", bound="IrisProtectionGroupModel")


@_attrs_define
class IrisProtectionGroupModel:
    """Protection group for InterSystems IRIS.

    Attributes:
        id (UUID): Protection group ID.
        name (str): Protection group name.
        description (str): Protection group description.
        type_ (EProtectionGroupType): Protection group type
        servers (list[IndividualComputerContainerModel]): Array of InterSystems IRIS servers in the protection group.
        is_disabled (bool | Unset): If `true`, the protection group is disabled
        options (ProtectionGroupOptionsModel | Unset): Protection group options.
    """

    id: UUID
    name: str
    description: str
    type_: EProtectionGroupType
    servers: list[IndividualComputerContainerModel]
    is_disabled: bool | Unset = UNSET
    options: ProtectionGroupOptionsModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description = self.description

        type_ = self.type_.value

        servers = []
        for servers_item_data in self.servers:
            servers_item = servers_item_data.to_dict()
            servers.append(servers_item)

        is_disabled = self.is_disabled

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "type": type_,
                "servers": servers,
            }
        )
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.individual_computer_container_model import IndividualComputerContainerModel
        from ..models.protection_group_options_model import ProtectionGroupOptionsModel

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        description = d.pop("description")

        type_ = EProtectionGroupType(d.pop("type"))

        servers = []
        _servers = d.pop("servers")
        for servers_item_data in _servers:
            servers_item = IndividualComputerContainerModel.from_dict(servers_item_data)

            servers.append(servers_item)

        is_disabled = d.pop("isDisabled", UNSET)

        _options = d.pop("options", UNSET)
        options: ProtectionGroupOptionsModel | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = ProtectionGroupOptionsModel.from_dict(_options)

        iris_protection_group_model = cls(
            id=id,
            name=name,
            description=description,
            type_=type_,
            servers=servers,
            is_disabled=is_disabled,
            options=options,
        )

        iris_protection_group_model.additional_properties = d
        return iris_protection_group_model

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
