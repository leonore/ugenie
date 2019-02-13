# Extend the official Rasa Core SDK image
FROM rasa/rasa_core_sdk:0.12.1

RUN apt-get update

RUN pip install elasticsearch

COPY ./chat-service/model/elastic.py /app/elastic.py
