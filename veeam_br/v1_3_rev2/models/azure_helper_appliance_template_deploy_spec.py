from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_helper_appliance_template_spec import AzureHelperApplianceTemplateSpec


T = TypeVar("T", bound="AzureHelperApplianceTemplateDeploySpec")


@_attrs_define
class AzureHelperApplianceTemplateDeploySpec:
    """An array of Azure helper appliance templates to deploy.

    Attributes:
        templates (list[AzureHelperApplianceTemplateSpec] | Unset): Array of Azure helper appliance templates to deploy.
    """

    templates: list[AzureHelperApplianceTemplateSpec] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for templates_item_data in self.templates:
                templates_item = templates_item_data.to_dict()
                templates.append(templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if templates is not UNSET:
            field_dict["templates"] = templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_helper_appliance_template_spec import AzureHelperApplianceTemplateSpec

        d = dict(src_dict)
        _templates = d.pop("templates", UNSET)
        templates: list[AzureHelperApplianceTemplateSpec] | Unset = UNSET
        if _templates is not UNSET:
            templates = []
            for templates_item_data in _templates:
                templates_item = AzureHelperApplianceTemplateSpec.from_dict(templates_item_data)

                templates.append(templates_item)

        azure_helper_appliance_template_deploy_spec = cls(
            templates=templates,
        )

        azure_helper_appliance_template_deploy_spec.additional_properties = d
        return azure_helper_appliance_template_deploy_spec

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
