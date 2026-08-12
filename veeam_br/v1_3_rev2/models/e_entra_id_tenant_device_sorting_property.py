from enum import Enum


class EEntraIdTenantDeviceSortingProperty(str, Enum):
    ACCOUNTENABLED = "AccountEnabled"
    DEVICEVERSION = "DeviceVersion"
    DISPLAYNAME = "DisplayName"
    LASTRESTOREPOINT = "LastRestorePoint"
    OBJECTID = "ObjectId"
    OPERATINGSYSTEM = "OperatingSystem"
    OPERATINGSYSTEMVERSION = "OperatingSystemVersion"

    def __str__(self) -> str:
        return str(self.value)
