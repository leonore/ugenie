# Extend the official Rasa Core SDK image
FROM rasa/rasa_core_sdk:latest

RUN apt-get update

RUN pip install elasticsearch

COPY ./chat-service/model/elastic.py /app/elastic.py
