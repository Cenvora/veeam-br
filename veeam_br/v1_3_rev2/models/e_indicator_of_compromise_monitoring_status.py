from enum import Enum


class EIndicatorOfCompromiseMonitoringStatus(str, Enum):
    ACTIVE = "Active"
    DISABLED = "Disabled"

    def __str__(self) -> str:
        return str(self.value)
