import os
from typing import List
from app.models.document import DocumentChunk


class DocumentService:
    """
    Serviço responsável pela leitura e fatiamento (chunking) de documentos da base de conhecimento.
    """

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir

    def load_and_chunk_file(self, filename: str) -> List[DocumentChunk]:
        """
        Lê um arquivo específico na pasta data/ e o divide em chunks com base em parágrafos.
        """
        file_path = os.path.join(self.data_dir, filename)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo '{filename}' não encontrado em '{self.data_dir}'.")

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        # Estratégia simples: dividir por parágrafos/blocos de texto de delimitador '\n\n'
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        chunks: List[DocumentChunk] = []
        for index, paragraph in enumerate(paragraphs, start=1):
            chunk = DocumentChunk(
                content=paragraph,
                source=filename,
                chunk_id=index
            )
            chunks.append(chunk)

        return chunks

    def load_and_chunk_all() -> List[DocumentChunk]:
        """
        Varre todos os arquivos .txt da pasta data/ e retorna todos os chunks combinados.
        """
        all_chunks: List[DocumentChunk] = []
        if not os.path.exists(self.data_dir):
            return all_chunks

        files = [f for f in os.listdir(self.data_dir) if f.endswith(".txt")]
        current_id = 1

        for file_name in files:
            file_chunks = self.load_and_chunk_file(file_name)
            for chunk in file_chunks:
                chunk.chunk_id = current_id
                all_chunks.append(chunk)
                current_id += 1

        return all_chunks
