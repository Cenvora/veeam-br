from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredDataBackupScopeItemModel")


@_attrs_define
class UnstructuredDataBackupScopeItemModel:
    """Unstructured data backup scope item.

    Attributes:
        server_id (UUID): Server ID.
        folder (str): Path to the folder.
        server_name (str | Unset): Server name.
    """

    server_id: UUID
    folder: str
    server_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_id = str(self.server_id)

        folder = self.folder

        server_name = self.server_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serverId": server_id,
                "folder": folder,
            }
        )
        if server_name is not UNSET:
            field_dict["serverName"] = server_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_id = UUID(d.pop("serverId"))

        folder = d.pop("folder")

        server_name = d.pop("serverName", UNSET)

        unstructured_data_backup_scope_item_model = cls(
            server_id=server_id,
            folder=folder,
            server_name=server_name,
        )

        unstructured_data_backup_scope_item_model.additional_properties = d
        return unstructured_data_backup_scope_item_model

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
