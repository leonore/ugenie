help:
	@echo "    run-actions"
	@echo "        Start the action server process in the background"
	@echo "    train"
	@echo "        Train the chatbot"
	@echo "    train-interactive"
	@echo "        Train the chatbot interactively"
	@echo "    run"
	@echo "        Start the chatbot in the normal way (without training)"
	@echo "    populate"
	@echo "        Populate the database (if you're not sure it's up to date)"
	@echo "    clean f=filename"
	@echo "        Zip all current chat logs into an archive called 'filename.zip' and remove text files"
	@echo "    testing"
	@echo "        Run available tests"

run-actions:
	cd chat-service/model; python3 -m rasa_core_sdk.endpoint --actions actions

# this removes any past models to avoid any clashes
train:
	cd chat-service/model/agent-data; rm -r models/;
	cd chat-service/model; python3 -c "import trainer; trainer.train()"

# & makes processes run in background
# sometimes Ctrl+C won't kill it properly
# to kill it, get its process id
# $ ps
# $ kill [psid]
train-interactive:
	make run-actions&
	cd chat-service/model; python3 -c "import trainer; trainer.train_interactive()"

run:
	make run-actions&
	cd chat-service; python3 main.py

populate:
	cd elastic-db; python3 populate_elastic.py;

testing:
	cd tests/unit_testing; python elastic_runner.py;
	cd tests; python tdd_units.py; python test_prototype.py; python testing_elastic.py;

clean:
	echo "zipping chat logs!"
	zip chat-service/model/chat-logs/$(f).zip chat-service/model/chat-logs/*.txt; rm chat-service/model/chat-logs/*.txt;
