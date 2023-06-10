import datetime

from pydantic import BaseModel, validator


class PostRequest(BaseModel):
    questions_num: int


class Question(BaseModel):
    id: int
    answer: str
    question: str
    created_at: datetime.datetime

    @validator('id', pre=True)
    def set_id(cls, val):
        return str(val)

    @classmethod
    def empty(cls):
        """ Возвращает пустой объект """
        return cls(
            id=0,
            question='',
            answer='',
            created_at=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        )

    @classmethod
    def from_orm(cls, question):
        return cls(
            id=question.id,
            question=question.question,
            answer=question.answer,
            created_at=question.created_at
        )
