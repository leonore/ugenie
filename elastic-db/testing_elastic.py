from elasticsearch import Elasticsearch
import os, time

if os.environ.get('DOCKER'):
    # leave elastic time to setup before testing
    time.sleep(20)
    elasticIP = "elastic"
else: # LOCAL DEPLOYMENT
    elasticIP = "localhost"

es = Elasticsearch([elasticIP], port=9200)

health = es.cluster.health()

assert(health['status'] == ('yellow' or 'green'))
assert(es.indices.exists(["admissions", "short_courses", "general_questions"]))
print("Database fully populated and in good health!")
