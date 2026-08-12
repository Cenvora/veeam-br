from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.azure_helper_appliance_template_spec import AzureHelperApplianceTemplateSpec


T = TypeVar("T", bound="AzureHelperApplianceTemplateModel")


@_attrs_define
class AzureHelperApplianceTemplateModel:
    """Azure helper appliance template.

    Attributes:
        id (UUID): Azure helper appliance template ID.
        spec (AzureHelperApplianceTemplateSpec): Azure helper appliance template.
    """

    id: UUID
    spec: AzureHelperApplianceTemplateSpec
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_helper_appliance_template_spec import AzureHelperApplianceTemplateSpec

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        spec = AzureHelperApplianceTemplateSpec.from_dict(d.pop("spec"))

        azure_helper_appliance_template_model = cls(
            id=id,
            spec=spec,
        )

        azure_helper_appliance_template_model.additional_properties = d
        return azure_helper_appliance_template_model

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
