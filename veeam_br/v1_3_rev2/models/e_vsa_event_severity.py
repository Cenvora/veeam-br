from enum import Enum


class EVsaEventSeverity(str, Enum):
    ALERT = "Alert"
    CRITICAL = "Critical"
    DEBUG = "Debug"
    EMERGENCY = "Emergency"
    ERROR = "Error"
    INFORMATIONAL = "Informational"
    NOTICE = "Notice"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
