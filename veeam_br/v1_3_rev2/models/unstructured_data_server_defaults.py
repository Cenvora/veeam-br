from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_model import RepositoryModel


T = TypeVar("T", bound="UnstructuredDataServerDefaults")


@_attrs_define
class UnstructuredDataServerDefaults:
    """Details on unstructured data servers.

    Attributes:
        default_cache_repository (RepositoryModel | Unset): Backup repository.
    """

    default_cache_repository: RepositoryModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_cache_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_cache_repository, Unset):
            default_cache_repository = self.default_cache_repository.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_cache_repository is not UNSET:
            field_dict["defaultCacheRepository"] = default_cache_repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_model import RepositoryModel

        d = dict(src_dict)
        _default_cache_repository = d.pop("defaultCacheRepository", UNSET)
        default_cache_repository: RepositoryModel | Unset
        if isinstance(_default_cache_repository, Unset):
            default_cache_repository = UNSET
        else:
            default_cache_repository = RepositoryModel.from_dict(_default_cache_repository)

        unstructured_data_server_defaults = cls(
            default_cache_repository=default_cache_repository,
        )

        unstructured_data_server_defaults.additional_properties = d
        return unstructured_data_server_defaults

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
