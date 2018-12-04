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
    return result.fetchall()

# SELECT description FROM course in short
def get_description(name):
    table = Table('short', metadata, autoload=True, autoload_with=engine)
    query = select([table.columns.description]).where(table.columns.title==name)
    result = connection.execute(query)
    return result

# issues with long text: here's some workarounds
# https://stackoverflow.com/questions/46733647/sqlalchemy-truncating-strings-on-import-from-ms-sql

print(get_fee("Biomedical Sciences"))
result = get_description("Painting in Venice in the Sixteenth Century")
for r in result:
    print(r['description'])
