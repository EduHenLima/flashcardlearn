from fastapi import APIRouter

from app.services.assuntoService import CreateAssunto

router = APIRouter()


@router.get("/assuntos")
async def get_assuntos():
    return {"message": "assuntos!"}


@router.post("/assuntos")
async def create_assuntos(assunto: CreateAssunto):
    return assunto
