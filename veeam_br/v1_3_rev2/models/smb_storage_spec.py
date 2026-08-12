from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_repository_type import ERepositoryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mount_servers_settings_model import MountServersSettingsModel
    from ..models.network_repository_settings_model import NetworkRepositorySettingsModel
    from ..models.smb_repository_share_settings_model import SmbRepositoryShareSettingsModel


T = TypeVar("T", bound="SmbStorageSpec")


@_attrs_define
class SmbStorageSpec:
    """SMB backup repository.

    Attributes:
        name (str): Name of the backup repository.
        description (str): Description of the backup repository.
        type_ (ERepositoryType): Repository type.
        share (SmbRepositoryShareSettingsModel): SMB share settings.
        repository (NetworkRepositorySettingsModel): Repository settings.
        unique_id (str | Unset): Unique ID that identifies the backup repository.
        import_backup (bool | Unset): If `true`, Veeam Backup & Replication will search the repository for existing
            backups and import them automatically.
        import_index (bool | Unset): If `true`, Veeam Backup & Replication will import the guest OS file system index.
        mount_server (MountServersSettingsModel | Unset): Mount server settings.
    """

    name: str
    description: str
    type_: ERepositoryType
    share: SmbRepositoryShareSettingsModel
    repository: NetworkRepositorySettingsModel
    unique_id: str | Unset = UNSET
    import_backup: bool | Unset = UNSET
    import_index: bool | Unset = UNSET
    mount_server: MountServersSettingsModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        type_ = self.type_.value

        share = self.share.to_dict()

        repository = self.repository.to_dict()

        unique_id = self.unique_id

        import_backup = self.import_backup

        import_index = self.import_index

        mount_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mount_server, Unset):
            mount_server = self.mount_server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "type": type_,
                "share": share,
                "repository": repository,
            }
        )
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if import_backup is not UNSET:
            field_dict["importBackup"] = import_backup
        if import_index is not UNSET:
            field_dict["importIndex"] = import_index
        if mount_server is not UNSET:
            field_dict["mountServer"] = mount_server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mount_servers_settings_model import MountServersSettingsModel
        from ..models.network_repository_settings_model import NetworkRepositorySettingsModel
        from ..models.smb_repository_share_settings_model import SmbRepositoryShareSettingsModel

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        type_ = ERepositoryType(d.pop("type"))

        share = SmbRepositoryShareSettingsModel.from_dict(d.pop("share"))

        repository = NetworkRepositorySettingsModel.from_dict(d.pop("repository"))

        unique_id = d.pop("uniqueId", UNSET)

        import_backup = d.pop("importBackup", UNSET)

        import_index = d.pop("importIndex", UNSET)

        _mount_server = d.pop("mountServer", UNSET)
        mount_server: MountServersSettingsModel | Unset
        if isinstance(_mount_server, Unset):
            mount_server = UNSET
        else:
            mount_server = MountServersSettingsModel.from_dict(_mount_server)

        smb_storage_spec = cls(
            name=name,
            description=description,
            type_=type_,
            share=share,
            repository=repository,
            unique_id=unique_id,
            import_backup=import_backup,
            import_index=import_index,
            mount_server=mount_server,
        )

        smb_storage_spec.additional_properties = d
        return smb_storage_spec

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
