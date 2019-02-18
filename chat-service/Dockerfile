FROM python:3.6.6-slim

COPY ./requirements.txt /app/requirements.txt

# install requirements
RUN apt-get update && apt-get install build-essential -y

WORKDIR app

RUN pip install -r requirements.txt
RUN python -m spacy download en

COPY ./model/network_config.py /app/network_config.py

ADD . /app

ENV DOCKER Yes

# Launch the whole stack
CMD [ "python", "main.py" ]
