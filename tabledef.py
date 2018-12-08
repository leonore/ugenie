# sources:
# https://pythonspot.com/orm-with-sqlalchemy/

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, Date, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import *
from sqlalchemy_utils import database_exists, create_database, drop_database
from datetime import datetime

# 1 - create engine to initialise the database
Base = declarative_base()

# MySQL-connector-python
# dialect+driver://username:password@host:port/database
engine = create_engine('mysql+mysqlconnector://root:root@localhost/courses_test')
#engine = create_engine('sqlite:///course_test.db')

if database_exists(engine.url):
    drop_database(engine.url)
create_database(engine.url)

# 2 - table definitions
class GeneralCourse(Base):
    __tablename__ = 'general'

    code = Column(String(40), primary_key=True) # TODO there are duplicates in the admission data (difference from one admission year to another)
    course_name = Column(String(250), nullable=False)
    qualification = Column(String(50), nullable=False)
    mario = Column(Boolean, nullable=False)
    full_time = Column(Boolean, nullable=False)
    part_time = Column(Boolean, nullable=False)
    requirements = Column(Text)
    ielts = Column(Text)
    info = Column(Text)
    jacs = Column(String(10))
    atas = Column(Boolean)
    subject = Column(String(50))
    degree = Column(Boolean, nullable=False) # True is UGT, False is PGT
    status = Column(String(10), nullable=False) # if the program is RUNNING or year of run TODO make enum for This
    jan_start = Column(Boolean, nullable=False) # True if january start, else False
    admit_term = Column(Integer, nullable=False)
    home_fee = Column(Integer)
    intl_fee = Column(Integer)

    def __init__(self, course_name, qualification, code, rio, mario, full_time, part_time,
                    requirements, ielts, info, jacs, atas, jan_start, subject, degree, status,
                    admit_term, home_fee, intl_fee):
        self.code = code+"-"+str(admit_term)
        self.course_name = course_name
        self.qualification = qualification
        self.mario = bool(mario)
        self.full_time = bool(full_time)
        self.part_time = bool(part_time)
        self.requirements = requirements
        self.ielts = ielts
        self.info = info
        self.jacs = jacs
        self.atas = bool(atas)
        self.subject = subject
        self.degree = bool(degree)
        self.status = status
        self.jan_start = bool(jan_start)
        self.admit_term = admit_term
        self.home_fee = home_fee
        self.intl_fee = intl_fee


# TODO consider making this
#class Requirements(Base):
#    __tablename__ = 'requirements'


class ShortCourse(Base):
    __tablename__ = 'short'

    code = Column(Integer, primary_key=True)
    subject = Column(String(50), nullable=False)
    title = Column(String(250), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    # QUESTION are all short courses in one day?
    start_time = Column(Integer, nullable=False)
    end_time = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    tutor = Column(String(100), nullable=False)
    location = Column(Text, nullable=False)
    link = Column(String(100))
    description = Column(Text, nullable=False)
    credits = Column(Integer)
    language_links = Column(Text)

    def __init__(self, subject, title, code, start_date, end_date,
                    start_time, end_time, cost, duration, tutor, location,
                    link, description, credits, language_links):
        self.code = code
        self.subject = subject
        self.title = title
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.end_date = datetime.strptime(end_date, "%d/%m/%Y")
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.cost = cost
        self.tutor = tutor
        self.location = location
        self.link = link
        self.description = description
        self.credits = credits
        self.language_links = language_links

# 3 - create tables
Base.metadata.create_all(engine)
