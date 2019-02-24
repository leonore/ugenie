#!/bin/bash

# populate the database if not populated (see file)
python3 populate_elastic.py
# start action server
python3 -m rasa_core_sdk.endpoint --actions actions.actions
