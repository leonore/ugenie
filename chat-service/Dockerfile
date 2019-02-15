FROM python:3.6.6-slim

COPY ./requirements.txt /app/requirements.txt

# install requirements
RUN apt-get update
RUN apt-get install build-essential -y

WORKDIR app

RUN pip install -r requirements.txt
RUN python -m spacy download en

ADD . /app

#WORKDIR model

#RUN python -c 'import trainer; trainer.train()'

#WORKDIR ..

# Launch the whole stack
CMD [ "python", "main.py" ]
