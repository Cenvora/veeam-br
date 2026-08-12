from enum import Enum


class EColdStorageRetrievalSessionState(str, Enum):
    CLEANEDUP = "CleanedUp"
    FAILED = "Failed"
    INITIALIZED = "Initialized"
    ITEMSEARCHCOMPLETE = "ItemSearchComplete"
    RETRIEVED = "Retrieved"

    def __str__(self) -> str:
        return str(self.value)
