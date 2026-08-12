from enum import Enum


class EADGroupScope(str, Enum):
    DOMAINLOCAL = "DomainLocal"
    GLOBAL = "Global"
    UNIVERSAL = "Universal"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
