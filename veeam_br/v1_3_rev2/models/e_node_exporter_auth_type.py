from enum import Enum


class ENodeExporterAuthType(str, Enum):
    NONE = "None"
    USERNAMEPASSWORD = "UsernamePassword"

    def __str__(self) -> str:
        return str(self.value)
