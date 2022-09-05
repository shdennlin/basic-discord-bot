FROM python:3.9.13-slim-buster

WORKDIR /app
COPY * ./
COPY .env ./
RUN apt-get update; apt-get install curl -y
RUN pip install poetry
RUN poetry install --no-dev

CMD ["poetry", "run", "python", "main.py"]