from enum import Enum


class EFileBackupMaskType(str, Enum):
    LEGACY = "Legacy"
    PATH = "Path"
    WILDCARD = "Wildcard"

    def __str__(self) -> str:
        return str(self.value)
