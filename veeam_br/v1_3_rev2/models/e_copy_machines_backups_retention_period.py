from enum import Enum


class ECopyMachinesBackupsRetentionPeriod(str, Enum):
    IN1MONTH = "In1Month"
    IN1WEEK = "In1Week"
    IN1YEAR = "In1Year"
    IN2WEEKS = "In2Weeks"
    IN2YEARS = "In2Years"
    IN3MONTHS = "In3Months"
    IN3YEARS = "In3Years"
    IN5YEARS = "In5Years"
    IN6MONTHS = "In6Months"
    IN7YEARS = "In7Years"

    def __str__(self) -> str:
        return str(self.value)
