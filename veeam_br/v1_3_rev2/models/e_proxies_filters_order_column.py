from enum import Enum


class EProxiesFiltersOrderColumn(str, Enum):
    DESCRIPTION = "Description"
    HOSTNAME = "HostName"
    NAME = "Name"
    STATUS = "Status"
    TYPE = "Type"

    def __str__(self) -> str:
        return str(self.value)
