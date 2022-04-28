# syntax=docker/dockerfile:1

FROM python:3.9.12-slim-buster

WORKDIR /app

ENV PYTHONBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install netcat -y

RUN apt-get install python3-dev -u gcc musl-dev -y

RUN apt-get install curl -y

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false \
    && poetry config virtualenvs.in-project false

COPY ./pyproject.toml ./poetry.lock* /app/

# Installing dependencies
ARG DEV
ENV DEV ${DEV:-true}
RUN /bin/sh -c "if [ $DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"


COPY ./entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

COPY . /app

CMD ["/app/entrypoint.sh"]