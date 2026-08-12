from enum import Enum


class EHelperApplianceTemplatesFiltersOrderColumn(str, Enum):
    LOCATION = "Location"
    RESOURCEGROUP = "ResourceGroup"

    def __str__(self) -> str:
        return str(self.value)
