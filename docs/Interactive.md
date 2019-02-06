## Running Interactive Mode

### Start Elastic:

Provided you've already followed the instructions in Elastic.md:

```bash
sudo -i service elasticsearch start
```

### Running in Interactive Learning mode:

Open two terminals, in the first run:
```bash
python3 -m rasa_core_sdk.endpoint --actions actions
```

This will start the running action endpoint process, leave that running and in the second terminal enter:
```bash
cd /chat-service/model
python3 -c 'import trainer; trainer.train_interactive()'
```

In the second terminal, wait a while for it to perform the initial training, then when prompted for user input begin to converse with it and give feedback on its responses.
You can track the flow of the conversation in your browser by going to "http://localhost:5005/visualization.html".

---