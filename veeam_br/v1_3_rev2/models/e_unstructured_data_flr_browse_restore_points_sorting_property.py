from enum import Enum


class EUnstructuredDataFlrBrowseRestorePointsSortingProperty(str, Enum):
    CREATIONTIME = "CreationTime"

    def __str__(self) -> str:
        return str(self.value)
