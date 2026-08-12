from enum import Enum


class EUnstructuredDataInventoryBrowseSessionsFiltersOrderColumn(str, Enum):
    SERVERNAME = "ServerName"

    def __str__(self) -> str:
        return str(self.value)
