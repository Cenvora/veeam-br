from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_file_server_host_type import EFileServerHostType
from ..models.e_unstructured_data_server_type import EUnstructuredDataServerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_server_processing_model import FileServerProcessingModel


T = TypeVar("T", bound="FileServerModel")


@_attrs_define
class FileServerModel:
    """File server.

    Attributes:
        id (UUID): ID of the unstructured data server.
        type_ (EUnstructuredDataServerType): Type of unstructured data server.
        host_id (UUID): Host ID.
        processing (FileServerProcessingModel): File server processing settings.
        name (str | Unset): DNS name of the file server.
        host_type (EFileServerHostType | Unset): Type of the host that backs the file server. Identifies whether the
            file server is a Linux machine, a Windows machine or the Veeam Backup & Replication server itself. Set by the
            server; ignored on write.
    """

    id: UUID
    type_: EUnstructuredDataServerType
    host_id: UUID
    processing: FileServerProcessingModel
    name: str | Unset = UNSET
    host_type: EFileServerHostType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_.value

        host_id = str(self.host_id)

        processing = self.processing.to_dict()

        name = self.name

        host_type: str | Unset = UNSET
        if not isinstance(self.host_type, Unset):
            host_type = self.host_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "hostId": host_id,
                "processing": processing,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if host_type is not UNSET:
            field_dict["hostType"] = host_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_server_processing_model import FileServerProcessingModel

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = EUnstructuredDataServerType(d.pop("type"))

        host_id = UUID(d.pop("hostId"))

        processing = FileServerProcessingModel.from_dict(d.pop("processing"))

        name = d.pop("name", UNSET)

        _host_type = d.pop("hostType", UNSET)
        host_type: EFileServerHostType | Unset
        if isinstance(_host_type, Unset):
            host_type = UNSET
        else:
            host_type = EFileServerHostType(_host_type)

        file_server_model = cls(
            id=id,
            type_=type_,
            host_id=host_id,
            processing=processing,
            name=name,
            host_type=host_type,
        )

        file_server_model.additional_properties = d
        return file_server_model

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
