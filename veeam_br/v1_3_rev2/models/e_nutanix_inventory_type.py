from enum import Enum


class ENutanixInventoryType(str, Enum):
    CATEGORY = "Category"
    CLUSTER = "Cluster"
    PRISMCENTRAL = "PrismCentral"
    VIRTUALMACHINE = "VirtualMachine"

    def __str__(self) -> str:
        return str(self.value)
