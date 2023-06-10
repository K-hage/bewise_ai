from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from src.questions.router import router as question_router

app = FastAPI(
    title='Test 1',
)

app.include_router(question_router)


@app.get("/", include_in_schema=False)
def read_root() -> RedirectResponse:
    return RedirectResponse(url='/docs')


@app.get("/{path:path}", include_in_schema=False)
async def get_any(path: str):
    raise HTTPException(status_code=404, detail='Страница не найдена')
