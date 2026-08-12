from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CapacityExtentModel")


@_attrs_define
class CapacityExtentModel:
    """Capacity extent.

    Attributes:
        id (UUID): ID of an object storage repository added as a capacity extent.
        crypto_key_id (UUID | Unset): If an object storage repository added as a capacity extent is encrypted, specify
            an ID of a crypto key for decryption.
    """

    id: UUID
    crypto_key_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        crypto_key_id: str | Unset = UNSET
        if not isinstance(self.crypto_key_id, Unset):
            crypto_key_id = str(self.crypto_key_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if crypto_key_id is not UNSET:
            field_dict["cryptoKeyId"] = crypto_key_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        _crypto_key_id = d.pop("cryptoKeyId", UNSET)
        crypto_key_id: UUID | Unset
        if isinstance(_crypto_key_id, Unset):
            crypto_key_id = UNSET
        else:
            crypto_key_id = UUID(_crypto_key_id)

        capacity_extent_model = cls(
            id=id,
            crypto_key_id=crypto_key_id,
        )

        capacity_extent_model.additional_properties = d
        return capacity_extent_model

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
