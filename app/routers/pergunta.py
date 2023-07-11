from fastapi import APIRouter

router = APIRouter()

@router.get("/pergunta")
async def get_perguntas():
    return {"message": "pergunta!"}
