from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UnstructuredDataArchiveRetrievalSpec")


@_attrs_define
class UnstructuredDataArchiveRetrievalSpec:
    """Settings for prolonging a cold storage retrieval operation.

    Attributes:
        retrieval_operation_id (UUID): Retrieval operation id.
        availability_period_days (int): Number of days, the retrieved files must be kept available.
    """

    retrieval_operation_id: UUID
    availability_period_days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retrieval_operation_id = str(self.retrieval_operation_id)

        availability_period_days = self.availability_period_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retrievalOperationId": retrieval_operation_id,
                "availabilityPeriodDays": availability_period_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retrieval_operation_id = UUID(d.pop("retrievalOperationId"))

        availability_period_days = d.pop("availabilityPeriodDays")

        unstructured_data_archive_retrieval_spec = cls(
            retrieval_operation_id=retrieval_operation_id,
            availability_period_days=availability_period_days,
        )

        unstructured_data_archive_retrieval_spec.additional_properties = d
        return unstructured_data_archive_retrieval_spec

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
