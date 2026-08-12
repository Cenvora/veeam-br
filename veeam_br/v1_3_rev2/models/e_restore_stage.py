from enum import Enum


class ERestoreStage(str, Enum):
    CANCELLATION = "Cancellation"
    INITIALIZING = "Initializing"
    RESTOREMESSAGE = "RestoreMessage"
    RESTOREPROGRESS = "RestoreProgress"
    RETRY = "Retry"
    STANDBYSERVICERESTARTED = "StandByServiceRestarted"
    STARTED = "Started"
    WAITINGFORRESOURCESONTARGETSERVER = "WaitingForResourcesOnTargetServer"

    def __str__(self) -> str:
        return str(self.value)
