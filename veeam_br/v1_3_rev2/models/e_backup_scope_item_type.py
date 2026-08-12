from enum import Enum


class EBackupScopeItemType(str, Enum):
    BACKUP = "Backup"
    SNAPSHOT = "Snapshot"

    def __str__(self) -> str:
        return str(self.value)
