## Using the chatbot via Docker container


### Installing Docker
Follow the [official tutorial for Docker CE](https://docs.docker.com/install/)     
Follow the [official tutorial for docker-compose](https://docs.docker.com/compose/install/)

### Starting the docker compose

Make sure docker is running in the background first.     

From the main directory of the project:
```bash
docker-compose up --build # if you change things to the project/first time you run it
docker-compose up
# docker-compose up -d if you don't wanna see the logs (run in background)
# then use docker-compose down to take down
# if you run this command quite a lot, sometimes
docker system prune # is useful!
```

### Starting the chatbot

The chatbot should be running at localhost:5000.     

**TLDR**; spinning up docker-compose up will have everything running for you in one command.
