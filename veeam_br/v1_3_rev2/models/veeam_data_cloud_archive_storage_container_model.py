from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.object_storage_immutability_model import ObjectStorageImmutabilityModel


T = TypeVar("T", bound="VeeamDataCloudArchiveStorageContainerModel")


@_attrs_define
class VeeamDataCloudArchiveStorageContainerModel:
    """Veeam Data Cloud Archive container.

    Attributes:
        folder (str): Folder used to store data.
        immutability (ObjectStorageImmutabilityModel): Object storage immutability.
    """

    folder: str
    immutability: ObjectStorageImmutabilityModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folder = self.folder

        immutability = self.immutability.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folder": folder,
                "immutability": immutability,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_storage_immutability_model import ObjectStorageImmutabilityModel

        d = dict(src_dict)
        folder = d.pop("folder")

        immutability = ObjectStorageImmutabilityModel.from_dict(d.pop("immutability"))

        veeam_data_cloud_archive_storage_container_model = cls(
            folder=folder,
            immutability=immutability,
        )

        veeam_data_cloud_archive_storage_container_model.additional_properties = d
        return veeam_data_cloud_archive_storage_container_model

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
