help:
	@echo "    run-actions"
	@echo "        Start the action server process in the background"
	@echo "    train"
	@echo "        Train the chatbot"
	@echo "    train-interactive"
	@echo "        Train the chatbot interactively"
	@echo "    run"
	@echo "        Start the chatbot in the normal way (without training)"

run-actions:
	cd chat-service/model; python3 -m rasa_core_sdk.endpoint --actions actions

train:
	cd chat-service/model; python3 -c "import trainer; trainer.train()"

train-interactive:
	make run-actions&
	cd chat-service/model; python3 -c "import trainer; trainer.train_interactive()"
# & makes it run in background
# to kill it, get its process id
# $ ps
# $ kill [psid]

run:
	make run-actions&
	cd chat-service; python3 main.py

#visualize:
#	python3 -m rasa_core.visualize -s data/core/ -d domain.yml -o story_graph.png
