from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.size_model import SizeModel


T = TypeVar("T", bound="RemoveDiskPartitionOperationSpec")


@_attrs_define
class RemoveDiskPartitionOperationSpec:
    """Settings for removing a disk partition.

    Attributes:
        target_disk_number (int): Disk number.
        live_volume_id (None | UUID): Live volume ID.
        start_offset (SizeModel): Size value with a measurement unit.
        size (SizeModel): Size value with a measurement unit.
    """

    target_disk_number: int
    live_volume_id: None | UUID
    start_offset: SizeModel
    size: SizeModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_disk_number = self.target_disk_number

        live_volume_id: None | str
        if isinstance(self.live_volume_id, UUID):
            live_volume_id = str(self.live_volume_id)
        else:
            live_volume_id = self.live_volume_id

        start_offset = self.start_offset.to_dict()

        size = self.size.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetDiskNumber": target_disk_number,
                "liveVolumeId": live_volume_id,
                "startOffset": start_offset,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.size_model import SizeModel

        d = dict(src_dict)
        target_disk_number = d.pop("targetDiskNumber")

        def _parse_live_volume_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                live_volume_id_type_0 = UUID(data)

                return live_volume_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        live_volume_id = _parse_live_volume_id(d.pop("liveVolumeId"))

        start_offset = SizeModel.from_dict(d.pop("startOffset"))

        size = SizeModel.from_dict(d.pop("size"))

        remove_disk_partition_operation_spec = cls(
            target_disk_number=target_disk_number,
            live_volume_id=live_volume_id,
            start_offset=start_offset,
            size=size,
        )

        remove_disk_partition_operation_spec.additional_properties = d
        return remove_disk_partition_operation_spec

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
