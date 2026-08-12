from enum import Enum


class EDetectionEngine(str, Enum):
    EXTERNAL = "External"
    VEEAMTHREATHUNTER = "VeeamThreatHunter"

    def __str__(self) -> str:
        return str(self.value)
