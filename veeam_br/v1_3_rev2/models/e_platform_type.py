from enum import Enum


class EPlatformType(str, Enum):
    APPLICATIONBACKUPREPOSITORY = "ApplicationBackupRepository"
    AWSEC2 = "AWSEC2"
    AZURECOMPUTE = "AzureCompute"
    CLOUDDIRECTOR = "CloudDirector"
    CUSTOMPLATFORM = "CustomPlatform"
    ENTRAID = "EntraID"
    GCE = "GCE"
    HYPERV = "HyperV"
    IRIS = "Iris"
    LINUXPHYSICAL = "LinuxPhysical"
    LINUXPHYSICALPPC = "LinuxPhysicalPpc"
    MONGODB = "MongoDb"
    NUTANIX = "Nutanix"
    PROXMOX = "Proxmox"
    TAPE = "Tape"
    TEST = "Test"
    UNSTRUCTUREDDATA = "UnstructuredData"
    VMWARE = "VMware"
    WINDOWSPHYSICAL = "WindowsPhysical"

    def __str__(self) -> str:
        return str(self.value)
