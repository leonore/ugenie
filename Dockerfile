FROM rasa/rasa_core:0.12.4

COPY . /app
WORKDIR /app

# install requirements
RUN apt-get update && \
    pip install -r requirements.txt

WORKDIR chat-service

# need to figure out paths
# train model
#RUN python -c 'import trainer; trainer.train()'
# spin up action server
#RUN nohup python -m rasa_core_sdk.endpoint --actions actions &

# Launch the whole stack
CMD [ "python", "main.py" ]
