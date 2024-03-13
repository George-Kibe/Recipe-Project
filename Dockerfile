FROM  python:3.11-alpine3.18
LABEL maintainer="georgekibe.vercel.app"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./project /project
WORKDIR /project
EXPOSE 8000

ARG DEV=false
RUN python3 -m venv /venv && /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    if [$DEV = "true"]; \
        then /venv/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/venv/bin:$PATH"

USER django-user