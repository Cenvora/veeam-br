from enum import Enum


class ERestoreOptionsFiltersOrderColumn(str, Enum):
    CODE = "Code"
    DESCRIPTION = "Description"
    GROUP = "Group"
    NAME = "Name"

    def __str__(self) -> str:
        return str(self.value)
