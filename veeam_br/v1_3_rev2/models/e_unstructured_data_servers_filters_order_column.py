from enum import Enum


class EUnstructuredDataServersFiltersOrderColumn(str, Enum):
    DESCRIPTION = "Description"
    NAME = "Name"
    REGION = "Region"
    TYPE = "Type"

    def __str__(self) -> str:
        return str(self.value)
