FROM python:3.11

RUN mkdir /application
EXPOSE 8000

COPY . /application/
COPY pyproject.toml /application/
WORKDIR /application

RUN pip3 install poetry && poetry install --no-interaction
WORKDIR /application/src
CMD ["poetry", "run", "uvicorn", "app:app", "--host","0.0.0.0", "--port","8000"]