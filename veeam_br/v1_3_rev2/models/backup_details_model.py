from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupDetailsModel")


@_attrs_define
class BackupDetailsModel:
    """Backup details.

    Attributes:
        object_original_size (float | Unset): Approximate original size of objects in the backup. When no `objectId` is
            provided, returns the sum across all objects. When `objectId` is provided, returns the approximate original size
            of that object only.
        backup_size (float | Unset): Total physical file size of backup files on disk after compression and
            deduplication. When `objectId` is provided, returns the sum for related storages to that object only.
        actual_size (float | Unset): Tier-aware physical size of the backup on storage. For SOBR repositories, this
            accounts for data distribution across performance, capacity, and archive tiers using extent-level tracking,
            avoiding double-counting. For non-SOBR repositories, equals `backupSize`. When `objectId` is provided, falls
            back to the sum of physical file sizes for storages related to that object.
        restore_points_count (int | Unset): Number of restore points in the backup.
    """

    object_original_size: float | Unset = UNSET
    backup_size: float | Unset = UNSET
    actual_size: float | Unset = UNSET
    restore_points_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_original_size = self.object_original_size

        backup_size = self.backup_size

        actual_size = self.actual_size

        restore_points_count = self.restore_points_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_original_size is not UNSET:
            field_dict["objectOriginalSize"] = object_original_size
        if backup_size is not UNSET:
            field_dict["backupSize"] = backup_size
        if actual_size is not UNSET:
            field_dict["actualSize"] = actual_size
        if restore_points_count is not UNSET:
            field_dict["restorePointsCount"] = restore_points_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_original_size = d.pop("objectOriginalSize", UNSET)

        backup_size = d.pop("backupSize", UNSET)

        actual_size = d.pop("actualSize", UNSET)

        restore_points_count = d.pop("restorePointsCount", UNSET)

        backup_details_model = cls(
            object_original_size=object_original_size,
            backup_size=backup_size,
            actual_size=actual_size,
            restore_points_count=restore_points_count,
        )

        backup_details_model.additional_properties = d
        return backup_details_model

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
