from enum import Enum


class EColdStorageOperationType(str, Enum):
    BACKUPTRANSFER = "BackupTransfer"
    FLRBLOBS = "FlrBlobs"
    GFSMETADATADOWNLOAD = "GfsMetadataDownload"
    HEALTHCHECK = "HealthCheck"
    METADOWNLOAD = "MetaDownload"
    RESTOREPOINTBLOBS = "RestorePointBlobs"

    def __str__(self) -> str:
        return str(self.value)
