from src.core.shared.enums.storage_client import StorageClient
from src.infra.storage.google_drive_client import GoogleDriveClient
from src.infra.storage.minio_client import MinioClient
from src.infra.storage.local_storage import LocalStorage


def get_storage_client(storage_client: StorageClient):
    match storage_client:
        case StorageClient.GOOGLE_DRIVE:
            return GoogleDriveClient()
        case StorageClient.MINIO:
            return MinioClient()
        case StorageClient.LOCAL:
            return LocalStorage()
        case _:
            raise ValueError("Storage Invalid")
