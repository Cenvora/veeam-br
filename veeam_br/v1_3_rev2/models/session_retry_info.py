from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionRetryInfo")


@_attrs_define
class SessionRetryInfo:
    """Retry metadata for a backup session. Present only when the session is a retry of a previous run.

    Attributes:
        is_recheck_retry (bool): If `true`, this retry session is a health-check retry. If `false`, this retry session
            is a plain retry triggered by the automatic retry policy after a failed run.
        retry_number (int | None | Unset): Ordinal of this retry within the run chain. For plain retries, the 1-based
            position in the chain excluding the original run. For health-check retries, the count of health-check retries up
            to and including this row. The value may be absent when a health-check retry precedes this plain retry in the
            chain, in which case the retry cannot be numbered.
    """

    is_recheck_retry: bool
    retry_number: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_recheck_retry = self.is_recheck_retry

        retry_number: int | None | Unset
        if isinstance(self.retry_number, Unset):
            retry_number = UNSET
        else:
            retry_number = self.retry_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isRecheckRetry": is_recheck_retry,
            }
        )
        if retry_number is not UNSET:
            field_dict["retryNumber"] = retry_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_recheck_retry = d.pop("isRecheckRetry")

        def _parse_retry_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_number = _parse_retry_number(d.pop("retryNumber", UNSET))

        session_retry_info = cls(
            is_recheck_retry=is_recheck_retry,
            retry_number=retry_number,
        )

        session_retry_info.additional_properties = d
        return session_retry_info

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
