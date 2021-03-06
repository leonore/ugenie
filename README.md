# CS01 - Virtual Assistant for UofG's External Relations &nbsp;<img src="chat-service/static/icon.png" width="30" height="30" alt="UGenie's face">

This software engineering project is to create a **virtual assistant / chatbot** that will help answer the increasing volume of application and course enquiries at the University of Glasgow's External Relations Directorate.     

Our application consists of:
* an interface for users to interact with the chatbot (`Flask + socketio`)
* connected to a Natural Language Understanding unit (`RASA`)
* which makes queries to a free-text search engine (`Elasticsearch`)

______________

- [Launching with Docker](#launching-with-docker)
- [Sample questions to ask the bot](#interacting-with-the-bot)
- [Contribution guide (includes codebase structure information)](CONTRIBUTING.md)
- [Set up dependencies manually](#manual-dependency-setup)
    - [Launching from manual set-up](#launching-after-setup)
--------

#### Set up

- Download a release of UGenie, which should include a data archive and a model archive
    - `models.zip` contains a trained instance of the bot
       - it should be decompressed in `chat-service/agent-data/` to create the path `chat-service/agent-data/models`
    - `data.zip` contains the client-provided university data
       - it should be decompressed in `elastic-db/` to create the path `elastic-db/data`


---------
#### Launching with Docker
This is easier for direct interaction with the bot and dependency setup.

```bash
docker-compose up --build
```
This should populate the database when launching. The bot should then be running at [localhost:5000](localhost:5000)

------

#### Manuel dependency setup
How to get yourself set up with dependencies manually, for development:

```bash
pip install rasa_core
pip install rasa_nlu[spacy]
python -m spacy download en
pip install -r requirements.txt # socket.io + elasticsearch wrapper + xlrd
````  
*N.B. Python should be `3.6+`. RASA installation is done in steps because it is a heavy package, and linking the spaCy english model only works this way.*

Elasticsearch also needs to be installed and ran as a background process:
- **with Docker**
```bash
docker-compose up elastic
```

- **Installing manually**

Installation varies quite a bit depending on OS, please look through [the official Elastic reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) for instructions!

##### Launching after setup
```bash
make populate # populate elastic with the data from data.zip
make train # not necessary if the models.zip was downloaded and nothing has been changed
make run
```

The bot should then be running at [localhost:5000](localhost:5000)     
*N.B.: if chat logs become excessive, run `make clean f=[filename]` to zip them up!*
_____

#### Interacting with the bot

Here are some questions you can ask UGenie:
- How can you help me?
- Can you redirect me to a human?
- What does [acronym] mean?
- What is [course] about?
- What are the English requirements for [course]?
- Does [course] run part-time/full-time?
- What [category] courses are there?
- What [category] courses are there in [month]?
- What [category] courses are there on [weekday]?
- How much is [course/short course]?
- What building is [short course] in?
- What time is [short course] at?
- Who teaches [short course]?
- What other courses does [tutor] teach?
- Are there credits attached to [course]?
- Do you have a link for [short course]?
- Is there funding available for short courses?
- Can I cancel my course?
- Can I get a refund?
- Can I transfer courses?
