from enum import Enum


class EMoveCopySessionAction(str, Enum):
    FORGETFAILED = "ForgetFailed"
    RETRY = "Retry"
    STOPANDUNDO = "StopAndUndo"

    def __str__(self) -> str:
        return str(self.value)
