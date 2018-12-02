# implemented with the help of:
# https://blogs.harvard.edu/rprasad/2014/06/16/reading-excel-with-python-xlrd/
# https://radiusofcircle.blogspot.com/2016/03/the-xlrd-python-module-for-reading-data.html

import xlrd
import datetime
from os.path import join, dirname, abspath
from os import pardir
from xlrd.sheet import ctype_text

def load_workbook(filename):
    git = abspath(join(__file__, pardir))
    data_folder = join(abspath(join(git, pardir)), 'data')
    fn = join(data_folder, filename)
    return xlrd.open_workbook(fn)

def get_first_sheet(wb):
    return wb.sheets()[0]

def get_field_type(cell):
    # assumes the data is well-formatted throughout
    return ctype_text.get(cell.ctype, 'unknown')

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
            current = []
            for cell in row:
                val = parse_value(cell)
                current.append(val)
            content.append(current)
    return fields, content
