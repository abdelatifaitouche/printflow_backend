from dataclasses import dataclass
from uuid import UUID, uuid4
from src.features.storage.domain.document_status import DocumentStatus
from src.features.storage.domain.processing_status import ProcessingStatus


@dataclass
class Document:
    id: UUID
    document_name: str
    document_id: str
    parent_folder_id: str
    mime_type: str
    size: int
    status: DocumentStatus
    processing_status: ProcessingStatus

    @classmethod
    def create(
        cls,
        *,
        document_name: str,
        document_id: str,
        parent_folder_id: str,
        mime_type: str,
        size: int,
    ) -> "Document":

        doc = cls(
            id=uuid4(),
            document_name=document_name,
            document_id=document_id,
            parent_folder_id=parent_folder_id,
            mime_type=mime_type,
            size=size,
            status=DocumentStatus.NON_ACTIVE,
            processing_status=ProcessingStatus.UPLOADING,
        )

        return doc
