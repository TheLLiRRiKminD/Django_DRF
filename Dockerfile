FROM python:3 as builder

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config installer.max-workers 10

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .