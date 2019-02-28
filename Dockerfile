# Extend the official Rasa Core SDK image
FROM rasa/rasa_core_sdk:0.12.1

# dependencies to interact with the database
RUN apt-get update && pip install elasticsearch && pip install xlrd

COPY ./chat-service/model /app/actions

COPY ./chat-service/model/elastic.py /app/elastic.py
COPY ./chat-service/model/network_config.py /app/network_config.py
COPY ./elastic-db/ /app/

ENV DOCKER Yes

# make the action server script executable
RUN chmod u+x start-action-server.sh

# run the database script and launch the action server
CMD ["run", "./start-action-server.sh"]
