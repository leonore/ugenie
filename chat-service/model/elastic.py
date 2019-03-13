from elasticsearch import Elasticsearch
from network_config import elasticIP

import datetime
import calendar

es = Elasticsearch([elasticIP])

### good functions as a starting point ###
# Get specific field for a given course
def get_sc_field(course, field):
    res = es.search(index="short_courses", body={"query": {"match": {"Title": course}}})
    first_hit = res['hits']['hits'][0]
    return  first_hit['_source'][field], first_hit['_score']

def get_admissions_field(course, field):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": course}}})
    first_hit = res['hits']['hits'][0]
    return first_hit['_source'][field], first_hit['_score']


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
    # course_cat = the type of course file it was found in e.g. short or admissions
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

# given a course, return a link if available
# action_check_course will have ran in actions
def get_sc_course_link(course):
    res = es.search(index="short_courses", body={"query": {"match": {"Title": course}}})
    first_hit = res['hits']['hits'][0]

    # specifiation is a typo within the given dataset
    link = first_hit['_source']["Link to Course specifiation"]

    if link == "N/A":
        return False
    else:
        return link

# given a query in a short-course context
# parse common questions and find most suitable link to answer
def get_sc_resource_link(query):
    res = es.search(index="common_questions", body={"query": {"match": {"question": query}}})

    try:
        first_hit = res['hits']['hits'][0]
    except:
        return False

    resource = first_hit['_source']["answer"]
    return resource

## TODO: move string formatting over to actions.py
# Returns a string informing the start time, end time, start date, end date and title if exist
def get_sc_times(course):
    # duration = number of days a course runs for
    # title = title of the course according to the database
    # start_time, end_time = military time of when the course begins and ends in a days#
    # start_data, end_date = calender dates of begining and end of course
    res = es.search(index="short_courses", body={"query": {"match": {"Title": course}}})
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

## TODO: move string formatting over to actions.py
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
def get_admission_requirements(course, requirement_type):
    #if requirement_type is "ielts":
    #    field = "IELTS requirements"
    #elif requirement_type is "general":
    #    field = "Ent Req"
    #    return False
    field = requirement_type
    try:
        res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": course}}})
        print(res)
    except:
        return "course_not_found"

    try:
        first_hit = res['hits']['hits'][0]
    except:
        return "course_not_found"

    requirements = first_hit['_source'][field]
    return requirements

## TODO: move string formatting over to actions.py
## assumes a course has been found
def check_pt_ft_course(course):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": course}}})
    hits = res['hits']['hits']
    cont = False
    run_list = list()
    for hit in hits:
        if hit['_source']['Lookup Name'] == course and hit['_source']['Admit Term'] == 2019:
            cont = True
            if hit['_source']['PT'] and "part-time" not in run_list:
                run_list.append("part-time")
            elif hit['_source']['FT'] and "full-time" not in run_list:
                run_list.append("full-time")

    if not cont or not run_list:
        response = "Sorry, it does not seem this course is running this year."
    else:
        response = str(course).title() + " runs " + ', '.join(run_list)

    return response

## TODO: move string formatting over to actions.py
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

## TODO: move string formatting over to actions.py
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
    # acronyms are mentioned in both the question and answer so checking over multiple fields
    res = es.search(index="common_questions",
                    body={"query": {
                            "multi_match" : {
                              "query":    query,
                              "fields": [ "question", "answer" ] }
                        }})

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

## TODO: move string formatting over to actions.py
# Returns the course description or the terminology explanation depending on which was asked
# Elastic's scoring feature is very useful to check what answer is most suitable to the query
# Hence why this function is not decoupled for admissions, short courses, terminology
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
            return False, False

    elif acro_score != None: # if acronym was more relevant
        desc = acro_desc
        topic = acro

    else: # if both course and acronym were irrelevant
        return False, False

    # topic = title of course or acronyms
    # desc = course description or acronym expansion
    return topic, desc

# Returns the tutor's name and a list of classes that they teach
def get_tutor_courses(query):
    # course_list = list of courses the tutor teaches
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
                # print(counter['_source']['Title'])
                course_list += str(counter['_source']['Title']).title() + ", "
        course_list += " and " + str(res['hits']['hits'][res_len-1]['_source']['Title']).title()

    return tutor, course_list


# Returns a list formatted user-friendly
# e.g. [1,2,3,4] -> "1, 2, 3, and 4"
def return_list(set):
    course_list = ""
    course_len = len(set)
    if course_len > 1:
        for counter in set:
            if counter != set[course_len-1]:
                # print(counter['_source']['Title'])
                course_list += str(counter).title() + ", "
        course_list += " and " + str(set[course_len-1]).title()
    else:
        course_list = set[0]
    return course_list

# Returns a list of relevant courses from the short courses file
def get_sc_type_courses(query):
    # Elasticsearch to match both the title of the course and subject area for relevancy
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
            }
        }})

    course_list = []
    course_set = []

    # Creates a list of the top 10 matched courses then turns it into a list to remove duplicates
    if res:
        for course in (res['hits']['hits']):
            course_list.append(course['_source'].get("Title"))
        course_set = list(set(course_list))
    # course_set_unformatted = course_set
    # If len > 1 we return a formatted list
    if len(course_set) > 1:
        # course_set = return_list(course_set)
        return course_set, res['hits']['total']
    # If len = 1 we return the single course
    elif len(course_set) == 1:
        return list(str(course_set[0]).title()), res['hits']['total']
    # If len < 1 if means we matched no courses so we return false
    else:
        return False, False

# Returns a list of relevant courses from the admissions courses file
def get_ad_type_courses(query):
    # Elasticsearch to match both the title of the course and subject area for relevancy
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
            }
        }})

    course_list = []
    course_set = []

    # Creates a list of the top 10 matched courses then turns it into a list to remove duplicates
    if res:
        for course in (res['hits']['hits']):
            course_list.append(course['_source'].get("Lookup Name"))
        course_set = list(set(course_list))

    # If len > 1 we return a formatted list
    if len(course_set) > 1:
        # course_list = return_list(course_set)
        return course_list, res['hits']['total']
    # If len = 1 we return the single course
    elif len(course_set) == 1:
        return str(course_set[0]).title(), res['hits']['total']
    # If len < 1 if means we matched no courses so we return false
    else:
        return False, False

def monthToNum(month):
    month = month.title()
    month = month[:3]
    number = list(calendar.month_abbr).index(month)
    return number

def weekdayToNum(day):
    day = day.title()
    day = day[:3]
    number = list(calendar.day_abbr).index(day)
    return number

def fullify_sc_list(course_list):
    full_list = []
    for course in course_list:
        # print("Course = ", course)
        res = es.search(index="short_courses", body={"query": {"match_phrase": {"Title": course}}})
        for instance in res['hits']['hits']:
            # print("Instance = ", instance['_source']["Title"])
            full_list.append(instance["_source"])
    return full_list

def filterForMonths(month, course_list):
    print("course list = ", course_list)
    filtered_course_list = []
    month_dec = monthToNum(month)
    full_course_list = fullify_sc_list(course_list)
    for course in full_course_list:
        starting_date = course["Start date"].split("/")
        starting_month = starting_date[1]
        if int(starting_month) == month_dec:
            # print(course["Title"], starting_date)
            filtered_course_list.append(course["Title"])

    filtered_course_set = list(set(filtered_course_list))
    if filtered_course_set:
        return filtered_course_set
        # return return_list(filtered_course_set)
    else:
        return False

def filterForWeekday(weekday, course_list):
    print("course list = ", course_list)
    filtered_course_list = []
    weekday_dec = weekdayToNum(weekday)
    full_course_list = fullify_sc_list(course_list)
    for course in full_course_list:
        sd = course["Start date"].split("/")
        starting_date = datetime.datetime(int(sd[2]), int(sd[1]), int(sd[0]))
        # print(starting_date.weekday())
        if starting_date.weekday() == weekday_dec:
            # print(starting_date)
            filtered_course_list.append(course['Title'])

    filtered_course_set = list(set(filtered_course_list))
    if filtered_course_set:
        return filtered_course_set
        # return return_list(filtered_course_set)
    else:
        return False

# print(get_sc_type_courses("music")[2])
# print(filterForMonths("april", get_sc_type_courses("art")[0]))
# print(filterForWeekday("thursday", get_sc_type_courses("spanish")[0]))
# print(weekdayToNum("Tue"))
# print(weekdayToNum("wednesday"))
# print(weekdayToNum("Friday"))
# print(monthToNum("March"))
# print(monthToNum("july"))
# print(monthToNum("nov"))
