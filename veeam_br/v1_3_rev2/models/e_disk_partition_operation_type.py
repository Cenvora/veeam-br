from enum import Enum


class EDiskPartitionOperationType(str, Enum):
    REMOVE = "Remove"
    RESIZE = "Resize"
    RESTORE = "Restore"
    UNLOCK = "Unlock"

    def __str__(self) -> str:
        return str(self.value)
