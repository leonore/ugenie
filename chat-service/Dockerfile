FROM python:3.6.6-slim

COPY ./requirements.txt /app/requirements.txt

# install requirements
RUN apt-get update && apt-get install build-essential -y

WORKDIR app

RUN pip install -r requirements.txt
RUN python -m spacy download en

COPY ./model/network_config.py /app/network_config.py

# check if training files have been modified
COPY ./model/domain.yml /app/domain.yml
COPY ./model/trainer.py /app/trainer.py
COPY ./model/nlu-config.yml /app/nlu-config.yml
COPY ./model/agent-data/data/stories.md /app/agent-data/data/stories.md
COPY ./model/agent-data/data/nlu.md /app/agent-data/data/nlu.md

# if modified: TRAINING needs to be done
RUN python -c "import trainer; trainer.train()"

ADD . /app

ENV DOCKER Yes

# Launch the whole stack
CMD [ "python", "main.py" ]
