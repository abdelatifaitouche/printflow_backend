from abc import ABC


class IStorageClient(ABC):
    def upload(self, *args, **kwargs):
        pass

    def download(self, *args, **kwargs):
        pass

    def generate_signed_url(self, *args, **kwargs):
        raise NotImplementedError()
