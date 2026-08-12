from enum import Enum


class EDiskPartitionType(str, Enum):
    BACKEFI = "BackEFI"
    BACKEXTVOLUME = "BackExtVolume"
    BACKMRP = "BackMrp"
    BACKVOLUME = "BackVolume"
    EFI = "EFI"
    EXTENDED = "Extended"
    EXTUNALLOCATED = "ExtUnallocated"
    EXTVOLUME = "ExtVolume"
    MRP = "Mrp"
    OTHEROSPARTITION = "OtherOsPartition"
    UNALLOCATED = "Unallocated"
    VOLUME = "Volume"

    def __str__(self) -> str:
        return str(self.value)
