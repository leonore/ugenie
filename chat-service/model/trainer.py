import platform
# checks if deployment instance is university VM, which does not support RASA training packages
if platform.platform() == "Linux-4.4.0-142-generic-x86_64-with-Ubuntu-16.04-xenial":
    print("Instance is " + platform.platform() + ", does not support Tensorflow. Exiting...")
    exit()

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.train import interactive
from rasa_core.utils import EndpointConfig

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer

import os
from network_config import actionIP

# Start Interactive Training Mode
def train_interactive():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    domain_file = 'domain.yml'
    interpreter = RasaNLUInterpreter(current_directory + '/agent-data/models/nlu/default/current')
    action_endpoint = EndpointConfig(url=actionIP)
    training_data_file = current_directory + '/agent-data/data/stories.md'
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=5), KerasPolicy()],
                  interpreter=interpreter, action_endpoint=action_endpoint)
    data = agent.load_data(training_data_file)
    agent.train(data)
    interactive.run_interactive_learning(agent, training_data_file)
    return agent

# Train Rasa-NLU Model
def train_nlu():
    training_data = load_data('agent-data/data/nlu.md')
    trainer = Trainer(config.load("nlu-config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('agent-data/models/nlu/', fixed_model_name="current")
    return model_directory

# Train Rasa-Core Dialogue Model
def train_core():
    domain_file="domain.yml"
    model_path="agent-data/models/dialogue"
    training_data_file="agent-data/data/stories.md"
    agent = Agent(
        domain_file,
        policies=[MemoizationPolicy(max_history=5), KerasPolicy()]
        )
    training_data = agent.load_data(training_data_file)
    agent.train(training_data)
    #agent.train(training_data, validation_split=0.2) --> we had this forever but it actually made the bot dumber :(
    agent.persist(model_path)
    return agent

# Train both Rasa-Core Dialogue Model and Rasa-NLU Model
def train():
    model_directory = train_nlu()
    agent = train_core()
