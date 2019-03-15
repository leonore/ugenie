from elasticsearch import Elasticsearch

es = Elasticsearch(["localhost"], port=9200)

health = es.cluster.health()

assert(health['status'] == ('yellow' or 'green'))
print("Database is healthy!")

assert(es.indices.exists(["admissions", "short_courses", "common_questions"]))
print("Database holds all 3 indexes for admissions, short courses, and common questions!\
        \nYou can `make populate` if you're not sure it's up to date.")
