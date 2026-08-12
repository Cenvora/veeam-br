from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_model import CertificateModel
    from ..models.certificate_upload_spec import CertificateUploadSpec


T = TypeVar("T", bound="ConnectionCertificateModel")


@_attrs_define
class ConnectionCertificateModel:
    """Connection fingerprint or certificate.

    Attributes:
        fingerprint (str | Unset): SSH key fingerprint used to verify the server identity.
        certificate (CertificateModel | Unset): Certificate settings.
        certificate_upload (CertificateUploadSpec | Unset): Certificate settings (for certificate-based authentication).
    """

    fingerprint: str | Unset = UNSET
    certificate: CertificateModel | Unset = UNSET
    certificate_upload: CertificateUploadSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fingerprint = self.fingerprint

        certificate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.certificate, Unset):
            certificate = self.certificate.to_dict()

        certificate_upload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.certificate_upload, Unset):
            certificate_upload = self.certificate_upload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if certificate_upload is not UNSET:
            field_dict["certificateUpload"] = certificate_upload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_model import CertificateModel
        from ..models.certificate_upload_spec import CertificateUploadSpec

        d = dict(src_dict)
        fingerprint = d.pop("fingerprint", UNSET)

        _certificate = d.pop("certificate", UNSET)
        certificate: CertificateModel | Unset
        if isinstance(_certificate, Unset):
            certificate = UNSET
        else:
            certificate = CertificateModel.from_dict(_certificate)

        _certificate_upload = d.pop("certificateUpload", UNSET)
        certificate_upload: CertificateUploadSpec | Unset
        if isinstance(_certificate_upload, Unset):
            certificate_upload = UNSET
        else:
            certificate_upload = CertificateUploadSpec.from_dict(_certificate_upload)

        connection_certificate_model = cls(
            fingerprint=fingerprint,
            certificate=certificate,
            certificate_upload=certificate_upload,
        )

        connection_certificate_model.additional_properties = d
        return connection_certificate_model

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
