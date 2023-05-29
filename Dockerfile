FROM python:3.8

ENV PYTHODONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .