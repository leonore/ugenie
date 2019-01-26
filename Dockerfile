FROM python:3.6.6-slim

COPY . /app
WORKDIR /app

RUN apt-get update
RUN apt-get install build-essential -y
RUN pip install -r requirements.txt
RUN python -m spacy download en

WORKDIR chat-interface
CMD [ "python", "main.py" ]
