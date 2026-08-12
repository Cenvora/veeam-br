from enum import Enum


class EProxyType(str, Enum):
    GENERALPURPOSEPROXY = "GeneralPurposeProxy"
    HVPROXY = "HvProxy"
    NUTANIXAHV = "NutanixAHV"
    PVE = "PVE"
    VIPROXY = "ViProxy"

    def __str__(self) -> str:
        return str(self.value)
