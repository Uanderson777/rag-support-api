from fastapi import FastAPI
from app.routers import health, documents

app = FastAPI(
    title="RAG Support API",
    description="API de Base de Conhecimento para Suporte Técnico utilizando RAG e FastAPI",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(documents.router)


@app.get("/")
def read_root():
    return {
        "message": "Bem-vindo à RAG Support API! Acesse /docs para visualizar a documentação interativa."
    }
