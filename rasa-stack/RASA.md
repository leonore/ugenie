### Steps to using the RASA Stack

```bash
cd rasa-stack
pip install -r requirements.txt
```

1. Create NLU examples
= define the user messages your bot should understand        
= define the intents and providing ways users might express them         

in nlu_data.md

2. Define the NLU model config
for us, either `spacy_sklearn` or `tensorflow_embedding` (if we get over 1000 utterances)

3. Train the model with your examples
= learn to understand what the user says
```bash
make train-nlu
```

4. Test the model
see test_file.py

---
It is possible to only get intents with steps 1-4. That's Rasa NLU.     
But Rasa Core allows the bot to follow a story. See below:     

5.  Write stories
= teaching your bot to respond      
= rasa core will train the dialogue model and predict response based on the specific state of the convo       

A story is a real conversation between a user and a bot where user inputs are expressed as intents and the responses of the bot are expressed as action names.
e.g. saying hello back:

```
## story1
* greet # lines with * are messages written by the user
   - utter_greet # lines with - are actions taken by your bot
```

In this case, all of our actions are just messages sent back to the user, like utter_greet, but in general, an action can do anything, including calling an API and interacting with the outside world (see https://rasa.com/docs/core/customactions/).

6. Define a domain
= the universe your bot lives in      
= what user inputs it should expect to get, what actions it should be able to predict, how to respond, what info to store       

in domain.yml

Rasa Core’s job is to choose the right action to execute at each step of the conversation. Simple actions are just sending a message to a user. These simple actions are the actions in the domain, which start with utter_. They will just respond with a message based on a template from the templates section. See customactions for how to build more interesting actions.

7. Train the dialogue model
```bash
make train-core
```

8. Talk to your bot
```bash
make cmdline
```
(ignore warnings)

for basic template answers.     
Right now I've only coded in basic one liner stories. Try:
```bash
hey bot!
thanks bot
im testing you
that was wrong
```
