from src.infra.storage.google_drive_client import GoogleDriveClient


class DocumentUC:
    def __init__(self, storage_client: GoogleDriveClient):
        self.storage_client = storage_client

    async def upload_file(self):
        # we need to save the document meta data to our db
        # generate a signed url to upload
        # return the signed url
        # track the state or event of the upload somehow and update the document db metadata

        signed_url = self.storage_client.generate_signed_url(
            "test.pdf", "application/pdf"
        )

        return signed_url
