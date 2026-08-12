from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_scope_item_model import RepositoryScopeItemModel


T = TypeVar("T", bound="RepositoryScopeModel")


@_attrs_define
class RepositoryScopeModel:
    """Repository scope.

    Attributes:
        all_repositories (bool): If `true`, the role can use all backup repositories on the backup server when creating
            backup jobs. If `false`, access is restricted to the repositories listed in the `repositories` property.
        repositories (list[RepositoryScopeItemModel] | Unset): Backup repositories that the role can use when creating
            backup jobs. Required if `allRepositories` is `false`.
    """

    all_repositories: bool
    repositories: list[RepositoryScopeItemModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_repositories = self.all_repositories

        repositories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = []
            for repositories_item_data in self.repositories:
                repositories_item = repositories_item_data.to_dict()
                repositories.append(repositories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allRepositories": all_repositories,
            }
        )
        if repositories is not UNSET:
            field_dict["repositories"] = repositories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_scope_item_model import RepositoryScopeItemModel

        d = dict(src_dict)
        all_repositories = d.pop("allRepositories")

        _repositories = d.pop("repositories", UNSET)
        repositories: list[RepositoryScopeItemModel] | Unset = UNSET
        if _repositories is not UNSET:
            repositories = []
            for repositories_item_data in _repositories:
                repositories_item = RepositoryScopeItemModel.from_dict(repositories_item_data)

                repositories.append(repositories_item)

        repository_scope_model = cls(
            all_repositories=all_repositories,
            repositories=repositories,
        )

        repository_scope_model.additional_properties = d
        return repository_scope_model

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
