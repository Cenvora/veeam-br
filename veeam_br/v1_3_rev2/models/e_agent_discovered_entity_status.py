from enum import Enum


class EAgentDiscoveredEntityStatus(str, Enum):
    OFFLINE = "Offline"
    ONLINE = "Online"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
