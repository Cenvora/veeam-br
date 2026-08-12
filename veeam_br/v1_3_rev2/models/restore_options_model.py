from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.restore_option_model import RestoreOptionModel


T = TypeVar("T", bound="RestoreOptionsModel")


@_attrs_define
class RestoreOptionsModel:
    """Restore options.

    Attributes:
        all_options (bool): If `true`, the role can use all restore types available in Veeam Backup & Replication. If
            `false`, the role is restricted to the restore types listed in the `restoreOptions` property.
        restore_options (list[RestoreOptionModel] | Unset): Restore types that the role can use. Required if
            `allOptions` is `false`.
    """

    all_options: bool
    restore_options: list[RestoreOptionModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_options = self.all_options

        restore_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.restore_options, Unset):
            restore_options = []
            for restore_options_item_data in self.restore_options:
                restore_options_item = restore_options_item_data.to_dict()
                restore_options.append(restore_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allOptions": all_options,
            }
        )
        if restore_options is not UNSET:
            field_dict["restoreOptions"] = restore_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.restore_option_model import RestoreOptionModel

        d = dict(src_dict)
        all_options = d.pop("allOptions")

        _restore_options = d.pop("restoreOptions", UNSET)
        restore_options: list[RestoreOptionModel] | Unset = UNSET
        if _restore_options is not UNSET:
            restore_options = []
            for restore_options_item_data in _restore_options:
                restore_options_item = RestoreOptionModel.from_dict(restore_options_item_data)

                restore_options.append(restore_options_item)

        restore_options_model = cls(
            all_options=all_options,
            restore_options=restore_options,
        )

        restore_options_model.additional_properties = d
        return restore_options_model

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
