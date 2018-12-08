# https://pythonspot.com/orm-with-sqlalchemy/

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import GeneralCourse, ShortCourse, GeneralQuestion, ShortQuestion

from xls_helper import *

# MySQL-connector-python
# dialect+driver://username:password@host:port/database
engine = create_engine('mysql+mysqlconnector://root:root@localhost/courses_test')
#engine = create_engine('sqlite:///course_test.db')

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# ! -- create objects -- ! #

## course objects ##
sc_wb = get_first_sheet(load_workbook('short_courses.xlsx'))
adm_wb = get_first_sheet(load_workbook('admissions.xlsx'))
sc_fields, sc_courses = read_into_list(sc_wb)
adm_fields, adm_courses = read_into_list(adm_wb)

for course in sc_courses:
    object = ShortCourse(*course)
    session.add(object)

for course in adm_courses:
    object = GeneralCourse(*course)
    session.add(object)

## question objects ##
general_questions = [{"question": "What does Plan Code mean?",
                    "topic": "acronyms",
                    "answer": "Plan Code is the unique code given to a course when created on MyCampus"},
                    {"question": "What does MaRio decision mean?",
                    "topic": "acronyms",
                    "answer": "It means admissions have the decision-making capacity, not the school"},
                    {"question": "What does FT mean?",
                    "topic": "acronyms",
                    "answer": "FT means full-time!"},
                    {"question": "What does PT mean?",
                    "topic": "acronyms",
                    "answer": "FT means part-time!"},
                    {"question": "What is IELTS requirements?",
                    "topic": "requirements",
                    "answer": "IELTS requirements is the English language test score required for non-English speakers"},
                    {"question": "What is ATAS?",
                    "topic": "acronyms",
                    "answer": "The Academic Technology Approval Scheme (ATAS) requires all international students\
                    subject to existing UK immigration permissions, who are applying to study for a postgraduate qualification\
                     in certain sensitive subjects, knowledge of which could be used in programmes to develop weapons of mass destruction\
                     (WMDs) or their means of delivery, to apply for an Academic Technology Approval Scheme (ATAS) certificate before they can study in the UK."}
                    ]

short_questions = [{"question": "Is there funding available?",
                    "topic": "funding",
                    "answer": "https://www.gla.ac.uk/study/short/informationforstudents/fees/"},
                    {"question": "Can I have a refund?",
                     "topic": "cancellations",
                     "answer": "https://www.gla.ac.uk/study/short/informationforstudents/transfers/"},
                    {"question": "Can I transfer?",
                    "topic": "cancellations",
                     "answer": "https://www.gla.ac.uk/study/short/informationforstudents/transfers/"},
                     {"question": "Can I cancel?",
                     "topic": "cancellations",
                     "answer": "https://www.gla.ac.uk/study/short/informationforstudents/transfers/"},
                  ]

for question in general_questions:
    object = GeneralQuestion(question=question["question"], topic=question["topic"], answer=question["answer"])
    session.add(object)

for question in short_questions:
    object = ShortQuestion(question=question["question"], topic=question["topic"], answer=question["answer"])
    session.add(object)

# commit to the database
session.commit()
