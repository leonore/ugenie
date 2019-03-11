from elasticsearch import Elasticsearch
import os, time

# leave elastic time to setup before populating + testing
if os.environ.get('DOCKER'):
    time.sleep(52)
    elasticIP = "elastic"
else:
    time.sleep(20)
    elasticIP = "localhost"

es = Elasticsearch([elasticIP], port=9200)

health = es.cluster.health()

assert(health['status'] == ('yellow' or 'green'))
assert(es.indices.exists(["admissions", "short_courses", "common_questions"]))
print("Database holds all 3 indexes for admissions, short courses, and common questions!\
        \nYou can `make populate` if you're not sure it's up to date.")
