# https://pythonspot.com/orm-with-sqlalchemy/

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import GeneralCourse, ShortCourse

from xls_helper import *

# MySQL-connector-python
# dialect+driver://username:password@host:port/database
engine = create_engine('mysql+mysqlconnector://root:root@localhost/courses_test')
#engine = create_engine('sqlite:///course_test.db')

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# ! -- create objects -- ! #
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

# commit to the database
session.commit()
