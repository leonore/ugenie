help:
	@echo "    run-actions"
	@echo "        Start the action server process in the background"
	@echo "    train"
	@echo "        Train the chatbot"
	@echo "    train-interactive"
	@echo "        Train the chatbot interactively"
	@echo "    run"
	@echo "        Start the chatbot in the normal way (without training)"
	@echo "    clean"
	@echo "        Zip all current chat logs into and archive and remove text files"

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

# possible to-do: clean up log files
# clean:
# 	echo "zipping logs"
# 	filename := $(shell date +%Y-%m-%d-m%M)
# 	cd chat-service/model/chat-logs
# 	zip $(filename).zip *.txt
# 	rm *.txt

#visualize:
#	python3 -m rasa_core.visualize -s data/core/ -d domain.yml -o story_graph.png
