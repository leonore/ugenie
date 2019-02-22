# don't forget to launch ES if running outside docker
from elasticsearch import Elasticsearch, helpers
from load_questions import general_questions, short_questions
import xlrd, datetime, os, time

if os.environ.get('DOCKER'):
    # Elastic needs time start up in Docker container
    # startup time is slow but was tested from the Google Cloud VM
    time.sleep(45)
    elasticIP = "elastic"
else: # LOCAL DEPLOYMENT
    elasticIP = "localhost"

book1 = xlrd.open_workbook('data/short_courses.xlsx')
wb1 = book1.sheet_by_index(0)

book2 = xlrd.open_workbook('data/admissions.xlsx')
wb2 = book2.sheet_by_index(0)

def parse_value(cell):
    try:
        # we check for date first
        new_val = datetime.datetime.strptime(str(cell), '%d/%m/%Y').strftime("%d/%m/%Y")
    except ValueError: # this isn't a date
        try:
            new_val = int(cell)
        except ValueError:
            if "£" in cell and len(cell)<10:
                new_val = int(float(cell.strip("£")))
            else:
                new_val = cell
    if new_val:
        return new_val
    else:
        return None

def read_into_list(wb):
    fields = []
    content = []
    for i in range(wb.nrows):
        row = wb.row_values(i)
        if i == 0:
            fields = row
        else:
            current = {}
            for j in range(len(row)):
                current[fields[j]] = parse_value(row[j])
            current['index'] = i
            content.append(current)
    return content

sc_courses = read_into_list(wb1)
adm_courses = read_into_list(wb2)

# read short courses data
actions1 = [
    {
    "_index" : "short_courses",
    "_type" : "external",
    "_id" : str(node['index']),
    "_source" : node
    }
for node in sc_courses
]

# read general courses data
actions2 = [
    {
    "_index" : "admissions",
    "_type" : "external",
    "_id" : str(node['index']),
    "_source" : node
    }
for node in adm_courses
]

# read common questions
# currently not reading in short questions
actions3 = [
    {
    "_index" : "general_questions",
    "_type" : "external",
    "_id" : str(node['index']),
    "_source" : node
    }
for node in general_questions
]

es = Elasticsearch([elasticIP], port=9200)

# the database isn't populated with all our data, repopulate
if not es.indices.exists(["admissions", "short_courses", "general_questions"]):
    # WIPE INDICES BEFORE RELOADING -- IN CASE SOMETHING WENT WRONG
    es.indices.delete("_all")

    helpers.bulk(es, actions1)
    helpers.bulk(es, actions2)
    helpers.bulk(es, actions3)
