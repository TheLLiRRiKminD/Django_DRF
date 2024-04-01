FROM python:3 as builder

ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config installer.max-workers 10

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .