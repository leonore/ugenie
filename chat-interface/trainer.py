from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer

# Train Rasa-NLU Model
def train_nlu():
    training_data = load_data('data/nlu-data.json')
    trainer = Trainer(config.load("nlu-config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="current")
    return model_directory

# Train Rasa-Core Dialogue Model
def train_core():
    domain_file="domain.yml"
    model_path="models/dialogue"
    training_data_file="data/stories.md"
    agent = Agent(
        domain_file,
        policies=[MemoizationPolicy(max_history=3), KerasPolicy()]
        )
    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        validation_split=0.2
        )
    agent.persist(model_path)
    return agent

# Train both Rasa-Core Dialogue Model and Rasa-NLU Model
def train():
    model_directory = train_nlu()
    agent = train_core()
