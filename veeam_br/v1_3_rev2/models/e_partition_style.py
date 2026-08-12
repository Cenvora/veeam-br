from enum import Enum


class EPartitionStyle(str, Enum):
    GPT = "Gpt"
    MBR = "Mbr"
    RAW = "Raw"

    def __str__(self) -> str:
        return str(self.value)
