FROM python:3.9.13-slim-buster

WORKDIR /app
COPY * ./
COPY .env ./
RUN apt-get update; apt-get install curl -y
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN /root/.local/bin/poetry install --no-dev

CMD ["/root/.local/bin/poetry", "run", "python", "main.py"]