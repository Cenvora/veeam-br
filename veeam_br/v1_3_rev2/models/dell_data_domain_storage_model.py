from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_repository_type import ERepositoryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dell_data_domain_repository_settings_model import DellDataDomainRepositorySettingsModel
    from ..models.dell_data_domain_storage_settings_model import DellDataDomainStorageSettingsModel
    from ..models.mount_servers_settings_model import MountServersSettingsModel


T = TypeVar("T", bound="DellDataDomainStorageModel")


@_attrs_define
class DellDataDomainStorageModel:
    """Dell Data Domain deduplication appliance repository.

    Attributes:
        id (UUID): Backup repository ID.
        name (str): Name of the backup repository.
        description (str): Description of the backup repository.
        type_ (ERepositoryType): Repository type.
        dell_data_domain (DellDataDomainStorageSettingsModel): Dell Data Domain storage settings.
        repository (DellDataDomainRepositorySettingsModel): Dell Data Domain repository settings.
        unique_id (str | Unset): Unique ID that identifies the backup repository.
        mount_servers (MountServersSettingsModel | Unset): Mount server settings.
    """

    id: UUID
    name: str
    description: str
    type_: ERepositoryType
    dell_data_domain: DellDataDomainStorageSettingsModel
    repository: DellDataDomainRepositorySettingsModel
    unique_id: str | Unset = UNSET
    mount_servers: MountServersSettingsModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description = self.description

        type_ = self.type_.value

        dell_data_domain = self.dell_data_domain.to_dict()

        repository = self.repository.to_dict()

        unique_id = self.unique_id

        mount_servers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mount_servers, Unset):
            mount_servers = self.mount_servers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "type": type_,
                "dellDataDomain": dell_data_domain,
                "repository": repository,
            }
        )
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if mount_servers is not UNSET:
            field_dict["mountServers"] = mount_servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dell_data_domain_repository_settings_model import DellDataDomainRepositorySettingsModel
        from ..models.dell_data_domain_storage_settings_model import DellDataDomainStorageSettingsModel
        from ..models.mount_servers_settings_model import MountServersSettingsModel

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        description = d.pop("description")

        type_ = ERepositoryType(d.pop("type"))

        dell_data_domain = DellDataDomainStorageSettingsModel.from_dict(d.pop("dellDataDomain"))

        repository = DellDataDomainRepositorySettingsModel.from_dict(d.pop("repository"))

        unique_id = d.pop("uniqueId", UNSET)

        _mount_servers = d.pop("mountServers", UNSET)
        mount_servers: MountServersSettingsModel | Unset
        if isinstance(_mount_servers, Unset):
            mount_servers = UNSET
        else:
            mount_servers = MountServersSettingsModel.from_dict(_mount_servers)

        dell_data_domain_storage_model = cls(
            id=id,
            name=name,
            description=description,
            type_=type_,
            dell_data_domain=dell_data_domain,
            repository=repository,
            unique_id=unique_id,
            mount_servers=mount_servers,
        )

        dell_data_domain_storage_model.additional_properties = d
        return dell_data_domain_storage_model

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
