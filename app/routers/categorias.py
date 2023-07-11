from fastapi import APIRouter

router = APIRouter()

@router.get("/categorias")
async def get_categorias():
    return {"message": "categorias!"}
