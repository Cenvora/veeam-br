from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_volume_file_system_type import EVolumeFileSystemType

if TYPE_CHECKING:
    from ..models.partition_info_model import PartitionInfoModel
    from ..models.size_model import SizeModel


T = TypeVar("T", bound="ResizePartitionOptionsRequest")


@_attrs_define
class ResizePartitionOptionsRequest:
    """Options for resizing disk partition.

    Attributes:
        disk_number (int): Disk number where the partition is located.
        live_volume_exists (bool): If `true`, a live volume exists for the partition.
        fs_type (EVolumeFileSystemType): File system type of the volume.
        size (SizeModel): Size value with a measurement unit.
        partition_info (PartitionInfoModel): Disk partition information.
    """

    disk_number: int
    live_volume_exists: bool
    fs_type: EVolumeFileSystemType
    size: SizeModel
    partition_info: PartitionInfoModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disk_number = self.disk_number

        live_volume_exists = self.live_volume_exists

        fs_type = self.fs_type.value

        size = self.size.to_dict()

        partition_info = self.partition_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "diskNumber": disk_number,
                "liveVolumeExists": live_volume_exists,
                "fsType": fs_type,
                "size": size,
                "partitionInfo": partition_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partition_info_model import PartitionInfoModel
        from ..models.size_model import SizeModel

        d = dict(src_dict)
        disk_number = d.pop("diskNumber")

        live_volume_exists = d.pop("liveVolumeExists")

        fs_type = EVolumeFileSystemType(d.pop("fsType"))

        size = SizeModel.from_dict(d.pop("size"))

        partition_info = PartitionInfoModel.from_dict(d.pop("partitionInfo"))

        resize_partition_options_request = cls(
            disk_number=disk_number,
            live_volume_exists=live_volume_exists,
            fs_type=fs_type,
            size=size,
            partition_info=partition_info,
        )

        resize_partition_options_request.additional_properties = d
        return resize_partition_options_request

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
