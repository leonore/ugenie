## Running the Chat

### Start MySQL:

Provided you've already followed the instructions in Database.md:

```bash
sudo service mysql start
```
---

### (Optional) Train the Rasa-Agent:

If changes have been made to the Rasa Agent's training data (anything in the '\dissertation\chat-interface\data' folder), the bot should be trained again with the new data.

To do this, open two terminals, in the first run:
```bash
python3 -m rasa_core_sdk.endpoint --actions actions
```

This will start the running action endpoint process, leave that running and in the second terminal enter:
```bash
cd /chat-interface
python3 -c 'import trainer; trainer.train()'
```
---

### Running the Chat Service:

If the agent has been trained and is ready to use, open two terminals, in the first run:
```bash
python3 -m rasa_core_sdk.endpoint --actions actions
```

This will start the running action endpoint process, leave that running and in the second terminal enter:
```bash
cd /chat-interface
python3 main.py
```

Then, wait until Flask prints the message:

```bash
* Debugger is active! 
```

Open your browser and visit http://127.0.0.1:5000/, be sure to check the server console for messages from the running chat server and the endpoint console for messages from the action endpoint.

---