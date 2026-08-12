from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_flr_restore_type import EFlrRestoreType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flr_restore_target_host_model import FlrRestoreTargetHostModel


T = TypeVar("T", bound="FlrRestoreToSpec")


@_attrs_define
class FlrRestoreToSpec:
    """Settings for restoring files and folders to another location.

    Attributes:
        source_path (list[str]): Array of paths to the items that you want to restore.
        restore_type (EFlrRestoreType): Restore type.
        target_host (FlrRestoreTargetHostModel): Target machine. To get an inventory object, run the [Get Inventory
            Objects](Inventory-Browser#operation/GetInventoryObjects) request.
        target_path (str): Path to the target folder.
        credentials_id (UUID | Unset): ID of a credentials record used to connect to the target machine.
    """

    source_path: list[str]
    restore_type: EFlrRestoreType
    target_host: FlrRestoreTargetHostModel
    target_path: str
    credentials_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_path = self.source_path

        restore_type = self.restore_type.value

        target_host = self.target_host.to_dict()

        target_path = self.target_path

        credentials_id: str | Unset = UNSET
        if not isinstance(self.credentials_id, Unset):
            credentials_id = str(self.credentials_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourcePath": source_path,
                "restoreType": restore_type,
                "targetHost": target_host,
                "targetPath": target_path,
            }
        )
        if credentials_id is not UNSET:
            field_dict["credentialsId"] = credentials_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flr_restore_target_host_model import FlrRestoreTargetHostModel

        d = dict(src_dict)
        source_path = cast(list[str], d.pop("sourcePath"))

        restore_type = EFlrRestoreType(d.pop("restoreType"))

        target_host = FlrRestoreTargetHostModel.from_dict(d.pop("targetHost"))

        target_path = d.pop("targetPath")

        _credentials_id = d.pop("credentialsId", UNSET)
        credentials_id: UUID | Unset
        if isinstance(_credentials_id, Unset):
            credentials_id = UNSET
        else:
            credentials_id = UUID(_credentials_id)

        flr_restore_to_spec = cls(
            source_path=source_path,
            restore_type=restore_type,
            target_host=target_host,
            target_path=target_path,
            credentials_id=credentials_id,
        )

        flr_restore_to_spec.additional_properties = d
        return flr_restore_to_spec

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
