import spacy
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
import json
from rasa_nlu.converters import load_data

params ={}
nlp = spacy.load('en')
training_data = load_data("./training_data.json")
config = RasaNLUConfig(cmdline_args={"pipeline": "spacy_sklearn"})
trainer = Trainer(config)
interpreter = trainer.train(training_data)

def parsing_message(message):
    default = "sorry i could not understand "
    data = interpreter.parse(message)
    for ent in data["entities"]:
         params[ent["entity"]] = ent["value"]
    if bool(params):
        return default
    else :
        return query_parsing()

def query_parsing():
    query = "select name FROM coursess"
    filters = ["{}=?".format(k) for k in params.keys()]
    conditions = " and ".join(filters)
    pass_query = " WHERE ".join([query, conditions])


def accessing_database(query):
