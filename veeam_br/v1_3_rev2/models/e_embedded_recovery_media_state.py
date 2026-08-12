from enum import Enum


class EEmbeddedRecoveryMediaState(str, Enum):
    CREATED = "Created"
    FAILED = "Failed"
    NOTCREATED = "NotCreated"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
