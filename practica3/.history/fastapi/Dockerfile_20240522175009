# syntax = docker/dockerfile:1.4

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY entrypoint.sh .
COPY ./app .

RUN pip install virtualenv \
    && virtualenv /app/venv \
    && . /app/venv/bin/activate \
    && pip install -r requirements.txt \
    && chmod +x entrypoint.sh


CMD ["/app/entrypoint.sh"]
