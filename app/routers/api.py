from fastapi import APIRouter

from app.routers import assuntos, cards, categorias, pergunta, resposta

router = APIRouter()
router.include_router(assuntos.router, prefix="/assuntos", tags=["Assuntos"])
router.include_router(cards.router, prefix="/cards", tags=["Cards"])
router.include_router(categorias.router, prefix="/categorias", tags=["Categorias"])
router.include_router(pergunta.router, prefix="/pergunta", tags=["Pergunta"])
router.include_router(resposta.router, prefix="/resposta", tags=["Resposta"])
