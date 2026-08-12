from enum import Enum


class ESessionAlgorithm(str, Enum):
    FULL = "Full"
    INCREMENT = "Increment"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
