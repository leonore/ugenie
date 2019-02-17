## Using the chatbot via Docker container


### Installing Docker
Follow the [official tutorial for Docker CE](https://docs.docker.com/install/)     
Follow the [official tutorial for docker-compose](https://docs.docker.com/compose/install/)

### Unconvenient setup

For the chat to work from a Docker base, you need to uncomment / comment some lines in:
```
trainer.py
elastic.py
agent.py
endpoints.yml
```

for inner-Docker interaction to work correctly.

### Starting the docker compose

Make sure docker is running in the background first.     

From the main directory of the project:
```bash
docker-compose up
# docker-compose up -d if you don't wanna see the logs (run in background)
# then use docker-compose down to take down
```

### Populating the docker elastic container for the first time

Make sure you've stopped your own background elastic processes in the background    
change "9200" to "9200:9200" in docker-compose.

```bash
cd elastic-db
python populate_elastic.py
curl localhost:9200/short_courses/_search?pretty # check it worked!
```

### Starting the chatbot

The chatbot should be running at localhost:5000.     

**TLDR**; spinning up docker-compose up will have everything running for you in one command.