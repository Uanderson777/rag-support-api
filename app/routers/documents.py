from typing import List
from fastapi import APIRouter, HTTPException, status
from app.models.document import DocumentChunk
from app.services.document_service import DocumentService

router = APIRouter(prefix="/documents", tags=["Documents"])
document_service = DocumentService()


@router.post("/ingest/file/{filename}", response_model=List[DocumentChunk], status_code=status.HTTP_200_OK)
def ingest_document_file(filename: str):
    """
    Endpoint para realizar a ingestão e o fatiamento (chunking) de um arquivo de texto específico da pasta data/.
    """
    try:
        chunks = document_service.load_and_chunk_file(filename)
        return chunks
    except FileNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
