from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_scope_model import InventoryScopeModel
    from ..models.repository_scope_model import RepositoryScopeModel
    from ..models.restore_permissions_scope_model import RestorePermissionsScopeModel
    from ..models.restore_target_scope_model import RestoreTargetScopeModel


T = TypeVar("T", bound="CustomRoleModel")


@_attrs_define
class CustomRoleModel:
    """Custom role.

    Attributes:
        id (UUID): Role ID.
        name (str): Role name.
        manage_backups (bool): If `true`, the role can create and manage backup jobs.
        manage_restores (bool): If `true`, the role can perform restores from existing backups.
        description (str | Unset): Role description.
        inventory_scope (InventoryScopeModel | Unset): Inventory scope.
        repository_scope (RepositoryScopeModel | Unset): Repository scope.
        restore_permissions_scope (RestorePermissionsScopeModel | Unset): Restore permissions scope.
        restore_target_scope (RestoreTargetScopeModel | Unset): Restore target scope.
    """

    id: UUID
    name: str
    manage_backups: bool
    manage_restores: bool
    description: str | Unset = UNSET
    inventory_scope: InventoryScopeModel | Unset = UNSET
    repository_scope: RepositoryScopeModel | Unset = UNSET
    restore_permissions_scope: RestorePermissionsScopeModel | Unset = UNSET
    restore_target_scope: RestoreTargetScopeModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        manage_backups = self.manage_backups

        manage_restores = self.manage_restores

        description = self.description

        inventory_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inventory_scope, Unset):
            inventory_scope = self.inventory_scope.to_dict()

        repository_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository_scope, Unset):
            repository_scope = self.repository_scope.to_dict()

        restore_permissions_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restore_permissions_scope, Unset):
            restore_permissions_scope = self.restore_permissions_scope.to_dict()

        restore_target_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restore_target_scope, Unset):
            restore_target_scope = self.restore_target_scope.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "manageBackups": manage_backups,
                "manageRestores": manage_restores,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if inventory_scope is not UNSET:
            field_dict["inventoryScope"] = inventory_scope
        if repository_scope is not UNSET:
            field_dict["repositoryScope"] = repository_scope
        if restore_permissions_scope is not UNSET:
            field_dict["restorePermissionsScope"] = restore_permissions_scope
        if restore_target_scope is not UNSET:
            field_dict["restoreTargetScope"] = restore_target_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_scope_model import InventoryScopeModel
        from ..models.repository_scope_model import RepositoryScopeModel
        from ..models.restore_permissions_scope_model import RestorePermissionsScopeModel
        from ..models.restore_target_scope_model import RestoreTargetScopeModel

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        manage_backups = d.pop("manageBackups")

        manage_restores = d.pop("manageRestores")

        description = d.pop("description", UNSET)

        _inventory_scope = d.pop("inventoryScope", UNSET)
        inventory_scope: InventoryScopeModel | Unset
        if isinstance(_inventory_scope, Unset):
            inventory_scope = UNSET
        else:
            inventory_scope = InventoryScopeModel.from_dict(_inventory_scope)

        _repository_scope = d.pop("repositoryScope", UNSET)
        repository_scope: RepositoryScopeModel | Unset
        if isinstance(_repository_scope, Unset):
            repository_scope = UNSET
        else:
            repository_scope = RepositoryScopeModel.from_dict(_repository_scope)

        _restore_permissions_scope = d.pop("restorePermissionsScope", UNSET)
        restore_permissions_scope: RestorePermissionsScopeModel | Unset
        if isinstance(_restore_permissions_scope, Unset):
            restore_permissions_scope = UNSET
        else:
            restore_permissions_scope = RestorePermissionsScopeModel.from_dict(_restore_permissions_scope)

        _restore_target_scope = d.pop("restoreTargetScope", UNSET)
        restore_target_scope: RestoreTargetScopeModel | Unset
        if isinstance(_restore_target_scope, Unset):
            restore_target_scope = UNSET
        else:
            restore_target_scope = RestoreTargetScopeModel.from_dict(_restore_target_scope)

        custom_role_model = cls(
            id=id,
            name=name,
            manage_backups=manage_backups,
            manage_restores=manage_restores,
            description=description,
            inventory_scope=inventory_scope,
            repository_scope=repository_scope,
            restore_permissions_scope=restore_permissions_scope,
            restore_target_scope=restore_target_scope,
        )

        custom_role_model.additional_properties = d
        return custom_role_model

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
