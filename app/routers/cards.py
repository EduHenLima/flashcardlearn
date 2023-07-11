from fastapi import APIRouter

router = APIRouter()

@router.get("/cards")
async def get_cards():
    return {"message": "cards!"}
