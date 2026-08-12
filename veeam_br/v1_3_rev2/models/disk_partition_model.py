from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_disk_partition_operation_type import EDiskPartitionOperationType
from ..models.e_disk_partition_type import EDiskPartitionType
from ..models.e_volume_file_system_type import EVolumeFileSystemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partition_info_model import PartitionInfoModel
    from ..models.size_model import SizeModel


T = TypeVar("T", bound="DiskPartitionModel")


@_attrs_define
class DiskPartitionModel:
    """Disk partition.

    Attributes:
        size (SizeModel): Size value with a measurement unit.
        starting_offset (SizeModel): Size value with a measurement unit.
        type_ (EDiskPartitionType): Type of disk partition.
        fs_type (EVolumeFileSystemType): File system type of the volume.
        available_operations (list[EDiskPartitionOperationType]): Available operations for the partition.
        live_volume_exists (bool): If `true`, a live volume exists for the partition.
        name (str | Unset): Partition name.
        description (str | Unset): Partition description.
        live_volume_id (None | Unset | UUID): Live volume ID.
        additional_info (PartitionInfoModel | Unset): Disk partition information.
    """

    size: SizeModel
    starting_offset: SizeModel
    type_: EDiskPartitionType
    fs_type: EVolumeFileSystemType
    available_operations: list[EDiskPartitionOperationType]
    live_volume_exists: bool
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    live_volume_id: None | Unset | UUID = UNSET
    additional_info: PartitionInfoModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size.to_dict()

        starting_offset = self.starting_offset.to_dict()

        type_ = self.type_.value

        fs_type = self.fs_type.value

        available_operations = []
        for available_operations_item_data in self.available_operations:
            available_operations_item = available_operations_item_data.value
            available_operations.append(available_operations_item)

        live_volume_exists = self.live_volume_exists

        name = self.name

        description = self.description

        live_volume_id: None | str | Unset
        if isinstance(self.live_volume_id, Unset):
            live_volume_id = UNSET
        elif isinstance(self.live_volume_id, UUID):
            live_volume_id = str(self.live_volume_id)
        else:
            live_volume_id = self.live_volume_id

        additional_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_info, Unset):
            additional_info = self.additional_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "size": size,
                "startingOffset": starting_offset,
                "type": type_,
                "fsType": fs_type,
                "availableOperations": available_operations,
                "liveVolumeExists": live_volume_exists,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if live_volume_id is not UNSET:
            field_dict["liveVolumeId"] = live_volume_id
        if additional_info is not UNSET:
            field_dict["additionalInfo"] = additional_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partition_info_model import PartitionInfoModel
        from ..models.size_model import SizeModel

        d = dict(src_dict)
        size = SizeModel.from_dict(d.pop("size"))

        starting_offset = SizeModel.from_dict(d.pop("startingOffset"))

        type_ = EDiskPartitionType(d.pop("type"))

        fs_type = EVolumeFileSystemType(d.pop("fsType"))

        available_operations = []
        _available_operations = d.pop("availableOperations")
        for available_operations_item_data in _available_operations:
            available_operations_item = EDiskPartitionOperationType(available_operations_item_data)

            available_operations.append(available_operations_item)

        live_volume_exists = d.pop("liveVolumeExists")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_live_volume_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                live_volume_id_type_0 = UUID(data)

                return live_volume_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        live_volume_id = _parse_live_volume_id(d.pop("liveVolumeId", UNSET))

        _additional_info = d.pop("additionalInfo", UNSET)
        additional_info: PartitionInfoModel | Unset
        if isinstance(_additional_info, Unset):
            additional_info = UNSET
        else:
            additional_info = PartitionInfoModel.from_dict(_additional_info)

        disk_partition_model = cls(
            size=size,
            starting_offset=starting_offset,
            type_=type_,
            fs_type=fs_type,
            available_operations=available_operations,
            live_volume_exists=live_volume_exists,
            name=name,
            description=description,
            live_volume_id=live_volume_id,
            additional_info=additional_info,
        )

        disk_partition_model.additional_properties = d
        return disk_partition_model

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
