from enum import Enum


class EHostTrustMode(str, Enum):
    TRUSTALL = "TrustAll"
    TRUSTSPECIFIED = "TrustSpecified"

    def __str__(self) -> str:
        return str(self.value)
