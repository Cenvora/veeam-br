from enum import Enum


class EAgentInventoryObjectType(str, Enum):
    CONTAINER = "Container"
    CUSTOM = "Custom"
    DOMAIN = "Domain"
    GROUP = "Group"
    LINUXCOMPUTER = "LinuxComputer"
    ORGANIZATIONUNIT = "OrganizationUnit"
    PROTECTIONGROUP = "ProtectionGroup"
    WINDOWSCLUSTER = "WindowsCluster"
    WINDOWSCOMPUTER = "WindowsComputer"

    def __str__(self) -> str:
        return str(self.value)
