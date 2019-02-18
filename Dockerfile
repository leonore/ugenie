# Extend the official Rasa Core SDK image
FROM rasa/rasa_core_sdk:0.12.1

RUN apt-get update && pip install elasticsearch

COPY ./chat-service/model/elastic.py /app/elastic.py
COPY ./chat-service/model/network_config.py /app/network_config.py

ENV DOCKER Yes
