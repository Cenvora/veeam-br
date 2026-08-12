from enum import Enum


class EDDBoostEncryptionType(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"

    def __str__(self) -> str:
        return str(self.value)
