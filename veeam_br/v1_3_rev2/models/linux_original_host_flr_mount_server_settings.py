from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_flr_mount_mode_server_type import EFlrMountModeServerType

if TYPE_CHECKING:
    from ..models.linux_flr_original_host_spec import LinuxFlrOriginalHostSpec


T = TypeVar("T", bound="LinuxOriginalHostFlrMountServerSettings")


@_attrs_define
class LinuxOriginalHostFlrMountServerSettings:
    """Mount server settings for file restore from Linux machines when `mountServerType` is `OriginalHost`.

    Attributes:
        mount_server_type (EFlrMountModeServerType): Mount server mode.
        original_host (LinuxFlrOriginalHostSpec): Original host settings. Use this option if you want to mount the file
            system to the original machine.
    """

    mount_server_type: EFlrMountModeServerType
    original_host: LinuxFlrOriginalHostSpec
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_server_type = self.mount_server_type.value

        original_host = self.original_host.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mountServerType": mount_server_type,
                "originalHost": original_host,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_flr_original_host_spec import LinuxFlrOriginalHostSpec

        d = dict(src_dict)
        mount_server_type = EFlrMountModeServerType(d.pop("mountServerType"))

        original_host = LinuxFlrOriginalHostSpec.from_dict(d.pop("originalHost"))

        linux_original_host_flr_mount_server_settings = cls(
            mount_server_type=mount_server_type,
            original_host=original_host,
        )

        linux_original_host_flr_mount_server_settings.additional_properties = d
        return linux_original_host_flr_mount_server_settings

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
