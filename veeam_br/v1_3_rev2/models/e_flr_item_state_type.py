from enum import Enum


class EFlrItemStateType(str, Enum):
    CHANGED = "Changed"
    COMPARING = "Comparing"
    DELETED = "Deleted"
    FAILEDTOCOMPARE = "FailedToCompare"
    NOTAVAILABLE = "NotAvailable"
    UNCHANGED = "Unchanged"

    def __str__(self) -> str:
        return str(self.value)
