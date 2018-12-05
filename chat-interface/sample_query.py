from sqlalchemy import *

# tutorial: https://www.pythonsheets.com/notes/python-sqlalchemy.html

engine = create_engine('mysql+mysqlconnector://root:root@localhost/courses_test')
connection = engine.connect()
metadata = MetaData()

short_courses = Table('short', metadata, autoload=True, autoload_with=engine)

# SELECT * FROM short
query = select([short_courses])


# SELECT home_fee FROM course in general
def get_fee(name):
    table = Table('general', metadata, autoload=True, autoload_with=engine)
    query = select([table.columns.intl_fee]).where(table.columns.course_name==name)
    result = connection.execute(query)
    r = result.fetchall()
    return "The fees for " + name + " is " + str(r)

# SELECT description FROM course in short
def get_description(name):
    table = Table('short', metadata, autoload=True, autoload_with=engine)
    query = select([table.columns.description]).where(table.columns.title==name)
    result = connection.execute(query)
    desc = []
    for r in result:
        desc.append(r['description'])
    return desc

# issues with long text: here's some workarounds
# https://stackoverflow.com/questions/46733647/sqlalchemy-truncating-strings-on-import-from-ms-sql
