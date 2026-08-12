from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entra_id_tenant_item_comparison_reference_model import EntraIdTenantItemComparisonReferenceModel
    from ..models.entra_id_tenant_item_recursive_comparison_node import EntraIdTenantItemRecursiveComparisonNode


T = TypeVar("T", bound="EntraIdTenantItemRecursiveComparisonModel")


@_attrs_define
class EntraIdTenantItemRecursiveComparisonModel:
    """Comparison result.

    Attributes:
        exists_in_old_restore_point (bool): If `true`, the item exists in the earlier restore point.
        exists_in_new_restore_point (bool): If `true`, the item exists in the later restore point.
        properties (list[EntraIdTenantItemRecursiveComparisonNode]): Array of properties.
        cache_timestamp (datetime.datetime): Date and time the mount session cache was last updated.
        references (list[EntraIdTenantItemComparisonReferenceModel] | Unset): Array of item references (relationship
            with other items).
    """

    exists_in_old_restore_point: bool
    exists_in_new_restore_point: bool
    properties: list[EntraIdTenantItemRecursiveComparisonNode]
    cache_timestamp: datetime.datetime
    references: list[EntraIdTenantItemComparisonReferenceModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exists_in_old_restore_point = self.exists_in_old_restore_point

        exists_in_new_restore_point = self.exists_in_new_restore_point

        properties = []
        for properties_item_data in self.properties:
            properties_item = properties_item_data.to_dict()
            properties.append(properties_item)

        cache_timestamp = self.cache_timestamp.isoformat()

        references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "existsInOldRestorePoint": exists_in_old_restore_point,
                "existsInNewRestorePoint": exists_in_new_restore_point,
                "properties": properties,
                "cacheTimestamp": cache_timestamp,
            }
        )
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entra_id_tenant_item_comparison_reference_model import EntraIdTenantItemComparisonReferenceModel
        from ..models.entra_id_tenant_item_recursive_comparison_node import EntraIdTenantItemRecursiveComparisonNode

        d = dict(src_dict)
        exists_in_old_restore_point = d.pop("existsInOldRestorePoint")

        exists_in_new_restore_point = d.pop("existsInNewRestorePoint")

        properties = []
        _properties = d.pop("properties")
        for properties_item_data in _properties:
            properties_item = EntraIdTenantItemRecursiveComparisonNode.from_dict(properties_item_data)

            properties.append(properties_item)

        cache_timestamp = isoparse(d.pop("cacheTimestamp"))

        _references = d.pop("references", UNSET)
        references: list[EntraIdTenantItemComparisonReferenceModel] | Unset = UNSET
        if _references is not UNSET:
            references = []
            for references_item_data in _references:
                references_item = EntraIdTenantItemComparisonReferenceModel.from_dict(references_item_data)

                references.append(references_item)

        entra_id_tenant_item_recursive_comparison_model = cls(
            exists_in_old_restore_point=exists_in_old_restore_point,
            exists_in_new_restore_point=exists_in_new_restore_point,
            properties=properties,
            cache_timestamp=cache_timestamp,
            references=references,
        )

        entra_id_tenant_item_recursive_comparison_model.additional_properties = d
        return entra_id_tenant_item_recursive_comparison_model

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
