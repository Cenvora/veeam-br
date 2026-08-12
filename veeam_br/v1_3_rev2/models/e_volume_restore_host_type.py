from enum import Enum


class EVolumeRestoreHostType(str, Enum):
    AGENT = "Agent"
    RECOVERYAPPLIANCE = "RecoveryAppliance"

    def __str__(self) -> str:
        return str(self.value)
