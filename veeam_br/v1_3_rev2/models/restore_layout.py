from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disk_mapping_context import DiskMappingContext


T = TypeVar("T", bound="RestoreLayout")


@_attrs_define
class RestoreLayout:
    """Restore layout for agent or recovery appliance.

    Attributes:
        id (UUID): Agent or recovery appliance ID.
        name (str): Agent or recovery appliance name.
        disk_management_session_id (UUID): Disk management session ID.
        volume_matching_results (DiskMappingContext): Disk mapping context.
        target_layout (DiskMappingContext | Unset): Disk mapping context.
        source_layout (DiskMappingContext | Unset): Disk mapping context.
    """

    id: UUID
    name: str
    disk_management_session_id: UUID
    volume_matching_results: DiskMappingContext
    target_layout: DiskMappingContext | Unset = UNSET
    source_layout: DiskMappingContext | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        disk_management_session_id = str(self.disk_management_session_id)

        volume_matching_results = self.volume_matching_results.to_dict()

        target_layout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_layout, Unset):
            target_layout = self.target_layout.to_dict()

        source_layout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_layout, Unset):
            source_layout = self.source_layout.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "diskManagementSessionId": disk_management_session_id,
                "volumeMatchingResults": volume_matching_results,
            }
        )
        if target_layout is not UNSET:
            field_dict["targetLayout"] = target_layout
        if source_layout is not UNSET:
            field_dict["sourceLayout"] = source_layout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disk_mapping_context import DiskMappingContext

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        disk_management_session_id = UUID(d.pop("diskManagementSessionId"))

        volume_matching_results = DiskMappingContext.from_dict(d.pop("volumeMatchingResults"))

        _target_layout = d.pop("targetLayout", UNSET)
        target_layout: DiskMappingContext | Unset
        if isinstance(_target_layout, Unset):
            target_layout = UNSET
        else:
            target_layout = DiskMappingContext.from_dict(_target_layout)

        _source_layout = d.pop("sourceLayout", UNSET)
        source_layout: DiskMappingContext | Unset
        if isinstance(_source_layout, Unset):
            source_layout = UNSET
        else:
            source_layout = DiskMappingContext.from_dict(_source_layout)

        restore_layout = cls(
            id=id,
            name=name,
            disk_management_session_id=disk_management_session_id,
            volume_matching_results=volume_matching_results,
            target_layout=target_layout,
            source_layout=source_layout,
        )

        restore_layout.additional_properties = d
        return restore_layout

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
