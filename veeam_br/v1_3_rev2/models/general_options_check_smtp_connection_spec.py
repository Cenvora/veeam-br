from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.advanced_smtp_options_model import AdvancedSmtpOptionsModel


T = TypeVar("T", bound="GeneralOptionsCheckSmtpConnectionSpec")


@_attrs_define
class GeneralOptionsCheckSmtpConnectionSpec:
    """SMTP server connection check settings.

    Attributes:
        smtp_server_name (str): Full DNS name or IP address of the SMTP server.
        advanced_smtp_options (AdvancedSmtpOptionsModel): Advanced global email notification settings.
    """

    smtp_server_name: str
    advanced_smtp_options: AdvancedSmtpOptionsModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        smtp_server_name = self.smtp_server_name

        advanced_smtp_options = self.advanced_smtp_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "smtpServerName": smtp_server_name,
                "advancedSmtpOptions": advanced_smtp_options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advanced_smtp_options_model import AdvancedSmtpOptionsModel

        d = dict(src_dict)
        smtp_server_name = d.pop("smtpServerName")

        advanced_smtp_options = AdvancedSmtpOptionsModel.from_dict(d.pop("advancedSmtpOptions"))

        general_options_check_smtp_connection_spec = cls(
            smtp_server_name=smtp_server_name,
            advanced_smtp_options=advanced_smtp_options,
        )

        general_options_check_smtp_connection_spec.additional_properties = d
        return general_options_check_smtp_connection_spec

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
