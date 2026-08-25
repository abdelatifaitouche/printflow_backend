from src.core.shared.interfaces.storage_client import IStorageClient


class GoogleDriveClient(IStorageClient):
    _instance = None
    _is_instantiated = False

    def __new__(cls):
        pass

    def __init__(self):
        pass

    def upload(self):
        pass

    def download(self):
        pass

    def generate_signed_url(self):
        pass

    def create_folder(self):
        pass

    def list_folders(self):
        pass

    def get_folder_files(self):
        pass

    def delete_file(self):
        pass

    def delete_folder(self):
        pass
