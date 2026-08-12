from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredDataInventoryBrowseSessionModel")


@_attrs_define
class UnstructuredDataInventoryBrowseSessionModel:
    """Unstructured data inventory browse session.

    Attributes:
        session_id (UUID): ID of the browse session.
        server_id (UUID): ID of the server being browsed.
        timeout (int): timeout in minutes.
        path_separator (str): Character that separates individual paths.
        root_path (str): Root path of the browse session.
        server_name (str | Unset): Name of the server being browsed.
    """

    session_id: UUID
    server_id: UUID
    timeout: int
    path_separator: str
    root_path: str
    server_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = str(self.session_id)

        server_id = str(self.server_id)

        timeout = self.timeout

        path_separator = self.path_separator

        root_path = self.root_path

        server_name = self.server_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sessionId": session_id,
                "serverId": server_id,
                "timeout": timeout,
                "pathSeparator": path_separator,
                "rootPath": root_path,
            }
        )
        if server_name is not UNSET:
            field_dict["serverName"] = server_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = UUID(d.pop("sessionId"))

        server_id = UUID(d.pop("serverId"))

        timeout = d.pop("timeout")

        path_separator = d.pop("pathSeparator")

        root_path = d.pop("rootPath")

        server_name = d.pop("serverName", UNSET)

        unstructured_data_inventory_browse_session_model = cls(
            session_id=session_id,
            server_id=server_id,
            timeout=timeout,
            path_separator=path_separator,
            root_path=root_path,
            server_name=server_name,
        )

        unstructured_data_inventory_browse_session_model.additional_properties = d
        return unstructured_data_inventory_browse_session_model

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
