from enum import Enum


class EUserFiltersOrderColumn(str, Enum):
    ISSERVICEACCOUNT = "IsServiceAccount"
    MFAENABLED = "MfaEnabled"
    NAME = "Name"
    TYPE = "Type"

    def __str__(self) -> str:
        return str(self.value)
