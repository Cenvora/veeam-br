from enum import Enum


class EHaPatroniNodeRole(str, Enum):
    LEADER = "Leader"
    REPLICA = "Replica"
    STANDBYLEADER = "StandbyLeader"
    SYNCSTANDBY = "SyncStandby"

    def __str__(self) -> str:
        return str(self.value)
