from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HighAvailabilityClusterStatesModel")


@_attrs_define
class HighAvailabilityClusterStatesModel:
    """High Availability cluster states.

    Attributes:
        is_creation_in_progress (bool): If `true`, the HA cluster creation process is currently running.
        is_failover_in_progress (bool): If `true`, an HA cluster failover or switchover operation is currently in
            progress.
        is_removal_in_progress (bool): If `true`, the HA cluster removal operation is currently running.
        is_first_launch_after_failover (bool): If `true`, this is the first launch of the service after a failover or
            switchover.
        is_cluster_endpoint_migration_in_progress (bool): If `true`, migration of the cluster endpoint IP is currently
            in progress.
        last_online_time_utc (str): Timestamp (UTC) when the cluster was last observed online.
        is_online (bool): If `true`, the cluster is currently online.
        is_secondary_reinit_in_progress (bool): If `true`, the secondary node reinitialization process is currently
            running.
        is_maintenance_in_progress (bool): If `true`, the HA maintenance job is running.
    """

    is_creation_in_progress: bool
    is_failover_in_progress: bool
    is_removal_in_progress: bool
    is_first_launch_after_failover: bool
    is_cluster_endpoint_migration_in_progress: bool
    last_online_time_utc: str
    is_online: bool
    is_secondary_reinit_in_progress: bool
    is_maintenance_in_progress: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_creation_in_progress = self.is_creation_in_progress

        is_failover_in_progress = self.is_failover_in_progress

        is_removal_in_progress = self.is_removal_in_progress

        is_first_launch_after_failover = self.is_first_launch_after_failover

        is_cluster_endpoint_migration_in_progress = self.is_cluster_endpoint_migration_in_progress

        last_online_time_utc = self.last_online_time_utc

        is_online = self.is_online

        is_secondary_reinit_in_progress = self.is_secondary_reinit_in_progress

        is_maintenance_in_progress = self.is_maintenance_in_progress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isCreationInProgress": is_creation_in_progress,
                "isFailoverInProgress": is_failover_in_progress,
                "isRemovalInProgress": is_removal_in_progress,
                "isFirstLaunchAfterFailover": is_first_launch_after_failover,
                "isClusterEndpointMigrationInProgress": is_cluster_endpoint_migration_in_progress,
                "lastOnlineTimeUtc": last_online_time_utc,
                "isOnline": is_online,
                "isSecondaryReinitInProgress": is_secondary_reinit_in_progress,
                "isMaintenanceInProgress": is_maintenance_in_progress,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_creation_in_progress = d.pop("isCreationInProgress")

        is_failover_in_progress = d.pop("isFailoverInProgress")

        is_removal_in_progress = d.pop("isRemovalInProgress")

        is_first_launch_after_failover = d.pop("isFirstLaunchAfterFailover")

        is_cluster_endpoint_migration_in_progress = d.pop("isClusterEndpointMigrationInProgress")

        last_online_time_utc = d.pop("lastOnlineTimeUtc")

        is_online = d.pop("isOnline")

        is_secondary_reinit_in_progress = d.pop("isSecondaryReinitInProgress")

        is_maintenance_in_progress = d.pop("isMaintenanceInProgress")

        high_availability_cluster_states_model = cls(
            is_creation_in_progress=is_creation_in_progress,
            is_failover_in_progress=is_failover_in_progress,
            is_removal_in_progress=is_removal_in_progress,
            is_first_launch_after_failover=is_first_launch_after_failover,
            is_cluster_endpoint_migration_in_progress=is_cluster_endpoint_migration_in_progress,
            last_online_time_utc=last_online_time_utc,
            is_online=is_online,
            is_secondary_reinit_in_progress=is_secondary_reinit_in_progress,
            is_maintenance_in_progress=is_maintenance_in_progress,
        )

        high_availability_cluster_states_model.additional_properties = d
        return high_availability_cluster_states_model

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
