from enum import Enum


class EPowerState(str, Enum):
    POWEREDOFF = "PoweredOff"
    POWEREDON = "PoweredOn"
    SUSPENDED = "Suspended"

    def __str__(self) -> str:
        return str(self.value)
