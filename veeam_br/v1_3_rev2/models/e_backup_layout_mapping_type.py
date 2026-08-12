from enum import Enum


class EBackupLayoutMappingType(str, Enum):
    CUSTOM = "Custom"
    TOORIGINALLAYOUT = "ToOriginalLayout"

    def __str__(self) -> str:
        return str(self.value)
