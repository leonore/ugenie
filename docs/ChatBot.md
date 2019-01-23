## Running the Chat

### Start MySQL:

Provided you've already followed the instructions in Database.md:

```bash
sudo service mysql start
```
---

### (Optional) Train the Rasa-Agent:

If changes have been made to the Rasa Agent's training data (anything in the '\dissertation\chat-interface\data' folder), the bot should be trained again with the new data.

To do this, run:

```bash
cd /chat-interface
python3 -c 'import trainer; trainer.train()'
```
---

### (Optional) Register Custom Actions:

If changes have been made to the agent's custom actions (anything in actions.py), the bot needs to re-register the new functions.

To do this, run:

```bash
python3 -m rasa_core_sdk.endpoint --actions actions
```

This will start a running process, simply Ctrl-C after it has outputted the messages indicating all the functions are registered.

---

### Running the Chat Service:

If the agent has been trained and is ready to use:

```bash
cd /chat-interface
python3 main.py
```

Then, wait until Flask prints the message:

```bash
* Debugger is active! 
```

Open your browser and visit http://127.0.0.1:5000/, be sure to check the console for messages from the running Python code.

---