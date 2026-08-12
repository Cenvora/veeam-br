from enum import Enum


class ETaskType(str, Enum):
    COMMON = "Common"
    DEPLOYMENTKIT = "DeploymentKit"
    FLRDOWNLOAD = "FlrDownload"
    FLRRESTORE = "FlrRestore"
    FLRSEARCH = "FlrSearch"
    HIERARCHYRESCAN = "HierarchyRescan"
    RECOVERYMEDIA = "RecoveryMedia"

    def __str__(self) -> str:
        return str(self.value)
