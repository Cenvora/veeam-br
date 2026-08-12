from enum import Enum


class EHaCertificateFileFormatType(str, Enum):
    PEM = "Pem"

    def __str__(self) -> str:
        return str(self.value)
