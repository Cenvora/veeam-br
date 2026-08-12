from enum import Enum


class EEntraIdTenantOrgContactSortingProperty(str, Enum):
    COMPANYNAME = "companyName"
    DEPARTMENT = "department"
    DISPLAYNAME = "displayName"
    JOBTITLE = "jobTitle"
    LASTRESTOREPOINT = "lastRestorePoint"
    MAIL = "mail"
    OBJECTID = "objectId"

    def __str__(self) -> str:
        return str(self.value)
