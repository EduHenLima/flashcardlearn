from fastapi import APIRouter

router = APIRouter()

@router.get("/resposta")
async def get_resposta():
    return {"message": "resposta!"}
