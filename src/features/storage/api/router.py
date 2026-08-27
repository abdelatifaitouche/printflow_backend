from fastapi import APIRouter, Depends
from src.features.storage.application.document_uc import DocumentUC
from src.infra.storage.google_drive_client import GoogleDriveClient

router = APIRouter(prefix="/document")


def get_uc():
    google_drive_client = GoogleDriveClient()
    return DocumentUC(google_drive_client)


@router.post("")
async def upload(uc: DocumentUC = Depends(get_uc)):
    return await uc.upload_file()
