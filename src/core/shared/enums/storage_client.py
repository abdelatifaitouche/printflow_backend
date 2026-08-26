from enum import StrEnum


class StorageClient(StrEnum):
    GOOGLE_DRIVE = "GOOGLE_DRIVE"
    MINIO = "MINIO"
    DROPBOX = "DROPBOX"
    LOCAL = "LOCAL"
