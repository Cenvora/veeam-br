from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.entra_id_tenant_revealed_bitlocker_recovery_key_model import (
        EntraIdTenantRevealedBitlockerRecoveryKeyModel,
    )


T = TypeVar("T", bound="EntraIdTenantRevealBitlockerRecoveryKeyResponse")


@_attrs_define
class EntraIdTenantRevealBitlockerRecoveryKeyResponse:
    """BitLocker recovery key.

    Attributes:
        bitlocker_recovery_keys (list[EntraIdTenantRevealedBitlockerRecoveryKeyModel]): Array of revealed BitLocker
            recovery keys.
    """

    bitlocker_recovery_keys: list[EntraIdTenantRevealedBitlockerRecoveryKeyModel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bitlocker_recovery_keys = []
        for bitlocker_recovery_keys_item_data in self.bitlocker_recovery_keys:
            bitlocker_recovery_keys_item = bitlocker_recovery_keys_item_data.to_dict()
            bitlocker_recovery_keys.append(bitlocker_recovery_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bitlockerRecoveryKeys": bitlocker_recovery_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entra_id_tenant_revealed_bitlocker_recovery_key_model import (
            EntraIdTenantRevealedBitlockerRecoveryKeyModel,
        )

        d = dict(src_dict)
        bitlocker_recovery_keys = []
        _bitlocker_recovery_keys = d.pop("bitlockerRecoveryKeys")
        for bitlocker_recovery_keys_item_data in _bitlocker_recovery_keys:
            bitlocker_recovery_keys_item = EntraIdTenantRevealedBitlockerRecoveryKeyModel.from_dict(
                bitlocker_recovery_keys_item_data
            )

            bitlocker_recovery_keys.append(bitlocker_recovery_keys_item)

        entra_id_tenant_reveal_bitlocker_recovery_key_response = cls(
            bitlocker_recovery_keys=bitlocker_recovery_keys,
        )

        entra_id_tenant_reveal_bitlocker_recovery_key_response.additional_properties = d
        return entra_id_tenant_reveal_bitlocker_recovery_key_response

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
