FROM python:3.10
ADD . /oddw

ARG host

ENV POETRY_VERSION=1.4.0
ENV DB_HOST="db"
ENV APP_HOST $host

RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /oddw
COPY poetry.lock pyproject.toml /oddw/

RUN poetry config virtualenvs.create false \
    && poetry install

CMD ["/bin/bash", "-c", "alembic upgrade head;poetry run python oddw/main.py;tail -F anything"]