FROM python:3.6.6-slim

COPY . /app
WORKDIR /app

# install requirements
RUN apt-get update
RUN apt-get install build-essential -y
RUN pip install -r requirements.txt
RUN python -m spacy download en

WORKDIR chat-service/model

# set up RASA unit
RUN python -c 'import trainer; trainer.train()'

# Launch the whole stack
CMD [ "python", "main.py" ]
