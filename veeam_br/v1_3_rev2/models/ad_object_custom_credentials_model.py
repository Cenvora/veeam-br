from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_individual_computer_connection_type import EIndividualComputerConnectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ad_object_model import ADObjectModel
    from ..models.linux_credentials_spec import LinuxCredentialsSpec


T = TypeVar("T", bound="ADObjectCustomCredentialsModel")


@_attrs_define
class ADObjectCustomCredentialsModel:
    """Credentials for authenticating to the specified Active Directory objects.

    Attributes:
        use_master_credentials (bool): If `true`, protection group-level access settings are used for authenticating
            with the specified Active Directory objects.
        object_ (ADObjectModel): Active Directory object.
        connection_type (EIndividualComputerConnectionType | Unset): Authentication method for the protected computer.
        credentials_id (UUID | Unset): Credentials ID.
        single_use_credentials (LinuxCredentialsSpec | Unset): Settings for single-use credentials.
    """

    use_master_credentials: bool
    object_: ADObjectModel
    connection_type: EIndividualComputerConnectionType | Unset = UNSET
    credentials_id: UUID | Unset = UNSET
    single_use_credentials: LinuxCredentialsSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_master_credentials = self.use_master_credentials

        object_ = self.object_.to_dict()

        connection_type: str | Unset = UNSET
        if not isinstance(self.connection_type, Unset):
            connection_type = self.connection_type.value

        credentials_id: str | Unset = UNSET
        if not isinstance(self.credentials_id, Unset):
            credentials_id = str(self.credentials_id)

        single_use_credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.single_use_credentials, Unset):
            single_use_credentials = self.single_use_credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "useMasterCredentials": use_master_credentials,
                "object": object_,
            }
        )
        if connection_type is not UNSET:
            field_dict["connectionType"] = connection_type
        if credentials_id is not UNSET:
            field_dict["credentialsId"] = credentials_id
        if single_use_credentials is not UNSET:
            field_dict["singleUseCredentials"] = single_use_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_object_model import ADObjectModel
        from ..models.linux_credentials_spec import LinuxCredentialsSpec

        d = dict(src_dict)
        use_master_credentials = d.pop("useMasterCredentials")

        object_ = ADObjectModel.from_dict(d.pop("object"))

        _connection_type = d.pop("connectionType", UNSET)
        connection_type: EIndividualComputerConnectionType | Unset
        if isinstance(_connection_type, Unset):
            connection_type = UNSET
        else:
            connection_type = EIndividualComputerConnectionType(_connection_type)

        _credentials_id = d.pop("credentialsId", UNSET)
        credentials_id: UUID | Unset
        if isinstance(_credentials_id, Unset):
            credentials_id = UNSET
        else:
            credentials_id = UUID(_credentials_id)

        _single_use_credentials = d.pop("singleUseCredentials", UNSET)
        single_use_credentials: LinuxCredentialsSpec | Unset
        if isinstance(_single_use_credentials, Unset):
            single_use_credentials = UNSET
        else:
            single_use_credentials = LinuxCredentialsSpec.from_dict(_single_use_credentials)

        ad_object_custom_credentials_model = cls(
            use_master_credentials=use_master_credentials,
            object_=object_,
            connection_type=connection_type,
            credentials_id=credentials_id,
            single_use_credentials=single_use_credentials,
        )

        ad_object_custom_credentials_model.additional_properties = d
        return ad_object_custom_credentials_model

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
