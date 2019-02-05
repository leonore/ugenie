import argparse
import warnings

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.trackers import DialogueStateTracker
from rasa_core.slots import TextSlot
from rasa_core.events import SlotSet

import os

class SessionAgent:
    # Start Rasa-Core Agent
    def __init__(self):
        interpreter = RasaNLUInterpreter(os.path.dirname(os.path.realpath(__file__)) + '/agent-data/models/nlu/default/current')
        action_endpoint = EndpointConfig(url='http://localhost:5055/webhook')
        self.agent = Agent.load(os.path.dirname(os.path.realpath(__file__)) + '/agent-data/models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)

    # Handle user message and return response from training data
    def getResponse(self, message):
        responses = self.agent.handle_text(message)
        print('Rasa-Core responses: ', responses)
        if(len(responses) > 0):
            return responses[0]['text']
        else:
            return "Sorry, I didn't understand, could you rephrase that?"
