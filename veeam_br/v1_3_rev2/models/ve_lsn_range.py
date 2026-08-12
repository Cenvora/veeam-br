from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ve_lsn import VeLsn


T = TypeVar("T", bound="VeLsnRange")


@_attrs_define
class VeLsnRange:
    """LSN Range.

    Attributes:
        from_ (VeLsn): LSN.
        to (VeLsn): LSN.
    """

    from_: VeLsn
    to: VeLsn
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.to_dict()

        to = self.to.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ve_lsn import VeLsn

        d = dict(src_dict)
        from_ = VeLsn.from_dict(d.pop("from"))

        to = VeLsn.from_dict(d.pop("to"))

        ve_lsn_range = cls(
            from_=from_,
            to=to,
        )

        ve_lsn_range.additional_properties = d
        return ve_lsn_range

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
