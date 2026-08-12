from enum import Enum


class EInventoryScopeWorkloadType(str, Enum):
    BACKUPS = "Backups"
    COMPUTERS = "Computers"
    ENTRAIDTENANT = "EntraIdTenant"
    HYPERV = "HyperV"
    JOBS = "Jobs"
    NUTANIX = "Nutanix"
    OBJECTSTORAGE = "ObjectStorage"
    PROXMOX = "Proxmox"
    UNSTRUCTUREDDATA = "UnstructuredData"
    VSPHERE = "VSphere"

    def __str__(self) -> str:
        return str(self.value)
