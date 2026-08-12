from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.e_platform_type import EPlatformType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agents_recovery_appliance_operation_info import AgentsRecoveryApplianceOperationInfo


T = TypeVar("T", bound="AgentRecoveryApplianceModel")


@_attrs_define
class AgentRecoveryApplianceModel:
    """Agent recovery appliance.

    Attributes:
        id (UUID): Agent recovery appliance unique identifier.
        host_name (str): Agent recovery appliance host name.
        version (str): Recovery appliance Veeam Agent version.
        endpoint (str): Agent recovery appliance connection IP address.
        addresses (list[str]): Recovery appliance IP addresses.
        port (int): Recovery appliance port.
        creation_time (datetime.datetime): Date and time when a recovery appliance connected to backup server.
        is_verified (bool): If `true`, the recovery appliance is verified.
        is_detached (bool): If `true`, the recovery appliance is disconnected from the backup server.
        can_expire (bool): If `true`, the connection to the recovery appliance can expire over time.
        verification_phrase (str): String which helps to identify recovery appliance and is also shown on recovery
            appliance side.
        used_personal_certificate (bool): If `true`, a personal certificate of the recovery appliance was used to
            connect to the backup server.
        last_contact_time (datetime.datetime): Date and time of last contact with a recovery appliance.
        platform_id (UUID): Platform id of a recovery appliance.
        platform_type (EPlatformType): Platform type.<p>`Test` is the platform of SureBackup content scan job
            (`SureBackupContentScan`) — backup verification and content scanning with antivirus software or YARA rules.</p>
        operations (list[AgentsRecoveryApplianceOperationInfo]): Array of operations available for the Agent Recovery
            Appliance.
        host_bios_id (UUID | Unset): Recovery appliance host BIOS ID.
        last_known_host_name (str | Unset): Last known host name.
    """

    id: UUID
    host_name: str
    version: str
    endpoint: str
    addresses: list[str]
    port: int
    creation_time: datetime.datetime
    is_verified: bool
    is_detached: bool
    can_expire: bool
    verification_phrase: str
    used_personal_certificate: bool
    last_contact_time: datetime.datetime
    platform_id: UUID
    platform_type: EPlatformType
    operations: list[AgentsRecoveryApplianceOperationInfo]
    host_bios_id: UUID | Unset = UNSET
    last_known_host_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        host_name = self.host_name

        version = self.version

        endpoint = self.endpoint

        addresses = self.addresses

        port = self.port

        creation_time = self.creation_time.isoformat()

        is_verified = self.is_verified

        is_detached = self.is_detached

        can_expire = self.can_expire

        verification_phrase = self.verification_phrase

        used_personal_certificate = self.used_personal_certificate

        last_contact_time = self.last_contact_time.isoformat()

        platform_id = str(self.platform_id)

        platform_type = self.platform_type.value

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()
            operations.append(operations_item)

        host_bios_id: str | Unset = UNSET
        if not isinstance(self.host_bios_id, Unset):
            host_bios_id = str(self.host_bios_id)

        last_known_host_name = self.last_known_host_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "hostName": host_name,
                "version": version,
                "endpoint": endpoint,
                "addresses": addresses,
                "port": port,
                "creationTime": creation_time,
                "isVerified": is_verified,
                "isDetached": is_detached,
                "canExpire": can_expire,
                "verificationPhrase": verification_phrase,
                "usedPersonalCertificate": used_personal_certificate,
                "lastContactTime": last_contact_time,
                "platformId": platform_id,
                "platformType": platform_type,
                "operations": operations,
            }
        )
        if host_bios_id is not UNSET:
            field_dict["hostBiosId"] = host_bios_id
        if last_known_host_name is not UNSET:
            field_dict["lastKnownHostName"] = last_known_host_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agents_recovery_appliance_operation_info import AgentsRecoveryApplianceOperationInfo

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        host_name = d.pop("hostName")

        version = d.pop("version")

        endpoint = d.pop("endpoint")

        addresses = cast(list[str], d.pop("addresses"))

        port = d.pop("port")

        creation_time = isoparse(d.pop("creationTime"))

        is_verified = d.pop("isVerified")

        is_detached = d.pop("isDetached")

        can_expire = d.pop("canExpire")

        verification_phrase = d.pop("verificationPhrase")

        used_personal_certificate = d.pop("usedPersonalCertificate")

        last_contact_time = isoparse(d.pop("lastContactTime"))

        platform_id = UUID(d.pop("platformId"))

        platform_type = EPlatformType(d.pop("platformType"))

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = AgentsRecoveryApplianceOperationInfo.from_dict(operations_item_data)

            operations.append(operations_item)

        _host_bios_id = d.pop("hostBiosId", UNSET)
        host_bios_id: UUID | Unset
        if isinstance(_host_bios_id, Unset):
            host_bios_id = UNSET
        else:
            host_bios_id = UUID(_host_bios_id)

        last_known_host_name = d.pop("lastKnownHostName", UNSET)

        agent_recovery_appliance_model = cls(
            id=id,
            host_name=host_name,
            version=version,
            endpoint=endpoint,
            addresses=addresses,
            port=port,
            creation_time=creation_time,
            is_verified=is_verified,
            is_detached=is_detached,
            can_expire=can_expire,
            verification_phrase=verification_phrase,
            used_personal_certificate=used_personal_certificate,
            last_contact_time=last_contact_time,
            platform_id=platform_id,
            platform_type=platform_type,
            operations=operations,
            host_bios_id=host_bios_id,
            last_known_host_name=last_known_host_name,
        )

        agent_recovery_appliance_model.additional_properties = d
        return agent_recovery_appliance_model

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
