from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AzureHelperApplianceTemplateIdSpec")


@_attrs_define
class AzureHelperApplianceTemplateIdSpec:
    """Azure helper appliance template IDs.

    Attributes:
        template_ids (list[UUID]): Array of Azure helper appliance template IDs.
    """

    template_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_ids = []
        for template_ids_item_data in self.template_ids:
            template_ids_item = str(template_ids_item_data)
            template_ids.append(template_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templateIds": template_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_ids = []
        _template_ids = d.pop("templateIds")
        for template_ids_item_data in _template_ids:
            template_ids_item = UUID(template_ids_item_data)

            template_ids.append(template_ids_item)

        azure_helper_appliance_template_id_spec = cls(
            template_ids=template_ids,
        )

        azure_helper_appliance_template_id_spec.additional_properties = d
        return azure_helper_appliance_template_id_spec

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
