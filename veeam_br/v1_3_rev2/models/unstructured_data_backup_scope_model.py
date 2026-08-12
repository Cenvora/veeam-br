from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_inventory_scope_workload_type import EInventoryScopeWorkloadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unstructured_data_backup_scope_item_model import UnstructuredDataBackupScopeItemModel


T = TypeVar("T", bound="UnstructuredDataBackupScopeModel")


@_attrs_define
class UnstructuredDataBackupScopeModel:
    """Unstructured data backup scope.

    Attributes:
        type_ (EInventoryScopeWorkloadType): Workload type.
        file_shares (list[UnstructuredDataBackupScopeItemModel] | Unset): Array of file shares.
    """

    type_: EInventoryScopeWorkloadType
    file_shares: list[UnstructuredDataBackupScopeItemModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        file_shares: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.file_shares, Unset):
            file_shares = []
            for file_shares_item_data in self.file_shares:
                file_shares_item = file_shares_item_data.to_dict()
                file_shares.append(file_shares_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if file_shares is not UNSET:
            field_dict["fileShares"] = file_shares

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unstructured_data_backup_scope_item_model import UnstructuredDataBackupScopeItemModel

        d = dict(src_dict)
        type_ = EInventoryScopeWorkloadType(d.pop("type"))

        _file_shares = d.pop("fileShares", UNSET)
        file_shares: list[UnstructuredDataBackupScopeItemModel] | Unset = UNSET
        if _file_shares is not UNSET:
            file_shares = []
            for file_shares_item_data in _file_shares:
                file_shares_item = UnstructuredDataBackupScopeItemModel.from_dict(file_shares_item_data)

                file_shares.append(file_shares_item)

        unstructured_data_backup_scope_model = cls(
            type_=type_,
            file_shares=file_shares,
        )

        unstructured_data_backup_scope_model.additional_properties = d
        return unstructured_data_backup_scope_model

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
