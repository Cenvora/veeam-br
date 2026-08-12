from enum import Enum


class EAclRights(str, Enum):
    FULL = "full"
    RESTORE = "restore"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
