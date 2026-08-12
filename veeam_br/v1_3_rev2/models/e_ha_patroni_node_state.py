from enum import Enum


class EHaPatroniNodeState(str, Enum):
    CRASHED = "Crashed"
    CREATINGREPLICA = "CreatingReplica"
    INARCHIVERECOVERY = "InArchiveRecovery"
    INITDBFAILED = "InitdbFailed"
    INITIALIZINGNEWCLUSTER = "InitializingNewCluster"
    RESTARTFAILED = "RestartFailed"
    RESTARTING = "Restarting"
    RUNNING = "Running"
    STARTFAILED = "StartFailed"
    STARTING = "Starting"
    STOPFAILED = "StopFailed"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    STREAMING = "Streaming"

    def __str__(self) -> str:
        return str(self.value)
