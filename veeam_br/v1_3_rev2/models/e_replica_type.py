from enum import Enum


class EReplicaType(str, Enum):
    CDP = "CDP"
    SNAPSHOT = "Snapshot"

    def __str__(self) -> str:
        return str(self.value)
