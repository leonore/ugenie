from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import warnings

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.trackers import DialogueStateTracker
from rasa_core.slots import TextSlot
from rasa_core.events import SlotSet

# Start Rasa-Core Agent
interpreter = RasaNLUInterpreter("models/nlu/default/current")
agent = Agent.load("models/dialogue", interpreter=interpreter)
tracker = DialogueStateTracker("default", slots=[TextSlot("course")])

# Handle user message and return response from training data
def getResponse(message):
    responses = agent.handle_text(message)
    print("Rasa-Core slots: ", tracker.slots)
    print("Rasa-Core responses: ", responses)
    if(len(responses) > 0):
        return responses[0]["text"]
    else:
        return "Sorry, I didn't understand, could you rephrase that?"
