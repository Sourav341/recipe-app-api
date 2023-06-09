FROM python:3.11-alpine3.15
LABEL MAINTAINER "Sourav" 

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app/

RUN adduser -D user
USER user


#d:\Doc_Djn\recipe-app-api\.venv\Scripts\python.exe 