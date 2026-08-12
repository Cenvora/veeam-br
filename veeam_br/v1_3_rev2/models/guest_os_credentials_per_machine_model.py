from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_object_model import InventoryObjectModel
    from ..models.specified_guest_os_credentials_model import SpecifiedGuestOsCredentialsModel


T = TypeVar("T", bound="GuestOsCredentialsPerMachineModel")


@_attrs_define
class GuestOsCredentialsPerMachineModel:
    """Settings for per-machine guest OS credentials.

    Attributes:
        vm_object (InventoryObjectModel): Inventory object properties.
        credentials (list[SpecifiedGuestOsCredentialsModel] | Unset): Array of credentials assigned to the machine.
            Maximum 2 entries: at most one Linux and one Standard or ManagedService.
        default (bool | Unset): If `true`, Veeam Backup & Replication will use job-level credentials.
    """

    vm_object: InventoryObjectModel
    credentials: list[SpecifiedGuestOsCredentialsModel] | Unset = UNSET
    default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vm_object = self.vm_object.to_dict()

        credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = []
            for credentials_item_data in self.credentials:
                credentials_item = credentials_item_data.to_dict()
                credentials.append(credentials_item)

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vmObject": vm_object,
            }
        )
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_object_model import InventoryObjectModel
        from ..models.specified_guest_os_credentials_model import SpecifiedGuestOsCredentialsModel

        d = dict(src_dict)
        vm_object = InventoryObjectModel.from_dict(d.pop("vmObject"))

        _credentials = d.pop("credentials", UNSET)
        credentials: list[SpecifiedGuestOsCredentialsModel] | Unset = UNSET
        if _credentials is not UNSET:
            credentials = []
            for credentials_item_data in _credentials:
                credentials_item = SpecifiedGuestOsCredentialsModel.from_dict(credentials_item_data)

                credentials.append(credentials_item)

        default = d.pop("default", UNSET)

        guest_os_credentials_per_machine_model = cls(
            vm_object=vm_object,
            credentials=credentials,
            default=default,
        )

        guest_os_credentials_per_machine_model.additional_properties = d
        return guest_os_credentials_per_machine_model

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
