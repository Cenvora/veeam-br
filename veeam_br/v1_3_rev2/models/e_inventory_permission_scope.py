from enum import Enum


class EInventoryPermissionScope(str, Enum):
    ANY = "Any"
    BACKUP = "Backup"
    RESTORE = "Restore"

    def __str__(self) -> str:
        return str(self.value)
