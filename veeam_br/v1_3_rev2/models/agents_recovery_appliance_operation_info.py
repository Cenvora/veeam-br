from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_agents_recovery_appliance_operation_type import EAgentsRecoveryApplianceOperationType

T = TypeVar("T", bound="AgentsRecoveryApplianceOperationInfo")


@_attrs_define
class AgentsRecoveryApplianceOperationInfo:
    """Availability of an operation for the Agent Recovery Appliance.

    Attributes:
        operation (EAgentsRecoveryApplianceOperationType): Defines action for an agent recovery appliance.
        enabled (bool): If `true`, the operation is available for the Agent Recovery Appliance.
    """

    operation: EAgentsRecoveryApplianceOperationType
    enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation.value

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation = EAgentsRecoveryApplianceOperationType(d.pop("operation"))

        enabled = d.pop("enabled")

        agents_recovery_appliance_operation_info = cls(
            operation=operation,
            enabled=enabled,
        )

        agents_recovery_appliance_operation_info.additional_properties = d
        return agents_recovery_appliance_operation_info

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
