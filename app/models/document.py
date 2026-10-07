from pydantic import BaseModel


class DocumentChunk(BaseModel):
    """
    Modelo Pydantic que representa um fragmento (chunk) de documento processado para o RAG.
    """
    content: str
    source: str
    chunk_id: int
