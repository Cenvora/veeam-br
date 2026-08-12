from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_repository_type import ERepositoryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mount_servers_settings_model import MountServersSettingsModel
    from ..models.veeam_data_cloud_storage_account_model import VeeamDataCloudStorageAccountModel
    from ..models.veeam_data_cloud_storage_container_model import VeeamDataCloudStorageContainerModel


T = TypeVar("T", bound="VeeamDataCloudVaultStorageModel")


@_attrs_define
class VeeamDataCloudVaultStorageModel:
    """Veeam Data Cloud Vault.

    Attributes:
        id (UUID): Backup repository ID.
        name (str): Name of the backup repository.
        description (str): Description of the backup repository.
        type_ (ERepositoryType): Repository type.
        account (VeeamDataCloudStorageAccountModel): Veeam Data Cloud Vault account.
        container (VeeamDataCloudStorageContainerModel): Veeam Data Cloud container.
        unique_id (str | Unset): Unique ID that identifies the backup repository.
        mount_server (MountServersSettingsModel | Unset): Mount server settings.
        task_limit_enabled (bool | Unset): If `true`, the maximum number of concurrent tasks is limited.
        max_task_count (int | Unset): Maximum number of concurrent tasks.
    """

    id: UUID
    name: str
    description: str
    type_: ERepositoryType
    account: VeeamDataCloudStorageAccountModel
    container: VeeamDataCloudStorageContainerModel
    unique_id: str | Unset = UNSET
    mount_server: MountServersSettingsModel | Unset = UNSET
    task_limit_enabled: bool | Unset = UNSET
    max_task_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description = self.description

        type_ = self.type_.value

        account = self.account.to_dict()

        container = self.container.to_dict()

        unique_id = self.unique_id

        mount_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mount_server, Unset):
            mount_server = self.mount_server.to_dict()

        task_limit_enabled = self.task_limit_enabled

        max_task_count = self.max_task_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "type": type_,
                "account": account,
                "container": container,
            }
        )
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if mount_server is not UNSET:
            field_dict["mountServer"] = mount_server
        if task_limit_enabled is not UNSET:
            field_dict["taskLimitEnabled"] = task_limit_enabled
        if max_task_count is not UNSET:
            field_dict["maxTaskCount"] = max_task_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mount_servers_settings_model import MountServersSettingsModel
        from ..models.veeam_data_cloud_storage_account_model import VeeamDataCloudStorageAccountModel
        from ..models.veeam_data_cloud_storage_container_model import VeeamDataCloudStorageContainerModel

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        description = d.pop("description")

        type_ = ERepositoryType(d.pop("type"))

        account = VeeamDataCloudStorageAccountModel.from_dict(d.pop("account"))

        container = VeeamDataCloudStorageContainerModel.from_dict(d.pop("container"))

        unique_id = d.pop("uniqueId", UNSET)

        _mount_server = d.pop("mountServer", UNSET)
        mount_server: MountServersSettingsModel | Unset
        if isinstance(_mount_server, Unset):
            mount_server = UNSET
        else:
            mount_server = MountServersSettingsModel.from_dict(_mount_server)

        task_limit_enabled = d.pop("taskLimitEnabled", UNSET)

        max_task_count = d.pop("maxTaskCount", UNSET)

        veeam_data_cloud_vault_storage_model = cls(
            id=id,
            name=name,
            description=description,
            type_=type_,
            account=account,
            container=container,
            unique_id=unique_id,
            mount_server=mount_server,
            task_limit_enabled=task_limit_enabled,
            max_task_count=max_task_count,
        )

        veeam_data_cloud_vault_storage_model.additional_properties = d
        return veeam_data_cloud_vault_storage_model

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
