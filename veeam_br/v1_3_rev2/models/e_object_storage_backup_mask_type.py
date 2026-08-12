from enum import Enum


class EObjectStorageBackupMaskType(str, Enum):
    FULLPATH = "FullPath"
    LEGACY = "Legacy"
    RELATIVEPATH = "RelativePath"

    def __str__(self) -> str:
        return str(self.value)
