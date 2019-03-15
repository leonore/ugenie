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


# given a query in a short-course context, parse common questions and find most suitable link to answer
def get_sc_resource_link(query):
    res = es.search(index="common_questions", body={"query": {"match": {"question": query}}})

    try:
        first_hit = res['hits']['hits'][0]
    except:
        return False

    resource = first_hit['_source']["answer"]
    return resource


# Returns start time, end time, start date, end date and title if exist
def get_sc_times(course):
    res = es.search(index="short_courses", body={"query": {"match": {"Title": course}}})
    first_hit = res['hits']['hits'][0]['_source']
    course_title = first_hit["Title"]
    list_instances = fullify_sc_list([course_title])

    instance_variables = []
    for instance in list_instances:
        duration = first_hit['Duration (days)']
        title = first_hit['Title']
        start_time, end_time = first_hit['Start time'], first_hit['End time']
        start_date, end_date = first_hit['Start date'], first_hit['End date']
        instance_variables.append([title.title(), start_date, end_date, start_time, end_time, duration])

    return instance_variables


# Returns how many credits a short course is worth
def get_sc_credits(course):
    res = es.search(index="short_courses", body={"query": {"match": {"Title": course}}})
    first_hit = res['hits']['hits'][0]['_source']
    course_title = first_hit["Title"].title()
    credits = first_hit["Credits attached"]

    return course_title, credits


# Returns the year in which the course starts and informs if it begins in january
def get_ad_times(query):
    # january = boolean if the course begins in January of not
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]['_source']
    title = first_hit['Lookup Name']
    term = first_hit['Admit Term']
    january = first_hit['JanuaryStart']

    time_variables = [title.title(), term, january]
    return time_variables


# Returns the IELTS requirements for an admissions course
# this checks for requirement type for future scalability
def get_admission_requirements(course, requirement_type):

    try:
        res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": course}}})
    except:
        return "course_not_found"

    try:
        first_hit = res['hits']['hits'][0]
    except:
        return "course_not_found"

    requirements = first_hit['_source'][requirement_type]
    return requirements


# checks if an admissions course runs part time or full time
def check_pt_ft_course(course):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": course}}})
    hits = res['hits']['hits']
    cont = False # assume the course isn't continuing first (does not have a row with this year)
    run_list = list()

    # loop for the multiple rows for one course in the admissions data
    for hit in hits:
        now = datetime.datetime.now()
        if hit['_source']['Lookup Name'] == course and hit['_source']['Admit Term'] >= now.year:
            cont = True
            if hit['_source']['PT'] and "part-time" not in run_list:
                run_list.append("part-time")
            elif hit['_source']['FT'] and "full-time" not in run_list:
                run_list.append("full-time")

    if not cont or not run_list:
        return "not_running", []
    else:
        return "running", [str(course).title(), run_list]


# Returns the home fee and international fee of an admissions course
# For now we return all the fee information we have for the admissions course = failproof bot answer regardless of enquirer's nationality
def get_ad_fees(query):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]['_source']
    course_title = first_hit["Lookup Name"]
    course_instances = fullify_ad_list([course_title])
    home_fee, int_fee = None, None

    # Goes through course instances looking if they have fee data
    for course in course_instances:
        now = datetime.datetime.now()
        if course["Admit Term"] >= now.year:
            if course["Home Fee"]:
                home_fee = str(course['Home Fee'])
            if course["Int Fee"]:
                int_fee = str(course['Int Fee'])

    fee_variables = [course_title.title(), home_fee, int_fee]

    return fee_variables


# Returns the kind of course an admissions course is e.g. Education PGT
def get_ad_description(query):
    res = es.search(index="admissions", body={"query": {"match": {"Lookup Name": query}}})
    first_hit = res['hits']['hits'][0]
    title = first_hit['_source']['Lookup Name'].title() # normalise course titles if they're all caps
    desc = first_hit['_source']['Apply Centre Description']

    return title, desc, first_hit['_score']


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
        # score = how relevant the acronym was to the one searched
        first_hit = res['hits']['hits'][0]
        response = first_hit['_source']['answer']
        acronym = first_hit['_source']['question']
        score = first_hit['_score']
        return acronym, response, score
    else:
        return None, None, None


# Returns the course description or the terminology explanation depending on which was asked
# If NLU fails RASA-side, Elastic's scoring feature is very useful to check what answer is most suitable to the query
# Hence why this function is not decoupled for admissions, short courses, terminology
def get_description(query):
    # cscore = relevancy score for course from elastic search
    # acro_score = relevancy score of acronym from elastic search
    # ct = course title
    # cat = "AD" or "SC" or "acronym"

    ct, cat, cscore = get_course_title(query)
    acro, acro_desc, acro_score = get_acronym_desc(query)

    if cscore != None and acro_score != None: # both acronyms and courses were returned
        if cscore >= acro_score: # if course was more relevant
            if cat == "SC": # if course was a short coures
                course_desc, score = get_sc_field(query, 'Course description')
                title = str(ct).title()
                desc = str(course_desc)
            elif cat == "AD": # if course was a admissions course
                title, desc, score = get_ad_description(query)

        else: # if acronym was more relevant
            desc = acro_desc
            title = acro
            category = "acronym"

    elif cscore != None: # only course was returned
        if cat == "SC": # if course was a short course
            course_desc, score = get_sc_field(query, 'Course description')
            desc = str(course_desc)
            title = str(ct).title()

        elif cat == "AD": # if course was a admissions course
            title, desc, score = get_ad_description(query)

        else:
            return False, False, False

    elif acro_score != None: # if acronym was more relevant
        desc = acro_desc
        title = acro
        cat = "acronym"

    else: # if both course and acronym were irrelevant
        return False, False, False

    return cat, title, desc


# Returns the tutor's name and a list of classes that they teach
def get_tutor_courses(query):
    res = es.search(index="short_courses", body={"query": {"match": {"Tutor": query}}})
    course_list = ""
    res_len = 0 # length of list of relevant results
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
                course_list += str(counter).title() + ", "
        course_list += " and " + str(set[course_len-1]).title()
    else:
        course_list = set[0]
    return course_list

def get_type_courses(query, type):
    if type == "short":
        title, subject, index = "Title", "Subject area", "short_courses"
    elif type == "admissions":
        title, subject, index = "Lookup Name", "Apply Centre Description", "admissions"
    else:
        # this should not have been called
        return False, False

    res = es.search(index=index,
    body={"query":{
            "bool":{
                "should":[
                    {"match":{
                        title: query
                    }},
                    {"match":{
                        subject: query
                    }}
                ],
            }
        }})
    course_list = []
    course_set = []

    # Creates a list of the top 10 matched courses then turns it into a list to remove duplicates
    if res:
        for course in (res['hits']['hits']):
            course_list.append(course['_source'].get(title))
        course_set = list(set(course_list))

    if len(course_set) > 1:
        # course_set = return_list(course_set)
        return course_set, res['hits']['total'] # multiple courses were matched
    elif len(course_set) == 1:
        return str(course_set[0]).title(), res['hits']['total']  # one course was matched
    else:
        return False, False # no courses were matched
    return False, False


# Function to receive a list of courses and expand it with all the different instances of it
def fullify_sc_list(course_list):
    full_list = []
    for course in course_list:
        res = es.search(index="short_courses", body={"query": {"match_phrase": {"Title": course}}})
        for instance in res['hits']['hits']:
            full_list.append(instance["_source"])
    return full_list


# Function to receive a list of courses and expand it with all the different instances of it
def fullify_ad_list(course_list):
    full_list = []
    for course in course_list:
        res = es.search(index="admissions", body={"query": {"match_phrase": {"Lookup Name": course}}})
        for instance in res['hits']['hits']:
            full_list.append(instance["_source"])
    return full_list


# Turns month string to number (e.g. "november" -> 10)
def monthToNum(month):
    month = month.title()
    month = month[:3]
    number = list(calendar.month_abbr).index(month)
    return number

# Turns weekday string to number (e.g. "wednesday" -> 2)
def weekdayToNum(day):
    day = day.title()
    day = day[:3]
    number = list(calendar.day_abbr).index(day)
    return number


# Filters a list of courses that start in a particular month
def filterForMonths(month, course_list):
    filtered_course_list = []
    month_dec = monthToNum(month)
    full_course_list = fullify_sc_list(course_list)

    # Finds courses in the expanded list that match the designated time and adds them to the filtered list
    for course in full_course_list:
        starting_date = course["Start date"].split("/")
        starting_month = starting_date[1]
        if int(starting_month) == month_dec:
            filtered_course_list.append(course["Title"])

    # Turns the list of courses into a set to remove duplicate titles
    filtered_course_set = list(set(filtered_course_list))
    if filtered_course_set:
        return filtered_course_set
    else:
        return False

# Filters a list of courses 'course_list' that start on a particular weekday 'weekday'
def filterForWeekday(weekday, course_list):
    filtered_course_list = []
    weekday_dec = weekdayToNum(weekday)
    full_course_list = fullify_sc_list(course_list)

    # Finds courses in the expanded list that match the designated time and adds them to the filtered list
    for course in full_course_list:
        sd = course["Start date"].split("/")
        starting_date = datetime.datetime(int(sd[2]), int(sd[1]), int(sd[0]))
        if starting_date.weekday() == weekday_dec:
            filtered_course_list.append(course['Title'])

    # Turns the list of courses into a set to remove duplicate titles
    filtered_course_set = list(set(filtered_course_list))
    if filtered_course_set:
        return filtered_course_set
    else:
        return False


# Returns a formatted list of tutors of a given course
def getMultiTutors(course):
    course_instances = fullify_sc_list([course])
    tutor_list = []

    for instance in course_instances:
        tutor_list.append(instance["Tutor"])

    tutor_list = list(set(tutor_list))
    answer = return_list(tutor_list)
    return len(tutor_list), answer
