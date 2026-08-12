from enum import Enum


class ExportLogsScopeType(str, Enum):
    HOSTS = "Hosts"
    JOBS = "Jobs"

    def __str__(self) -> str:
        return str(self.value)
