FROM python:3.11.3-alpine

WORKDIR /app

COPY . /app

ADD requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt