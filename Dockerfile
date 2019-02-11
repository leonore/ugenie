FROM python:3.6.6-slim

COPY ./requirements.txt /app/requirements.txt

# install requirements
RUN apt-get update && pip install -r requirements.txt
RUN python -m spacy download en

ADD . /app

WORKDIR ./chat-service

# need to figure out paths
# train model
#RUN python -c 'import trainer; trainer.train()'

# spin up action server
#RUN nohup python -m rasa_core_sdk.endpoint --actions actions &

# Launch the whole stack
CMD [ "python", "main.py" ]
