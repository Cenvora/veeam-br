from enum import Enum


class EColdStorageRetrievalMode(str, Enum):
    AMAZONBULK = "AmazonBulk"
    AMAZONEXPEDITED = "AmazonExpedited"
    AMAZONSTANDARD = "AmazonStandard"
    AZUREHIGHPRIORITY = "AzureHighPriority"
    AZURESTANDARDPRIORITY = "AzureStandardPriority"

    def __str__(self) -> str:
        return str(self.value)
