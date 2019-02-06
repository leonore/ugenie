from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# TODO confirm_query question for things such as clarifying courses
# TODO tokenize?, e.g. for questions such as "who teaches X", how much is "X"
# --> only one function, returns one field
# TODO deal with duplicate short_courses

# get answer to common questions about ADMISSIONS acronyms
def get_acronym_answer(query):
    res = es.search(index="general_questions", body={"query": {"match": {"question": query}}})
    first_hit = res['hits']['hits'][0]
    return first_hit['_source']['question'], first_hit['_source']['answer'] # gives answer in text

# returns the full title of course
def get_sc_title(query):
    title = get_sc_field(query, 'Title')
    return title

# get specific field for given short course: fees, tutor, course description, credits attached, subject area
def get_sc_field(query, field):
    res = es.search(index="short_courses", body={"query": {"match": {"Title": query}}})
    first_hit = res['hits']['hits'][0]
    return  first_hit['_source'][field] # gives field in text

def get_sc_times(query):
    res = es.search(index="short_courses", body={"query": {"match": {"Title": query}}})
    first_hit = res['hits']['hits'][0]['_source']
    duration = first_hit['Duration (days)']
    title = first_hit['Title']
    start_time, end_time = first_hit['Start time'], first_hit['End time']
    if duration is not 1:
        start_date, end_date = first_hit['Start date'], first_hit['End date']
        answer = "%s starts on %s and ends on %s, and runs from %s to %s" % (title, start_date, end_date, start_time, end_time)
    else:
        date = first_hit['Start date']
        answer = "%s runs from %s to %s on %s" % (title, start_time, end_time, date)
    return answer

def get_admission_requirements(query, requirement_type):
    if requirement_type is "ielts":
        field = "IELTS requirements"
    elif requirement_type is "general":
        field = "Ent Req"
    else:
        return False

    res = es.search(index="admissions", body={"query": {"match": {"Title": query}}})
    first_hit = res['hits']['hits'][0]
    return first_hit['_source'][field]

#print(get_sc_field("Botanical painting and illustration", "Course description"))
#print(get_sc_field("Impressionism 1860-1900", "Course description"))
#print(get_sc_field("SPANISH STAGE 2", "Course description"))

#print(get_sc_times("Ancient Medicine: Theory and Practice"))
#print(get_sc_times("SPANISH STAGE 2"))
#print(get_sc_times("Scottish history in maps"))
