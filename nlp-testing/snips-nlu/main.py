from __future__ import unicode_literals, print_function
import io
import json
import snips_nlu
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

with io.open("sample_datasets/flights_dataset.json") as f:
    sample_dataset = json.load(f)

snips_nlu.load_resources('snips_nlu_en')
nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
nlu_engine = nlu_engine.fit(sample_dataset)
text = "Book me a flight to go to boston this weekend"
parsing = nlu_engine.parse(text)
print(parsing["intent"]["intentName"])
