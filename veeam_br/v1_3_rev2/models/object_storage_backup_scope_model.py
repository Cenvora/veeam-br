from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_inventory_scope_workload_type import EInventoryScopeWorkloadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unstructured_data_backup_scope_item_model import UnstructuredDataBackupScopeItemModel


T = TypeVar("T", bound="ObjectStorageBackupScopeModel")


@_attrs_define
class ObjectStorageBackupScopeModel:
    """Object storage backup scope.

    Attributes:
        type_ (EInventoryScopeWorkloadType): Workload type.
        object_storage_server (list[UnstructuredDataBackupScopeItemModel] | Unset): Array of object storage servers.
    """

    type_: EInventoryScopeWorkloadType
    object_storage_server: list[UnstructuredDataBackupScopeItemModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        object_storage_server: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.object_storage_server, Unset):
            object_storage_server = []
            for object_storage_server_item_data in self.object_storage_server:
                object_storage_server_item = object_storage_server_item_data.to_dict()
                object_storage_server.append(object_storage_server_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if object_storage_server is not UNSET:
            field_dict["objectStorageServer"] = object_storage_server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unstructured_data_backup_scope_item_model import UnstructuredDataBackupScopeItemModel

        d = dict(src_dict)
        type_ = EInventoryScopeWorkloadType(d.pop("type"))

        _object_storage_server = d.pop("objectStorageServer", UNSET)
        object_storage_server: list[UnstructuredDataBackupScopeItemModel] | Unset = UNSET
        if _object_storage_server is not UNSET:
            object_storage_server = []
            for object_storage_server_item_data in _object_storage_server:
                object_storage_server_item = UnstructuredDataBackupScopeItemModel.from_dict(
                    object_storage_server_item_data
                )

                object_storage_server.append(object_storage_server_item)

        object_storage_backup_scope_model = cls(
            type_=type_,
            object_storage_server=object_storage_server,
        )

        object_storage_backup_scope_model.additional_properties = d
        return object_storage_backup_scope_model

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
