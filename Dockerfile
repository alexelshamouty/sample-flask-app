FROM python:3.7.1-stretch as base
USER root

RUN useradd -m app
RUN mkdir -p /app && chown -R app:app /app

USER app
WORKDIR /app
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
COPY --chown=app:app poetry.lock pyproject.toml /app/
RUN ~/.poetry/bin/poetry install

FROM base as development
USER app
COPY --chown=app:app guestbook /app
EXPOSE 5000
CMD ~/.poetry/bin/poetry run python myapp.py