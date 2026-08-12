from enum import Enum


class EHelperApplianceTemplateStatus(str, Enum):
    DELETING = "Deleting"
    DEPLOYING = "Deploying"
    OK = "OK"
    OUTDATED = "Outdated"

    def __str__(self) -> str:
        return str(self.value)
