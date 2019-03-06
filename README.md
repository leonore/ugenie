# CS01 - Virtual Assistant for UofG's External Relations

[![build status](http://stgit.dcs.gla.ac.uk/tp3-2018-cs01/dissertation/badges/master/pipeline.svg)](http://stgit.dcs.gla.ac.uk/tp3-2018-cs01/dissertation/commits/master)             

This software engineering project is to create a **virtual assistant / chatbot** that will help answer the increasing volume of application and course enquiries at the University of Glasgow's External Relations Directorate.     

Our application consists of:
* an interface for users to interact with the chatbot (`Flask + socketio`)
* connected to a Natural Language Understanding unit (`RASA`)
* which makes queries to a free-text search engine (`Elasticsearch`)

An online prototype of the bot is available [here :robot:](bit.do/uofg-bot)
______________

Cloning this repository from 15th of March 2019 should include a trained version of the bot.
- [Set up dependencies manually](Manuel dependency setup) 
    - [Launching from manual set-up](Launching after setup)
- [Launching from Docker](Launching from Docker)
- [Sample questions to ask the bot](Interacting with the bot)
- [Extra documentation on different app components](http://stgit.dcs.gla.ac.uk/tp3-2018-cs01/dissertation/tree/master/docs)

--------

#### Manuel dependency setup
How to get yourself set up with dependencies manually, for development:

```bash
pip install rasa_core
pip install rasa_nlu[spacy]
python -m spacy download en
pip install flask-socketio
pip install elasticsearch
pip install xlrd
````
*N.B. Python should be `3.6+`*

##### Launching after setup
```bash
make train
make run
```

The bot should then be running at [localhost:5000](localhost:5000)

#### Launching from Docker
This is easier for direct interaction with the bot.
*NB: Need to figure out how to train the bot from Docker containers because it doesn't work from VM so our build would fail*

```bash
docker-compose up --build
```
The bot should then be running at [localhost:5000](localhost:5000)

_____
#### Interacting with the bot

Here are some questions you can ask GUVA:
- What is [course]?
- How much is [course/short course]?
- When is [short course]?
- Who teaches [short course]?
- What other courses does [tutor] teach?
- What does [acronym] mean?
- What does [acronym] of a course mean?
