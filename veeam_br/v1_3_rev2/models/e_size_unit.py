from enum import Enum


class ESizeUnit(str, Enum):
    BYTE = "Byte"
    GB = "Gb"
    KB = "Kb"
    MB = "Mb"

    def __str__(self) -> str:
        return str(self.value)
