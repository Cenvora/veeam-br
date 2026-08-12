from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_agent_discovered_entity_status import EAgentDiscoveredEntityStatus

T = TypeVar("T", bound="AgentStateModel")


@_attrs_define
class AgentStateModel:
    """Agent state.

    Attributes:
        id (UUID): Agent ID.
        name (str): Agent name.
        status (EAgentDiscoveredEntityStatus): Status of the agent.
    """

    id: UUID
    name: str
    status: EAgentDiscoveredEntityStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        status = EAgentDiscoveredEntityStatus(d.pop("status"))

        agent_state_model = cls(
            id=id,
            name=name,
            status=status,
        )

        agent_state_model.additional_properties = d
        return agent_state_model

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
