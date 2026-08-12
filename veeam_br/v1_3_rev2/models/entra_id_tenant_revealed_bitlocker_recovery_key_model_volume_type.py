from enum import Enum


class EntraIdTenantRevealedBitlockerRecoveryKeyModelVolumeType(str, Enum):
    FIXEDDATAVOLUME = "FixedDataVolume"
    OPERATINGSYSTEMVOLUME = "OperatingSystemVolume"
    REMOVABLEDATAVOLUME = "RemovableDataVolume"
    UNKNOWNFUTUREVALUE = "UnknownFutureValue"

    def __str__(self) -> str:
        return str(self.value)
