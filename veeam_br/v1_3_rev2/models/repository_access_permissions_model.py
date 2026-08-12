from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_repository_access_type import ERepositoryAccessType

if TYPE_CHECKING:
    from ..models.backup_storage_settings_encryption_model import BackupStorageSettingsEncryptionModel
    from ..models.repository_access_account_model import RepositoryAccessAccountModel


T = TypeVar("T", bound="RepositoryAccessPermissionsModel")


@_attrs_define
class RepositoryAccessPermissionsModel:
    """Repository access permissions.

    Attributes:
        access_policy (ERepositoryAccessType): Access type.
        accounts (list[RepositoryAccessAccountModel]): (For *AllowExplicit* access policy) Array of accounts that have
            access to the backup repository.
        encryption_settings (BackupStorageSettingsEncryptionModel): Encryption of backup files.
    """

    access_policy: ERepositoryAccessType
    accounts: list[RepositoryAccessAccountModel]
    encryption_settings: BackupStorageSettingsEncryptionModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_policy = self.access_policy.value

        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)

        encryption_settings = self.encryption_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessPolicy": access_policy,
                "accounts": accounts,
                "encryptionSettings": encryption_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_storage_settings_encryption_model import BackupStorageSettingsEncryptionModel
        from ..models.repository_access_account_model import RepositoryAccessAccountModel

        d = dict(src_dict)
        access_policy = ERepositoryAccessType(d.pop("accessPolicy"))

        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = RepositoryAccessAccountModel.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        encryption_settings = BackupStorageSettingsEncryptionModel.from_dict(d.pop("encryptionSettings"))

        repository_access_permissions_model = cls(
            access_policy=access_policy,
            accounts=accounts,
            encryption_settings=encryption_settings,
        )

        repository_access_permissions_model.additional_properties = d
        return repository_access_permissions_model

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
