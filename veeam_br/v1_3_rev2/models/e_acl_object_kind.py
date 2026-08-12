from enum import Enum


class EAclObjectKind(str, Enum):
    BACKUP = "backup"
    BACKUPJOB = "backupJob"

    def __str__(self) -> str:
        return str(self.value)
