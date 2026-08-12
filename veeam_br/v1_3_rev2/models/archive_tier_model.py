from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archive_tier_advanced_settings_model import ArchiveTierAdvancedSettingsModel
    from ..models.backup_storage_settings_encryption_model import BackupStorageSettingsEncryptionModel


T = TypeVar("T", bound="ArchiveTierModel")


@_attrs_define
class ArchiveTierModel:
    """Archive tier.

    Attributes:
        is_enabled (bool): If `true`, the archive tier is enabled.
        extent_id (UUID | Unset): ID of an object storage repository added as an archive extent.
        extent_crypto_key_id (UUID | Unset): If an object storage repository added as an archive extent is encrypted,
            specify an ID of a crypto key for decryption.
        archive_period_days (int | Unset): Number of days after which backup chains on the capacity extent are moved to
            the archive extent. Specify *0* to offload inactive backup chains on the same day they are created.
        copy_policy_enabled (bool | Unset): If `true`, Veeam Backup & Replication copies backups to the archive extent
            as soon as the backups are created. Default: False.
        move_policy_enabled (bool | Unset): If `true`, Veeam Backup & Replication moves backups from the capacity extent
            to the archive extent after the `archivePeriodDays` period.
        advanced_settings (ArchiveTierAdvancedSettingsModel | Unset): Advanced settings of the archive tier.
        encryption (BackupStorageSettingsEncryptionModel | Unset): Encryption of backup files.
    """

    is_enabled: bool
    extent_id: UUID | Unset = UNSET
    extent_crypto_key_id: UUID | Unset = UNSET
    archive_period_days: int | Unset = UNSET
    copy_policy_enabled: bool | Unset = False
    move_policy_enabled: bool | Unset = UNSET
    advanced_settings: ArchiveTierAdvancedSettingsModel | Unset = UNSET
    encryption: BackupStorageSettingsEncryptionModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        extent_id: str | Unset = UNSET
        if not isinstance(self.extent_id, Unset):
            extent_id = str(self.extent_id)

        extent_crypto_key_id: str | Unset = UNSET
        if not isinstance(self.extent_crypto_key_id, Unset):
            extent_crypto_key_id = str(self.extent_crypto_key_id)

        archive_period_days = self.archive_period_days

        copy_policy_enabled = self.copy_policy_enabled

        move_policy_enabled = self.move_policy_enabled

        advanced_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_settings, Unset):
            advanced_settings = self.advanced_settings.to_dict()

        encryption: dict[str, Any] | Unset = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if extent_id is not UNSET:
            field_dict["extentId"] = extent_id
        if extent_crypto_key_id is not UNSET:
            field_dict["extentCryptoKeyId"] = extent_crypto_key_id
        if archive_period_days is not UNSET:
            field_dict["archivePeriodDays"] = archive_period_days
        if copy_policy_enabled is not UNSET:
            field_dict["copyPolicyEnabled"] = copy_policy_enabled
        if move_policy_enabled is not UNSET:
            field_dict["movePolicyEnabled"] = move_policy_enabled
        if advanced_settings is not UNSET:
            field_dict["advancedSettings"] = advanced_settings
        if encryption is not UNSET:
            field_dict["encryption"] = encryption

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archive_tier_advanced_settings_model import ArchiveTierAdvancedSettingsModel
        from ..models.backup_storage_settings_encryption_model import BackupStorageSettingsEncryptionModel

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        _extent_id = d.pop("extentId", UNSET)
        extent_id: UUID | Unset
        if isinstance(_extent_id, Unset):
            extent_id = UNSET
        else:
            extent_id = UUID(_extent_id)

        _extent_crypto_key_id = d.pop("extentCryptoKeyId", UNSET)
        extent_crypto_key_id: UUID | Unset
        if isinstance(_extent_crypto_key_id, Unset):
            extent_crypto_key_id = UNSET
        else:
            extent_crypto_key_id = UUID(_extent_crypto_key_id)

        archive_period_days = d.pop("archivePeriodDays", UNSET)

        copy_policy_enabled = d.pop("copyPolicyEnabled", UNSET)

        move_policy_enabled = d.pop("movePolicyEnabled", UNSET)

        _advanced_settings = d.pop("advancedSettings", UNSET)
        advanced_settings: ArchiveTierAdvancedSettingsModel | Unset
        if isinstance(_advanced_settings, Unset):
            advanced_settings = UNSET
        else:
            advanced_settings = ArchiveTierAdvancedSettingsModel.from_dict(_advanced_settings)

        _encryption = d.pop("encryption", UNSET)
        encryption: BackupStorageSettingsEncryptionModel | Unset
        if isinstance(_encryption, Unset):
            encryption = UNSET
        else:
            encryption = BackupStorageSettingsEncryptionModel.from_dict(_encryption)

        archive_tier_model = cls(
            is_enabled=is_enabled,
            extent_id=extent_id,
            extent_crypto_key_id=extent_crypto_key_id,
            archive_period_days=archive_period_days,
            copy_policy_enabled=copy_policy_enabled,
            move_policy_enabled=move_policy_enabled,
            advanced_settings=advanced_settings,
            encryption=encryption,
        )

        archive_tier_model.additional_properties = d
        return archive_tier_model

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
