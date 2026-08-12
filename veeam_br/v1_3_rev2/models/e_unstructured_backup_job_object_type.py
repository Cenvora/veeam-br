from enum import Enum


class EUnstructuredBackupJobObjectType(str, Enum):
    CONTAINER = "Container"
    DIRECTORY = "Directory"
    FILE = "File"
    FILESERVERROOT = "FileServerRoot"
    FILESERVERSHARE = "FileServerShare"
    OBJECT = "Object"
    OBJECTSTORAGEROOT = "ObjectStorageRoot"
    PREFIX = "Prefix"
    SANCONTAINER = "SanContainer"
    SANFILER = "SanFiler"
    SANVOLUME = "SanVolume"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
