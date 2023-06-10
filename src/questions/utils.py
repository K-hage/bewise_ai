import requests

from src.questions.schemas import Question


def get_questions(questions_num: int) -> list[Question]:
    """
    Делает API запрос вопросов
    questions_num: количество запрашиваемых запросов
    возвращает список объектов Question
    """

    resp = requests.get(f"https://jservice.io/api/random?count={questions_num}")
    data = resp.json()
    questions = [Question.parse_obj(ques) for ques in data]
    return questions
