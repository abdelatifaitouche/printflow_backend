from src.core.shared.interfaces.storage_client import IStorageClient


class MinioClient(IStorageClient):
    _instance = None
    _is_instantiated = False

    def __new__(cls):
        pass

    def __init__(self):
        pass
