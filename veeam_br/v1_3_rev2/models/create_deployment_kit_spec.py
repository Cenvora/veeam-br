from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDeploymentKitSpec")


@_attrs_define
class CreateDeploymentKitSpec:
    """Deployment kit settings.

    Attributes:
        validity_period_hours (int | Unset): Number of hours before the certificate in the deployment kit expires.
            Permitted values are 1–8760. Default: 720.
        include_windows_packages (bool | Unset): If `true`, the deployment kit includes Windows packages. Default: True.
        include_linux_packages (bool | Unset): If `true`, the deployment kit includes Linux packages. Default: False.
        include_unix_packages (bool | Unset): If `true`, the deployment kit includes Unix packages. Default: False.
    """

    validity_period_hours: int | Unset = 720
    include_windows_packages: bool | Unset = True
    include_linux_packages: bool | Unset = False
    include_unix_packages: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        validity_period_hours = self.validity_period_hours

        include_windows_packages = self.include_windows_packages

        include_linux_packages = self.include_linux_packages

        include_unix_packages = self.include_unix_packages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if validity_period_hours is not UNSET:
            field_dict["validityPeriodHours"] = validity_period_hours
        if include_windows_packages is not UNSET:
            field_dict["includeWindowsPackages"] = include_windows_packages
        if include_linux_packages is not UNSET:
            field_dict["includeLinuxPackages"] = include_linux_packages
        if include_unix_packages is not UNSET:
            field_dict["includeUnixPackages"] = include_unix_packages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        validity_period_hours = d.pop("validityPeriodHours", UNSET)

        include_windows_packages = d.pop("includeWindowsPackages", UNSET)

        include_linux_packages = d.pop("includeLinuxPackages", UNSET)

        include_unix_packages = d.pop("includeUnixPackages", UNSET)

        create_deployment_kit_spec = cls(
            validity_period_hours=validity_period_hours,
            include_windows_packages=include_windows_packages,
            include_linux_packages=include_linux_packages,
            include_unix_packages=include_unix_packages,
        )

        create_deployment_kit_spec.additional_properties = d
        return create_deployment_kit_spec

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
