from enum import StrEnum


class ProcessingStatus(StrEnum):
    UPLOADING = "UPLOADING"
    UPLOADED = "UPLOADED"
    FAILED = "FAILED"
