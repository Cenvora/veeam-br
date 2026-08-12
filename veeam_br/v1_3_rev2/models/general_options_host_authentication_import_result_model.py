from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GeneralOptionsHostAuthenticationImportResultModel")


@_attrs_define
class GeneralOptionsHostAuthenticationImportResultModel:
    """Result of the trusted hosts import operation.

    Attributes:
        result (str): Import summary report.
        warnings (list[str]): Array of warning messages for items that could not be imported.
    """

    result: str
    warnings: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = self.result

        warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result = d.pop("result")

        warnings = cast(list[str], d.pop("warnings"))

        general_options_host_authentication_import_result_model = cls(
            result=result,
            warnings=warnings,
        )

        general_options_host_authentication_import_result_model.additional_properties = d
        return general_options_host_authentication_import_result_model

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
