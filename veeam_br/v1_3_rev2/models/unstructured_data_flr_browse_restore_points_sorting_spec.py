from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_sort_expression_direction_type import ESortExpressionDirectionType
from ..models.e_unstructured_data_flr_browse_restore_points_sorting_property import (
    EUnstructuredDataFlrBrowseRestorePointsSortingProperty,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredDataFlrBrowseRestorePointsSortingSpec")


@_attrs_define
class UnstructuredDataFlrBrowseRestorePointsSortingSpec:
    """Sorting options.

    Attributes:
        property_ (EUnstructuredDataFlrBrowseRestorePointsSortingProperty | Unset): Sorting property.
        direction (ESortExpressionDirectionType | Unset): Sorting order.
    """

    property_: EUnstructuredDataFlrBrowseRestorePointsSortingProperty | Unset = UNSET
    direction: ESortExpressionDirectionType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_: str | Unset = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.value

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_ is not UNSET:
            field_dict["property"] = property_
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _property_ = d.pop("property", UNSET)
        property_: EUnstructuredDataFlrBrowseRestorePointsSortingProperty | Unset
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = EUnstructuredDataFlrBrowseRestorePointsSortingProperty(_property_)

        _direction = d.pop("direction", UNSET)
        direction: ESortExpressionDirectionType | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = ESortExpressionDirectionType(_direction)

        unstructured_data_flr_browse_restore_points_sorting_spec = cls(
            property_=property_,
            direction=direction,
        )

        unstructured_data_flr_browse_restore_points_sorting_spec.additional_properties = d
        return unstructured_data_flr_browse_restore_points_sorting_spec

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
