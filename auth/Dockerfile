FROM python:3.8

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml entrypoint.sh ./
RUN poetry install --only=main

COPY ./auth ./auth

CMD ["/bin/bash", "entrypoint.sh"]
#CMD ["flask", "run", "--app", "auth.py", "--host=0.0.0.0"]
# docker run -p 4001:5000 auth
