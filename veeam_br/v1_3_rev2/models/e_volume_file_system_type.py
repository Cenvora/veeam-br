from enum import Enum


class EVolumeFileSystemType(str, Enum):
    CDFS = "CDFS"
    EXFAT = "exFAT"
    FAT = "FAT"
    FAT32 = "FAT32"
    HPFS = "HPFS"
    NTFS = "NTFS"
    NWFS = "NWFS"
    REFS = "ReFS"
    UDF = "UDF"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
