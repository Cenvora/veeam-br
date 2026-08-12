from enum import Enum


class EUnstructuredDataInventoryBrowseItemType(str, Enum):
    DRIVE = "Drive"
    FILE = "File"
    FOLDER = "Folder"

    def __str__(self) -> str:
        return str(self.value)
