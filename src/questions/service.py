from typing import List

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.questions.models import Questions
from src.questions.schemas import Question
from src.questions.utils import get_questions


async def save_questions(session: AsyncSession, questions: List[Question]) -> None:
    """ Получает сессию к бд и список вопросов и сохраняет их в бд """

    async with session.begin():
        try:
            for question in questions:
                retry_count = 0
                # 10 попыток на замену существующего вопроса, если нет замены пропускаем(защита от зацикливания)
                while retry_count != 10:
                    retry_count += 1
                    existing_question = await session.get(Questions, question.id)
                    if existing_question:
                        question = get_questions(1)[0]
                    break
                else:
                    continue
                db_question = Questions(**question.dict())
                session.add(db_question)
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=400, detail='Ошибка при создании записи'
            )


async def process_questions(session: AsyncSession, questions_num: int) -> None:
    """ Получаем вопросы из get_questions """

    questions = get_questions(questions_num)
    await save_questions(session, questions)


async def get_last_question(session: AsyncSession) -> Questions | None:
    """ Возвращает последний сохраненный вопрос в бд """

    query = select(Questions).order_by(Questions.created.desc())
    question = await session.execute(query)
    q = question.scalars().first()
    await session.commit()
    return q
