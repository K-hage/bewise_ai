FROM python:3.10-slim

WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD alembic upgrade head
CMD uvicorn src.main:app --host 0.0.0.0 --port 8000
