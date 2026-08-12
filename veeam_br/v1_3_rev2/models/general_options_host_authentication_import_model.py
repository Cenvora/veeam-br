from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GeneralOptionsHostAuthenticationImportModel")


@_attrs_define
class GeneralOptionsHostAuthenticationImportModel:
    """Settings for importing the list of trusted hosts.

    Attributes:
        path (str): Path to the file from which the list of trusted hosts is imported.
        overwrite_existing_trusted_hosts (bool): If `true`, existing trusted hosts are overwritten during the import.
    """

    path: str
    overwrite_existing_trusted_hosts: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        overwrite_existing_trusted_hosts = self.overwrite_existing_trusted_hosts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "overwriteExistingTrustedHosts": overwrite_existing_trusted_hosts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        overwrite_existing_trusted_hosts = d.pop("overwriteExistingTrustedHosts")

        general_options_host_authentication_import_model = cls(
            path=path,
            overwrite_existing_trusted_hosts=overwrite_existing_trusted_hosts,
        )

        general_options_host_authentication_import_model.additional_properties = d
        return general_options_host_authentication_import_model

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
