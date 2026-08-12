from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_flr_mount_mode_server_type import EFlrMountModeServerType

if TYPE_CHECKING:
    from ..models.linux_flr_helper_host_model import LinuxFlrHelperHostModel


T = TypeVar("T", bound="LinuxHelperHostFlrMountServerSettings")


@_attrs_define
class LinuxHelperHostFlrMountServerSettings:
    """Mount server settings for file restore from Linux machines when `mountServerType` is `HelperHost`.

    Attributes:
        mount_server_type (EFlrMountModeServerType): Mount server mode.
        helper_host (LinuxFlrHelperHostModel): Helper host settings. Use this option if you want to mount the file
            system to a Linux server added to the backup infrastructure.
    """

    mount_server_type: EFlrMountModeServerType
    helper_host: LinuxFlrHelperHostModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_server_type = self.mount_server_type.value

        helper_host = self.helper_host.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mountServerType": mount_server_type,
                "helperHost": helper_host,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_flr_helper_host_model import LinuxFlrHelperHostModel

        d = dict(src_dict)
        mount_server_type = EFlrMountModeServerType(d.pop("mountServerType"))

        helper_host = LinuxFlrHelperHostModel.from_dict(d.pop("helperHost"))

        linux_helper_host_flr_mount_server_settings = cls(
            mount_server_type=mount_server_type,
            helper_host=helper_host,
        )

        linux_helper_host_flr_mount_server_settings.additional_properties = d
        return linux_helper_host_flr_mount_server_settings

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
