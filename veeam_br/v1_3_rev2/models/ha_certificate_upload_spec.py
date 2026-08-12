from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_ha_certificate_file_format_type import EHaCertificateFileFormatType

T = TypeVar("T", bound="HaCertificateUploadSpec")


@_attrs_define
class HaCertificateUploadSpec:
    """PEM certificate settings for the HA cluster.

    Attributes:
        certificate (str): Base64-encoded string of the PEM certificate content.
        format_type (EHaCertificateFileFormatType): Certificate file format. Only PEM is supported for HA clusters.
    """

    certificate: str
    format_type: EHaCertificateFileFormatType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate = self.certificate

        format_type = self.format_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "certificate": certificate,
                "formatType": format_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate = d.pop("certificate")

        format_type = EHaCertificateFileFormatType(d.pop("formatType"))

        ha_certificate_upload_spec = cls(
            certificate=certificate,
            format_type=format_type,
        )

        ha_certificate_upload_spec.additional_properties = d
        return ha_certificate_upload_spec

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
