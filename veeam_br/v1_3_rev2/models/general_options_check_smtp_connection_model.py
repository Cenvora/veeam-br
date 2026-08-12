from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneralOptionsCheckSmtpConnectionModel")


@_attrs_define
class GeneralOptionsCheckSmtpConnectionModel:
    """SMTP server connection check result.

    Attributes:
        is_valid (bool): If `true`, the certificate is valid.
        thumbprints (list[str] | Unset): Array of untrusted certificate thumbprints. Empty array if the certificate is
            trusted.
    """

    is_valid: bool
    thumbprints: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_valid = self.is_valid

        thumbprints: list[str] | Unset = UNSET
        if not isinstance(self.thumbprints, Unset):
            thumbprints = self.thumbprints

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isValid": is_valid,
            }
        )
        if thumbprints is not UNSET:
            field_dict["thumbprints"] = thumbprints

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_valid = d.pop("isValid")

        thumbprints = cast(list[str], d.pop("thumbprints", UNSET))

        general_options_check_smtp_connection_model = cls(
            is_valid=is_valid,
            thumbprints=thumbprints,
        )

        general_options_check_smtp_connection_model.additional_properties = d
        return general_options_check_smtp_connection_model

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
