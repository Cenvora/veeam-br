from enum import Enum


class EDriverStatus(str, Enum):
    FAILED = "Failed"
    INSTALLED = "Installed"
    INSTALLEDREBOOTREQUIRED = "InstalledRebootRequired"
    NOTINSTALLED = "NotInstalled"
    NOTINSTALLEDREBOOTREQUIRED = "NotInstalledRebootRequired"
    STOPPED = "Stopped"
    UNKNOWN = "Unknown"
    UPGRADEAVAILABLE = "UpgradeAvailable"

    def __str__(self) -> str:
        return str(self.value)
