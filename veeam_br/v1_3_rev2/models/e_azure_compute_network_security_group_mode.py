from enum import Enum


class EAzureComputeNetworkSecurityGroupMode(str, Enum):
    CREATENEW = "CreateNew"
    DONOTASSIGN = "DoNotAssign"
    EXISTING = "Existing"

    def __str__(self) -> str:
        return str(self.value)
