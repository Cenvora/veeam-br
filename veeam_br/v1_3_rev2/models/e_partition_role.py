from enum import Enum


class EPartitionRole(str, Enum):
    BOOT = "Boot"
    MSR = "Msr"
    NONE = "None"
    RECOVERY = "Recovery"
    SYSTEM = "System"

    def __str__(self) -> str:
        return str(self.value)
