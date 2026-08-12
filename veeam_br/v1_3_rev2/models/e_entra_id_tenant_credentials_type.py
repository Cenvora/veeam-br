from enum import Enum


class EEntraIdTenantCredentialsType(str, Enum):
    CERTIFICATE = "Certificate"
    SECRET = "Secret"

    def __str__(self) -> str:
        return str(self.value)
