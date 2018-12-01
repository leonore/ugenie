# implemented with the help of:
# https://blogs.harvard.edu/rprasad/2014/06/16/reading-excel-with-python-xlrd/

import xlrd
from os.path import join, dirname, abspath
from os import pardir
from xls_helper import get_fields, get_field_type

git = abspath(join(__file__, pardir))
data_folder = join(abspath(join(git, pardir)), 'data')
filename = join(data_folder, 'admissions.xlsx')

workbook = xlrd.open_workbook(filename)
xl = workbook.sheets()[0] # holds XL sheet 1 (all the data given to us is one one sheet)
print(get_fields(xl))
print(get_field_type(xl))
