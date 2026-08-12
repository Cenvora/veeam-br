from enum import Enum


class EFileServerHostType(str, Enum):
    BACKUPSERVER = "BackupServer"
    LINUX = "Linux"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)
