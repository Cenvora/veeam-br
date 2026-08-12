from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_platform_type import EPlatformType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupSourceObjectModel")


@_attrs_define
class BackupSourceObjectModel:
    """Backup source for the backup copy job. Supported platforms are `AWSEC2`, `AzureCompute`, and `GCE`

    Attributes:
        id (UUID): Backup ID.
        name (str | Unset): Name of the backup.
        platform_name (EPlatformType | Unset): Platform type.<p>`Test` is the platform of SureBackup content scan job
            (`SureBackupContentScan`) — backup verification and content scanning with antivirus software or YARA rules.</p>
    """

    id: UUID
    name: str | Unset = UNSET
    platform_name: EPlatformType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        platform_name: str | Unset = UNSET
        if not isinstance(self.platform_name, Unset):
            platform_name = self.platform_name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if platform_name is not UNSET:
            field_dict["platformName"] = platform_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name", UNSET)

        _platform_name = d.pop("platformName", UNSET)
        platform_name: EPlatformType | Unset
        if isinstance(_platform_name, Unset):
            platform_name = UNSET
        else:
            platform_name = EPlatformType(_platform_name)

        backup_source_object_model = cls(
            id=id,
            name=name,
            platform_name=platform_name,
        )

        backup_source_object_model.additional_properties = d
        return backup_source_object_model

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
