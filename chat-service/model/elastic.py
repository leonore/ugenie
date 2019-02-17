from elasticsearch import Elasticsearch

#es = Elasticsearch([{'host': 'elastic', 'port': 9200}]) # FOR DOCKER
es = Elasticsearch(['host': 'localhost', 'port': 9200]) # FOR LOCAL DEPLOYMENT

# TODO tokenize?, e.g. for questions such as "who teaches X", how much is "X"
# --> only one function, returns one field
# TODO deal with duplicate courses

# get answer to common questions about ADMISSIONS acronyms
def get_acronym_answer(query):
    res = es.search(index="general_questions", body={"query": {"match": {"question": query}}})
    first_hit = res['hits']['hits'][0]
    return first_hit['_source']['question'], first_hit['_source']['answer'] # gives answer in text


# returns the full title of a short course
def get_sc_title(query):
    title = get_sc_field(query, 'Title')
    return title

# returns the full title of a admissions course
def get_admissions_title(query):
    title = get_admissions_field(query, 'Lookup Name')
    return title

# returns the most relevant course title in both the short courses and the admissions file, and returns the file it was in
def get_course_title(query):
    print("ES Get course title")
    # title = get_sc_field(query, 'Title')
    # res = es.search(index="short_courses, admissions", body={"query":{"dis_max":{"queries":[{"match": {"Title": query}}, {"match":{"Lookup Name": query}}]}}})
    # res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    #
    # first_hit = res['hits']['hits'][0]
    # print('HIT = ' + str(res['hits']['hits'][0]))
    # print('Score 0 = ' + str(res['hits']['hits'][0]['_score']))
    # print('Score 1 = ' + str(res['hits']['hits'][1]['_score']))
    # course1 = first_hit['_source']['Lookup Name']
    # print('Course = ' + course1)
    # if sc_res['hits']['max_score'] || ad_res['hits']['max_score']:

    sc = es.search(index="short_courses", body={"query": {"match": {"Title": query}}})
    # print(str(sc))
    if sc['hits']['total'] > 0:
        sc_res = sc['hits']['hits'][0]
    else:
        sc_res = None

    ad = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    if ad['hits']['total'] > 0:
        ad_res = ad['hits']['hits'][0]
    else:
        ad_res = None

    if sc_res != None and ad_res != None:
        print('We have both with SC Score = ' + str(sc_res['_score']) + ', and AD Score = ' + str(ad_res['_score']))
        if sc_res['_score'] >= ad_res['_score']:
            print("SC = " + str(sc_res))
            course = sc_res['_source']['Title']
            course_cat = "SC"
            course_score = sc_res['_score']
        else:
            print("AD = " + str(ad_res))
            course = ad_res['_source']['Lookup Name']
            course_cat = "AD"
            course_score = ad_res['_score']
    elif sc_res != None:
        print("SC = " + str(sc_res))
        course = sc_res['_source']['Title']
        course_cat = "SC"
        course_score = sc_res['_score']
    elif ad_res != None:
        print("AD = " + str(ad_res))
        course = ad_res['_source']['Lookup Name']
        course_cat = "AD"
        course_score = ad_res['_score']
    else:
        print("Not a Course")
        return None, None, None

    print("Course = " + course)
    return course, course_cat, course_score
    # return first_hit['_source']['Lookup Name']
    # return title


# get specific field for given short course: fees, tutor, course description, credits attached, subject area
def get_sc_field(query, field):
    res = es.search(index="short_courses", body={"query": {"match": {"Title": query}}})
    first_hit = res['hits']['hits'][0]
    return  first_hit['_source'][field], first_hit['_score'] # gives field in text

# get specfic field for a give admissions course: int fees, rio, ielts requirements EndpointConfig
# def get_ad_field(query, feild):
#     res

# get specific field for given admissions course: title, start date, int fee e.t.c.
def get_admissions_field(query, field):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]
    return first_hit['_source'][field]

# returns a string informing the start time, end time, start date, end date and title if exist
def get_sc_times(query):
    res = es.search(index="short_courses", body={"query": {"match": {"Title": query}}})
    first_hit = res['hits']['hits'][0]['_source']
    duration = first_hit['Duration (days)']
    title = first_hit['Title']
    start_time, end_time = first_hit['Start time'], first_hit['End time']

    if duration is not 1:
        start_date, end_date = first_hit['Start date'], first_hit['End date']
        answer = "%s starts on %s and ends on %s, and runs from %s to %s" % (title.title(), start_date, end_date, start_time, end_time)
    else:
        date = first_hit['Start date']
        answer = "%s runs from %s to %s on %s" % (title.title(), start_time, end_time, date)
    return answer

# returns the year in which the course starts and informs if it begins in january
def get_ad_times(query):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]['_source']
    title = first_hit['Lookup Name']
    term = first_hit['Admit Term']
    january = first_hit['JanuaryStart']

    if january:
        answer = "%s starts in %s and begins in January." % (title.title(), term)
    else:
        answer = "%s starts in %s" % (title.title(), term)
    return answer

# returns the requirements for an admissions course
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

# returns the home fee and internaitonal fee of an admissions course
def get_ad_fees(query):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]['_source']
    title = first_hit['Lookup Name']
    home_fee = first_hit['Home Fee']
    int_fee = first_hit['Int Fee']
    response = "%s costs £%s if you are from Scotland or the EU, %s costs £%s if you are from elsewhere in the UK or abroad." % (title.title(), str(home_fee), title.title(), str(int_fee))
    return response

# returns the kind of course an admissions course is
def get_ad_description(query):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]
    title = first_hit['_source']['Lookup Name']
    desc = first_hit['_source']['Apply Centre Description']
    response = "%s is a %s course" % (title.title(), desc)
    return response, first_hit['_score']

def get_acronym_desc(query):
    # print(next(question["answer"] for question in general_questions if question["question"] == "FT"))
    # res = (next(question["answer"] for question in general_questions if question["question"] == query))
    res = es.search(index="general_questions", body={"query": {"match": {"answer":query}}})
    if res['hits']['hits']:
        first_hit = res['hits']['hits'][0]
    # print (first_hit['_source']['answer'])
        response = first_hit['_source']['answer']
        acro = first_hit['_source']['question']
        score = first_hit['_score']
        return acro, response, score
    else:
        return None, None, None

# returns the course desciption or the terminology explanation depending on which was aksed
def get_description(query):
    ct, cat, cscore = get_course_title(query)
    acro, acro_desc, acro_score = get_acronym_desc(query)

    if cscore != None and acro_score != None:
        if cscore >= acro_score:
            if cat == "SC":
                course_desc, score = get_sc_field(query, 'Course description')
                desc = str(ct).title() + " is: " + str(course_desc)
                topic = ct
            elif cat == "AD":
                desc, score = get_ad_description(query)
                topic = ct
        else:
            desc = acro_desc
            topic = acro
    elif cscore != None:
        if cat == "SC":
            course_desc, score = get_sc_field(query, 'Course description')
            desc = str(ct).title() + " is: " + str(course_desc)
            topic = ct
        elif cat == "AD":
            desc, score = get_ad_description(query)
            topic = ct
        else:
            response = "Sorry, I could not find any details for that"
            return False, False

    elif acro_score != None:
        desc = acro_desc
        topic = acro

    else:
        response = "Sorry, I could not find any details for that"
        return False, False

    # elif cscore == None:
    #     if acro_score == None:
    #         response = "Sorry, I could not find any details for that"
    #     elif acro_score != None:
    #         desc = acro
    # elif acro_score == None:
    #     if cat == "SC":
    #         desc = get_sc_field(query, 'Course description')
    #     elif cat == "AD":
    #         desc = get_ad_description(query)
    # else:


    # print("Meaning = " + str(desc))
    # print("Topic = " + str(topic) + ", and desc = " + str(desc))
    return topic, desc

#print(get_sc_field("Botanical painting and illustration", "Course description"))
#print(get_sc_field("Impressionism 1860-1900", "Course description"))
#print(get_sc_field("SPANISH STAGE 2", "Course description"))

#print(get_sc_times("Ancient Medicine: Theory and Practice"))
#print(get_sc_times("SPANISH STAGE 2"))
#print(get_sc_times("Scottish history in maps"))

# print(get_sc_times("French stage 1"))
# print(get_course_title("Brain Sciences"))
# print(get_course_title("French Stage 1"))
# print(get_course_title("Orkney"))
# print(get_course_title("Film"))
# print(get_course_title("Film Studies"))
# print(get_acronym_desc("FT"))

# print(get_description("french study 1"))
# print(get_description("brain science"))
# print(get_description("FT"))
# print(get_description("french"))
