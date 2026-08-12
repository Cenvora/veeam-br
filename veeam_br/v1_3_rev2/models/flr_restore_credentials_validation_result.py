from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrRestoreCredentialsValidationResult")


@_attrs_define
class FlrRestoreCredentialsValidationResult:
    """File-level restore target machine credentials validation result.

    Attributes:
        is_successful (bool): If `true`, the credentials validation is successful.
        message (str): Message that explains the credentials validation result.
        credentials_id (UUID | Unset): Credentials record used to access the guest OS if needed during the restore
    """

    is_successful: bool
    message: str
    credentials_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_successful = self.is_successful

        message = self.message

        credentials_id: str | Unset = UNSET
        if not isinstance(self.credentials_id, Unset):
            credentials_id = str(self.credentials_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isSuccessful": is_successful,
                "message": message,
            }
        )
        if credentials_id is not UNSET:
            field_dict["credentialsId"] = credentials_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_successful = d.pop("isSuccessful")

        message = d.pop("message")

        _credentials_id = d.pop("credentialsId", UNSET)
        credentials_id: UUID | Unset
        if isinstance(_credentials_id, Unset):
            credentials_id = UNSET
        else:
            credentials_id = UUID(_credentials_id)

        flr_restore_credentials_validation_result = cls(
            is_successful=is_successful,
            message=message,
            credentials_id=credentials_id,
        )

        flr_restore_credentials_validation_result.additional_properties = d
        return flr_restore_credentials_validation_result

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
