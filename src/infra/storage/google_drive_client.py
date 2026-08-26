from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from src.core.shared.interfaces.storage_client import IStorageClient
from typing import Any


class GoogleDriveClient(IStorageClient):
    _instance = None
    _is_instantiated = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._is_instantiated = False
        return cls._instance

    def __init__(self):
        if self._is_instantiated:
            return
        self.drive_service = self._auth()
        self.parent_folder: str = "1wRsXYJ3BzyiZJkL6YwlZ1X1i5zgDweGK"
        self._is_instantiated = True

    def _auth(self):
        BASE_DIR = Path(__file__).resolve().parents[3]
        SERVICE_ACCOUNT_FILE = BASE_DIR / "drive_api_secret.json"

        SCOPES = ["https://www.googleapis.com/auth/drive"]

        creds = service_account.Credentials.from_service_account_file(
            filename=SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )

        return build(
            "drive",
            "v3",
            credentials=creds,
        )

    def upload(self):
        pass

    def download(self):
        pass

    def generate_signed_url(self):
        pass

    def create_folder(
        self,
        folder_name: str,
        parent_folder_id: str | None = None,
    ):
        folder_metadata: dict[str, Any] = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder",
        }

        if parent_folder_id is None:
            folder_metadata["parents"] = [self.parent_folder]

        folder = (
            self.drive_service.files()
            .create(body=folder_metadata, fields="id, name", supportsAllDrives=True)
            .execute()
        )

        print(f"Created folder for '{folder.get('name')}'")

        return folder.get("id")

    def list_files(self, folder_id: str | None = None, page_size: int = 10):

        target_folder_id: str = folder_id or self.parent_folder

        query = f"'{target_folder_id}' in parents and trashed = false"

        results = (
            self.drive_service.files()
            .list(
                q=query,
                pageSize=page_size,
                fields="nextPageToken, files(id, name, mimeType, size, createdTime)",
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
            )
            .execute()
        )

        files = results.get("files", [])

        return files

    def delete_file(self):
        pass

    def delete_folder(self):
        pass
