from enum import Enum


class EProxmoxInventoryType(str, Enum):
    CLUSTER = "Cluster"
    NODE = "Node"
    POOL = "Pool"
    VIRTUALMACHINE = "VirtualMachine"

    def __str__(self) -> str:
        return str(self.value)
