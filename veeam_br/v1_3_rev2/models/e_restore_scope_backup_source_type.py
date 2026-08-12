from enum import Enum


class ERestoreScopeBackupSourceType(str, Enum):
    BACKUP = "Backup"
    COMPUTER = "Computer"
    JOB = "Job"

    def __str__(self) -> str:
        return str(self.value)
