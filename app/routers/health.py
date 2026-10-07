from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/healthcheck")
def healthcheck():
    """
    Endpoint de monitoramento para verificar se a API está online e saudável.
    """
    return {
        "status": "ok",
        "service": "RAG Support API",
        "version": "1.0.0"
    }
