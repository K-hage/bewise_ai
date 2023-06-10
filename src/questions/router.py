from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.questions.schemas import PostRequest, Question
from src.questions.service import process_questions, get_last_question


router = APIRouter(
    prefix="/question",
    tags=["Question"]
)


@router.post("/")
async def questions_request(
        new_request: PostRequest,
        session: AsyncSession = Depends(get_async_session)
) -> Question:
    """
    Получает запрос на количество вопросов для сохранения в бд.
    Возвращает последний сохраненный вопрос, с предыдущего сохранения
    """

    questions_num = new_request.questions_num
    question = await get_last_question(session)
    await process_questions(session, questions_num)

    return Question.from_orm(question) if question else Question.empty()
