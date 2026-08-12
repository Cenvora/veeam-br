from enum import Enum


class EOSBitness(str, Enum):
    PPC64LE = "PPC64le"
    UNKNOWN = "Unknown"
    X64 = "x64"
    X86 = "x86"

    def __str__(self) -> str:
        return str(self.value)
