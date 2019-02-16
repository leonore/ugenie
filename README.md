# CS01 - Virtual Assistant for UofG's External Relations

The External Relations Project is to create a **virtual assistant / chatbot** that will help answer the increasing volume of application and course enquiries at the 
University of Glasgow's External Relations Directorate.     

Our system consists of:
* an interface for users to interact with the chatbot, 
* connected to a Natural Language Understanding unit (RASA)
* which makes queries to a free-text search engine, the Elastic database

Get yourself set up with dependencies:
```bash
pip install rasa_core
pip install rasa_nlu[spacy]
python -m spacy download en
pip install flask-socketio
pip install elasticsearch
pip install xlrd
```
Provided your python is python 3.

Visit [docs](http://stgit.dcs.gla.ac.uk/tp3-2018-cs01/dissertation/tree/master/docs) for more specific information on the different components in the project.