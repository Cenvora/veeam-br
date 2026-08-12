from enum import Enum


class EAgentsRecoveryApplianceOperationType(str, Enum):
    REBOOT = "Reboot"

    def __str__(self) -> str:
        return str(self.value)
