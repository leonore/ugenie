# tutorial: https://tryolabs.com/blog/2015/02/17/python-elasticsearch-first-steps/
#connect to our cluster
# please leave this file for testing purposes
# alternative: try from python within terminal

from elasticsearch import Elasticsearch
import requests

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#let's iterate over swapi people documents and index them
import json
r = requests.get('http://localhost:9200')

o = es.search(index="short_courses", body={"query": {"match": {'Start time':'19.15'}}})
print(o)
