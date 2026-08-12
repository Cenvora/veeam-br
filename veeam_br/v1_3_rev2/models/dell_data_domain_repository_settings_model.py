from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_advanced_settings_model import RepositoryAdvancedSettingsModel
    from ..models.repository_immutability_model import RepositoryImmutabilityModel


T = TypeVar("T", bound="DellDataDomainRepositorySettingsModel")


@_attrs_define
class DellDataDomainRepositorySettingsModel:
    """Dell Data Domain repository settings.

    Attributes:
        path (str): Path to the folder where backup files are stored.
        immutability (RepositoryImmutabilityModel | Unset): Backup repository immutability settings.
        enable_task_limit (bool | Unset): If `true`, the maximum number of concurrent tasks is limited.
        max_task_count (int | Unset): Maximum number of concurrent tasks.
        enable_read_write_limit (bool | Unset): If `true`, the maximum rate that restricts the total speed of reading
            and writing data to the backup repository disk is limited.
        read_write_rate (int | Unset): Maximum rate that restricts the total speed of reading and writing data to the
            backup repository disk.
        advanced_settings (RepositoryAdvancedSettingsModel | Unset): Advanced settings for the backup repository.
    """

    path: str
    immutability: RepositoryImmutabilityModel | Unset = UNSET
    enable_task_limit: bool | Unset = UNSET
    max_task_count: int | Unset = UNSET
    enable_read_write_limit: bool | Unset = UNSET
    read_write_rate: int | Unset = UNSET
    advanced_settings: RepositoryAdvancedSettingsModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        immutability: dict[str, Any] | Unset = UNSET
        if not isinstance(self.immutability, Unset):
            immutability = self.immutability.to_dict()

        enable_task_limit = self.enable_task_limit

        max_task_count = self.max_task_count

        enable_read_write_limit = self.enable_read_write_limit

        read_write_rate = self.read_write_rate

        advanced_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_settings, Unset):
            advanced_settings = self.advanced_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if immutability is not UNSET:
            field_dict["immutability"] = immutability
        if enable_task_limit is not UNSET:
            field_dict["enableTaskLimit"] = enable_task_limit
        if max_task_count is not UNSET:
            field_dict["maxTaskCount"] = max_task_count
        if enable_read_write_limit is not UNSET:
            field_dict["enableReadWriteLimit"] = enable_read_write_limit
        if read_write_rate is not UNSET:
            field_dict["readWriteRate"] = read_write_rate
        if advanced_settings is not UNSET:
            field_dict["advancedSettings"] = advanced_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_advanced_settings_model import RepositoryAdvancedSettingsModel
        from ..models.repository_immutability_model import RepositoryImmutabilityModel

        d = dict(src_dict)
        path = d.pop("path")

        _immutability = d.pop("immutability", UNSET)
        immutability: RepositoryImmutabilityModel | Unset
        if isinstance(_immutability, Unset):
            immutability = UNSET
        else:
            immutability = RepositoryImmutabilityModel.from_dict(_immutability)

        enable_task_limit = d.pop("enableTaskLimit", UNSET)

        max_task_count = d.pop("maxTaskCount", UNSET)

        enable_read_write_limit = d.pop("enableReadWriteLimit", UNSET)

        read_write_rate = d.pop("readWriteRate", UNSET)

        _advanced_settings = d.pop("advancedSettings", UNSET)
        advanced_settings: RepositoryAdvancedSettingsModel | Unset
        if isinstance(_advanced_settings, Unset):
            advanced_settings = UNSET
        else:
            advanced_settings = RepositoryAdvancedSettingsModel.from_dict(_advanced_settings)

        dell_data_domain_repository_settings_model = cls(
            path=path,
            immutability=immutability,
            enable_task_limit=enable_task_limit,
            max_task_count=max_task_count,
            enable_read_write_limit=enable_read_write_limit,
            read_write_rate=read_write_rate,
            advanced_settings=advanced_settings,
        )

        dell_data_domain_repository_settings_model.additional_properties = d
        return dell_data_domain_repository_settings_model

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
