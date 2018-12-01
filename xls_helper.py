import xlrd
from xlrd.sheet import ctype_text

def get_fields(sheet):
    # this function assumes the first row of an xls contains the fields
    # RETURNS a list of strings
    field_row = sheet.row(0)
    fields = []
    for field in field_row:
        if field is not None:
            fields.append(field.value)
    return fields

def get_field_type(sheet):
    # assumes the data is well-formatted throughout
    test_row = sheet.row(1)
    types = []
    for value in test_row:
        type = ctype_text.get(value.ctype, 'unknown type')
        types.append(type)
    return types
