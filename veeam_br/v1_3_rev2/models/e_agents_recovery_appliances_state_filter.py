from enum import Enum


class EAgentsRecoveryAppliancesStateFilter(str, Enum):
    ALL = "All"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"

    def __str__(self) -> str:
        return str(self.value)
