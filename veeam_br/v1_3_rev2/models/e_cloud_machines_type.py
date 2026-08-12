from enum import Enum


class ECloudMachinesType(str, Enum):
    AMAZON = "Amazon"
    AZURE = "Azure"

    def __str__(self) -> str:
        return str(self.value)
