from enum import Enum


class EAgentsRecoveryAppliancesOrderColumn(str, Enum):
    ADDRESSES = "Addresses"
    CREATIONTIME = "CreationTime"
    HOSTNAME = "HostName"
    ISDETACHED = "IsDetached"
    LASTCONTACTTIME = "LastContactTime"
    PLATFORMTYPE = "PlatformType"
    VERSION = "Version"

    def __str__(self) -> str:
        return str(self.value)
