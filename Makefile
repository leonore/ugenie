help:
	@echo "    run-actions"
	@echo "        Start the action server process in the background"
	@echo "    train"
	@echo "        Train the chatbot"
	@echo "    train-interactive"
	@echo "        Train the chatbot interactively"
	@echo "    run"
	@echo "        Start the chatbot in the normal way (without training)"
	@echo "    clean f=filename"
	@echo "        Zip all current chat logs into an archive called 'filename' and remove text files"

run-actions:
	cd chat-service/model; python3 -m rasa_core_sdk.endpoint --actions actions

train:
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

clean:
	echo "zipping logs"
	zip chat-service/model/chat-logs/$(f).zip chat-service/model/chat-logs/*.txt; rm chat-service/model/chat-logs/*.txt;
