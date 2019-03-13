#!/bin/bash

# populate the database if not populated/if files have changed
python3 populate_elastic.py

# start action server for interaction with the database
python3 -m rasa_core_sdk.endpoint --actions actions.actions
