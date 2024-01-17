FROM python:3.10-alpine

WORKDIR /code

COPY ./code/requirements.txt .

RUN pip install -r requirements.txt

COPY ./code .
