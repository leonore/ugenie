import argparse
import warnings

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.trackers import DialogueStateTracker
from rasa_core.slots import TextSlot
from rasa_core.events import SlotSet

from model.network_config import actionIP

# Start Rasa-Core Agent
interpreter = RasaNLUInterpreter('model/agent-data/models/nlu/default/current')
action_endpoint = EndpointConfig(url=actionIP)
agent = Agent.load('model/agent-data/models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)

# Handle user message and return responses from training data
def getResponse(sessionId, message):
    responses = agent.handle_text(message, sender_id=sessionId)
    print('Rasa-Core responses: ', responses)
    if(len(responses) > 0):
        returnResponses = []
        for response in responses:
            if 'buttons' in response:
                returnResponses.append({'text': response['text'], 'buttons': response['buttons']}) 
            else:
                returnResponses.append({'text': response['text']})
        return returnResponses
    else:
        return {'text': "Sorry, I didn't understand, could you rephrase that?"}
