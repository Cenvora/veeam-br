from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_helper_appliance_template_status import EHelperApplianceTemplateStatus

T = TypeVar("T", bound="HelperApplianceTemplateStateModel")


@_attrs_define
class HelperApplianceTemplateStateModel:
    """Helper appliance template state.

    Attributes:
        id (UUID): Helper appliance template ID.
        subscription_id (UUID): Azure subscription ID.
        location (str): Azure region where the helper appliance template is deployed.
        status (EHelperApplianceTemplateStatus): Helper appliance template status.
    """

    id: UUID
    subscription_id: UUID
    location: str
    status: EHelperApplianceTemplateStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        subscription_id = str(self.subscription_id)

        location = self.location

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "subscriptionId": subscription_id,
                "location": location,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        subscription_id = UUID(d.pop("subscriptionId"))

        location = d.pop("location")

        status = EHelperApplianceTemplateStatus(d.pop("status"))

        helper_appliance_template_state_model = cls(
            id=id,
            subscription_id=subscription_id,
            location=location,
            status=status,
        )

        helper_appliance_template_state_model.additional_properties = d
        return helper_appliance_template_state_model

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
