from fastapi import APIRouter


router = APIRouter()


@router.get('/questions/')
async def get_questions():
    return {"question_1": "What are you?"}
