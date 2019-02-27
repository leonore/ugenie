from elasticsearch import Elasticsearch
from network_config import elasticIP

es = Elasticsearch([elasticIP])

# TODO tokenize?, e.g. for questions such as "who teaches X", how much is "X"
# --> only one function, returns one field
# TODO deal with duplicate courses

# Get answer to common questions about acronyms
def get_acronym_answer(query):
    res = es.search(index="general_questions", body={"query": {"match": {"question": query}}})
    first_hit = res['hits']['hits'][0]
    return first_hit['_source']['question'], first_hit['_source']['answer'] # gives answer in text

# Returns the full title of a short course according to the database
def get_sc_title(query):
    title = get_sc_field(query, 'Title')
    return title

# Returns the full title of a admissions course according to the database
def get_admissions_title(query):
    title = get_admissions_field(query, 'Lookup Name')
    return title

# Returns the most relevant course title in both the short courses and the admissions file, and returns the file type it was in
def get_course_title(query):
    # Searches the short courses and gets the most relevant result if any
    sc = es.search(index="short_courses", body={"query": {"match": {"Title": query}}})
    if sc['hits']['total'] > 0:
        sc_res = sc['hits']['hits'][0]
    else:
        sc_res = None

    # Searches the admissions courses and gets the most relevant result if any
    ad = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    if ad['hits']['total'] > 0:
        ad_res = ad['hits']['hits'][0]
    else:
        ad_res = None

    # course = the course title
    # couse_cat = the type of course file it was found in e.g. short or admissions
    # course_score = score sowing relevancy given by the elastic search
    if sc_res != None and ad_res != None:
        if sc_res['_score'] >= ad_res['_score']:
            course = sc_res['_source']['Title']
            course_cat = "SC"
            course_score = sc_res['_score']
        else:
            course = ad_res['_source']['Lookup Name']
            course_cat = "AD"
            course_score = ad_res['_score']
    elif sc_res != None:
        course = sc_res['_source']['Title']
        course_cat = "SC"
        course_score = sc_res['_score']
    elif ad_res != None:
        course = ad_res['_source']['Lookup Name']
        course_cat = "AD"
        course_score = ad_res['_score']
    else:
        return None, None, None

    return course, course_cat, course_score

# Get specific field for given short course
# e.g.  fees, tutor, course description, credits attached, subject area
def get_sc_field(query, field):
    res = es.search(index="short_courses", body={"query": {"match": {"Title": query}}})
    first_hit = res['hits']['hits'][0]
    return  first_hit['_source'][field], first_hit['_score']

# Get specific field for given admissions course
# e.g. title, start date, int fee
def get_admissions_field(query, field):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]
    return first_hit['_source'][field]

# Returns a string informing the start time, end time, start date, end date and title if exist
def get_sc_times(query):
    # duration = number of days a course runs for
    # title = title of the course according to the database
    # start_time, end_time = military time of when the course begins and ends in a days#
    # start_data, end_date = calender dates of begining and end of course
    res = es.search(index="short_courses", body={"query": {"match": {"Title": query}}})
    first_hit = res['hits']['hits'][0]['_source']
    duration = first_hit['Duration (days)']
    title = first_hit['Title']
    start_time, end_time = first_hit['Start time'], first_hit['End time']

    # If the course is a short course then there is no reason to tell the end date
    if duration is not 1:
        start_date, end_date = first_hit['Start date'], first_hit['End date']
        answer = "%s starts on %s and ends on %s, and runs from %s to %s" % (title.title(), start_date, end_date, start_time, end_time)
    else:
        date = first_hit['Start date']
        answer = "%s runs from %s to %s on %s" % (title.title(), start_time, end_time, date)
    return answer

# Returns the year in which the course starts and informs if it begins in january
def get_ad_times(query):
    # title = title of the course according to the database
    # term = year the course begins
    # january = boolean if the course begins in January of not
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]['_source']
    title = first_hit['Lookup Name']
    term = first_hit['Admit Term']
    january = first_hit['JanuaryStart']

    # If the course begins in January, then it will specify,
    # Otherwise it will not mention the start month as we do not have more information
    if january:
        answer = "%s starts in %s and begins in January." % (title.title(), term)
    else:
        answer = "%s starts in %s" % (title.title(), term)
    return answer

## IN WORK ##
# Returns the requirements for an admissions course
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

# Returns the home fee and internaitonal fee of an admissions course
# For now we return all the fee information we have for the admissions courwse, whether the user is international or not
def get_ad_fees(query):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]['_source']
    title = first_hit['Lookup Name']
    home_fee = first_hit['Home Fee']
    int_fee = first_hit['Int Fee']
    response = "%s costs £%s if you are from Scotland or the EU, %s costs £%s if you are from elsewhere in the UK or abroad." % (title.title(), str(home_fee), title.title(), str(int_fee))
    return response

# Returns the kind of course an admissions course is
def get_ad_description(query):
    # title = title of course according to the database
    # desc = short title for type of courses e.g. Education PGT
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]
    title = first_hit['_source']['Lookup Name']
    desc = first_hit['_source']['Apply Centre Description']
    response = "%s is a %s course" % (title.title(), desc)
    return response, first_hit['_score']

# Returns the meaning of the acronym given
def get_acronym_desc(query):
    res = es.search(index="general_questions", body={"query": {"match": {"answer":query}}})
    if res['hits']['hits']:
        # acro = acronym given e.g. FT
        # response = meaning of acronym
        # score = how relevant the acronym was to the one searched
        first_hit = res['hits']['hits'][0]
        response = first_hit['_source']['answer']
        acro = first_hit['_source']['question']
        score = first_hit['_score']
        return acro, response, score
    else:
        return None, None, None

# Returns the course description or the terminology explanation depending on which was aksed
def get_description(query):
    # ct = course title
    # cat = course category
    # cscore = relevancy score for course from elastic search
    # acro = acronym
    # acro_desc = acronym's expansion
    # acro_score = relevancy score of acronym from elastic search
    ct, cat, cscore = get_course_title(query)
    acro, acro_desc, acro_score = get_acronym_desc(query)

    if cscore != None and acro_score != None:
        if cscore >= acro_score: # if course was more relevant
            if cat == "SC": # if course was a short coures
                course_desc, score = get_sc_field(query, 'Course description')
                desc = str(ct).title() + " is: " + str(course_desc)
                topic = ct
            elif cat == "AD": # if course was a admissions course
                desc, score = get_ad_description(query)
                topic = ct
        else: # if acronym was more relevant
            desc = acro_desc
            topic = acro
    elif cscore != None: # if course was the only result
        if cat == "SC": # if course was a short course
            course_desc, score = get_sc_field(query, 'Course description')
            desc = str(ct).title() + " is: " + str(course_desc)
            topic = ct
        elif cat == "AD": # if course was a admissions course
            desc, score = get_ad_description(query)
            topic = ct
        else:
            response = "Sorry, I could not find any details for that"
            return False, False

    elif acro_score != None: # if acornym was more relevant
        desc = acro_desc
        topic = acro

    else: # if both course and acronym were irrelevant
        response = "Sorry, I could not find any details for that"
        return False, False

    # topic = title of course or acronyms
    # desc = course description or acronym expansion
    return topic, desc

# Returns the tutor's name and a list of classes that they teach
def get_tutor_courses(query):
    # couse_list = list of courses the tutor teaches
    # res_len = lenght of list of relevant results
    # tutor = name of tutor according to the database
    res = es.search(index="short_courses", body={"query": {"match": {"Tutor": query}}})
    course_list = ""
    res_len = 0
    if res['hits']['total']:
        res_len = len(res['hits']['hits'])
        first_hit = res['hits']['hits'][0]
        tutor = first_hit['_source']['Tutor']

    if res_len == 0: # if they teach 0 courses
        return False, False
    elif res_len == 1: # if they teach 1 course
        course_list = str(res['hits']['hits'][0]['_source']['Title']).title()
    elif res_len > 1: # if they teach more than one course
        # for loop and if used to make sure the list is grammatically correct
        # e.g. "one, two, three, and four"
        for counter in res['hits']['hits']:
            if counter != res['hits']['hits'][res_len-1]:
                print(counter['_source']['Title'])
                course_list += str(counter['_source']['Title']).title() + ", "
        course_list += " and " + str(res['hits']['hits'][res_len-1]['_source']['Title']).title()

    return tutor, course_list

def return_sc_list(res):
    course_list = ""
    res_len = len(res['hits']['hits'])

    for counter in res['hits']['hits']:
        if counter != res['hits']['hits'][res_len-1]:
            # print(counter['_source']['Title'])
            course_list += str(counter['_source']['Title']).title() + ", "
    course_list += " and " + str(res['hits']['hits'][res_len-1]['_source']['Title']).title()
    return course_list

def return_ad_list(res):
    course_list = ""
    res_len = len(res['hits']['hits'])

    for counter in res['hits']['hits']:
        if counter != res['hits']['hits'][res_len-1]:
            # print(counter['_source']['Title'])
            course_list += str(counter['_source']['Lookup Name']).title() + ", "
    course_list += " and " + str(res['hits']['hits'][res_len-1]['_source']['Lookup Name']).title()
    return course_list

def return_list(set):
    course_list = ""
    course_len = len(set)
    for counter in set:
        if counter != set[course_len-1]:
            # print(counter['_source']['Title'])
            course_list += str(counter).title() + ", "
    course_list += " and " + str(set[course_len-1]).title()
    return course_list

def get_sc_type_courses(query):
    res = es.search(index="short_courses",
    body={"query":{
            "bool":{
                "should":[
                    {"match":{
                    "Title":query
                    }},
                    {"match":{
                    "Subject area":query
                    }}
                ],
                "minimum_should_match":1
            }
    }
    })
     # {"match": {"Title": query}}})
    # print(res)
    # print(return_list(res))
    course_list = return_sc_list(res)

    course_list = []
    course_set = []

    if res:
        for course in (res['hits']['hits']):
            course_list.append(course['_source'].get("Title"))

            course_set = list(set(course_list))
        # print("Course Set = ", course_set)
        course_list = return_list(course_set)

    print(couse_set)
    if len(course_set) > 1:
        course_list = return_list(course_set)
        return course_list, res['hits']['total']
    elif len(course_set) == 1:
        return str(course_set[0]).title(), res['hits']['total']
    else:
        return False, False



def get_ad_type_courses(query):
    res = es.search(index="admissions",
    body={"query":{
            "bool":{
                "should":[
                    {"match":{
                    "Lookup Name":query
                    }},
                    {"match":{
                    "Apply Centre Description":query
                    }}
                ],
                "minimum_should_match":1
            }
    }
    })
     # {"match": {"Title": query}}})
    course_list = []
    course_set = []
    # print(res)
    if res:
        for course in (res['hits']['hits']):
            # print(course['_source'].get("Lookup Name"))
            course_list.append(course['_source'].get("Lookup Name"))

        course_set = list(set(course_list))

    # print("Course Set = ", course_set)
    # print(return_list(res))
    # hits = res[]
    # print(list(set(classes)))
    print(course_set)
    if len(course_set) > 1:
        course_list = return_list(course_set)
        return course_list, res['hits']['total']
    elif len(course_set) == 1:
        return str(course_set[0]).title(), res['hits']['total']
    else:
        return False, False


# print(get_sc_type_courses("History"))
# print(get_sc_type_courses("Languages"))
# print(get_ad_type_courses("Medicine"))
# print(get_ad_type_courses("Arts"))
# print(get_sc_type_courses("Spanish"))
# print(get_sc_type_courses("Chinese"))
# print(get_ad_type_courses("Vietnamese"))
