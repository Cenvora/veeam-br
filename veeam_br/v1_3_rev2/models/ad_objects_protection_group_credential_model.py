from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_individual_computer_connection_type import EIndividualComputerConnectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ad_object_custom_credentials_model import ADObjectCustomCredentialsModel


T = TypeVar("T", bound="ADObjectsProtectionGroupCredentialModel")


@_attrs_define
class ADObjectsProtectionGroupCredentialModel:
    """Authentication settings for Active Directory objects.

    Attributes:
        master_connection_type (EIndividualComputerConnectionType): Authentication method for the protected computer.
        use_custom_credentials (bool): If `true`, custom credentials are used for authenticating with the specified
            Active Directory objects.
        master_credentials_id (UUID | Unset): Master account credentials for authenticating with all Active Directory
            objects in a protection scope.
        custom_credentials (list[ADObjectCustomCredentialsModel] | Unset): Array of credentials for authenticating to
            the specified Active Directory objects.
    """

    master_connection_type: EIndividualComputerConnectionType
    use_custom_credentials: bool
    master_credentials_id: UUID | Unset = UNSET
    custom_credentials: list[ADObjectCustomCredentialsModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_connection_type = self.master_connection_type.value

        use_custom_credentials = self.use_custom_credentials

        master_credentials_id: str | Unset = UNSET
        if not isinstance(self.master_credentials_id, Unset):
            master_credentials_id = str(self.master_credentials_id)

        custom_credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_credentials, Unset):
            custom_credentials = []
            for custom_credentials_item_data in self.custom_credentials:
                custom_credentials_item = custom_credentials_item_data.to_dict()
                custom_credentials.append(custom_credentials_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "masterConnectionType": master_connection_type,
                "useCustomCredentials": use_custom_credentials,
            }
        )
        if master_credentials_id is not UNSET:
            field_dict["masterCredentialsId"] = master_credentials_id
        if custom_credentials is not UNSET:
            field_dict["customCredentials"] = custom_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_object_custom_credentials_model import ADObjectCustomCredentialsModel

        d = dict(src_dict)
        master_connection_type = EIndividualComputerConnectionType(d.pop("masterConnectionType"))

        use_custom_credentials = d.pop("useCustomCredentials")

        _master_credentials_id = d.pop("masterCredentialsId", UNSET)
        master_credentials_id: UUID | Unset
        if isinstance(_master_credentials_id, Unset):
            master_credentials_id = UNSET
        else:
            master_credentials_id = UUID(_master_credentials_id)

        _custom_credentials = d.pop("customCredentials", UNSET)
        custom_credentials: list[ADObjectCustomCredentialsModel] | Unset = UNSET
        if _custom_credentials is not UNSET:
            custom_credentials = []
            for custom_credentials_item_data in _custom_credentials:
                custom_credentials_item = ADObjectCustomCredentialsModel.from_dict(custom_credentials_item_data)

                custom_credentials.append(custom_credentials_item)

        ad_objects_protection_group_credential_model = cls(
            master_connection_type=master_connection_type,
            use_custom_credentials=use_custom_credentials,
            master_credentials_id=master_credentials_id,
            custom_credentials=custom_credentials,
        )

        ad_objects_protection_group_credential_model.additional_properties = d
        return ad_objects_protection_group_credential_model

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
