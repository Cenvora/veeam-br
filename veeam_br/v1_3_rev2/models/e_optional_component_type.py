from enum import Enum


class EOptionalComponentType(str, Enum):
    APPLICATIONBACKUPREPOSITORY = "ApplicationBackupRepository"
    CATALYSTSDK = "CatalystSdk"
    CIFSGATEWAY = "CifsGateway"
    DDBOOSTSDK = "DDBoostSdk"
    GUESTINTERACTIONPROXY = "GuestInteractionProxy"
    IRISPLUGIN = "IrisPlugin"
    MOUNTTARGET = "MountTarget"
    NFSGATEWAY = "NfsGateway"
    SNAPDIFFV3 = "SnapDiffV3"

    def __str__(self) -> str:
        return str(self.value)
