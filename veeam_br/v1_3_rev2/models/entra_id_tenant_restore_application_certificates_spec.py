from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.entra_id_tenant_restore_application_certificate_item_spec import (
        EntraIdTenantRestoreApplicationCertificateItemSpec,
    )


T = TypeVar("T", bound="EntraIdTenantRestoreApplicationCertificatesSpec")


@_attrs_define
class EntraIdTenantRestoreApplicationCertificatesSpec:
    """Settings of custom application certificates restore.

    Attributes:
        application_id (str): Application ID.
        certificates (list[EntraIdTenantRestoreApplicationCertificateItemSpec]): Array of certificates.
    """

    application_id: str
    certificates: list[EntraIdTenantRestoreApplicationCertificateItemSpec]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        certificates = []
        for certificates_item_data in self.certificates:
            certificates_item = certificates_item_data.to_dict()
            certificates.append(certificates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applicationId": application_id,
                "certificates": certificates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entra_id_tenant_restore_application_certificate_item_spec import (
            EntraIdTenantRestoreApplicationCertificateItemSpec,
        )

        d = dict(src_dict)
        application_id = d.pop("applicationId")

        certificates = []
        _certificates = d.pop("certificates")
        for certificates_item_data in _certificates:
            certificates_item = EntraIdTenantRestoreApplicationCertificateItemSpec.from_dict(certificates_item_data)

            certificates.append(certificates_item)

        entra_id_tenant_restore_application_certificates_spec = cls(
            application_id=application_id,
            certificates=certificates,
        )

        entra_id_tenant_restore_application_certificates_spec.additional_properties = d
        return entra_id_tenant_restore_application_certificates_spec

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
