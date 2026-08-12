from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntraIdTenantOrgContactFilterBrowseSpec")


@_attrs_define
class EntraIdTenantOrgContactFilterBrowseSpec:
    """Filtering options.

    Attributes:
        display_name (str | Unset): Display name of the organization contact.
        company_name (str | Unset): Name of the company that this organizational contact belongs to.
        department (str | Unset): The name for the department in which the contact works.
        job_title (str | Unset): Job title for this organizational contact.
        mail (str | Unset): The SMTP address for the contact, for example, "jeff@contoso.com".
    """

    display_name: str | Unset = UNSET
    company_name: str | Unset = UNSET
    department: str | Unset = UNSET
    job_title: str | Unset = UNSET
    mail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        company_name = self.company_name

        department = self.department

        job_title = self.job_title

        mail = self.mail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if department is not UNSET:
            field_dict["department"] = department
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if mail is not UNSET:
            field_dict["mail"] = mail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        company_name = d.pop("companyName", UNSET)

        department = d.pop("department", UNSET)

        job_title = d.pop("jobTitle", UNSET)

        mail = d.pop("mail", UNSET)

        entra_id_tenant_org_contact_filter_browse_spec = cls(
            display_name=display_name,
            company_name=company_name,
            department=department,
            job_title=job_title,
            mail=mail,
        )

        entra_id_tenant_org_contact_filter_browse_spec.additional_properties = d
        return entra_id_tenant_org_contact_filter_browse_spec

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
