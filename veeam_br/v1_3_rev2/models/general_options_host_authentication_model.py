from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_host_trust_mode import EHostTrustMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneralOptionsHostAuthenticationModel")


@_attrs_define
class GeneralOptionsHostAuthenticationModel:
    """Host authentication settings.

    Attributes:
        mode (EHostTrustMode): Host trust mode.
        trusted_host_count (int | Unset): Number of trusted hosts in the environment. This property is read-only.
    """

    mode: EHostTrustMode
    trusted_host_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        trusted_host_count = self.trusted_host_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if trusted_host_count is not UNSET:
            field_dict["trustedHostCount"] = trusted_host_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = EHostTrustMode(d.pop("mode"))

        trusted_host_count = d.pop("trustedHostCount", UNSET)

        general_options_host_authentication_model = cls(
            mode=mode,
            trusted_host_count=trusted_host_count,
        )

        general_options_host_authentication_model.additional_properties = d
        return general_options_host_authentication_model

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
