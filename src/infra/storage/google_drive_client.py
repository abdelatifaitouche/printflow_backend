from pathlib import Path
import requests
from google.auth.transport.requests import Request
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

    def _get_creds(self):
        BASE_DIR = Path(__file__).resolve().parents[3]
        SERVICE_ACCOUNT_FILE = BASE_DIR / "drive_api_secret.json"

        SCOPES = ["https://www.googleapis.com/auth/drive"]

        creds = service_account.Credentials.from_service_account_file(
            filename=SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )

        return creds

    def _auth(self):
        creds = self._get_creds()
        return build(
            "drive",
            "v3",
            credentials=creds,
        )

    def upload(self):
        pass

    def download(self):
        pass

    def generate_signed_url(
        self,
        file_name: str,
        mime_type: str,
        parent_folder_id: str | None = None,
    ):
        try:
            creds = self._get_creds()
            creds.refresh(Request())
            access_token = creds.token

            url = (
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=resumable"
            )

            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json; charset=UTF-8",
                "X-Upload-Content-Type": mime_type,
            }

            metadata: dict[str, Any] = {
                "name": file_name,
            }

            if parent_folder_id is None:
                metadata["parents"] = [self.parent_folder]

            response = requests.post(
                url,
                headers=headers,
                json=metadata,
            )

            response.raise_for_status()

            upload_session_url = response.headers.get("Location")

            return upload_session_url
        except Exception as e:
            raise e

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
