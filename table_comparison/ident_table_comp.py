"""
ident_table_comp.py is intended to check that two tables contain equivalent data.
This program does not check only for identical entries,
    but compensates for equivalent entries stored in different formats,
        e.g., 1.0 = 1, 20170814 = 8/14/2017, repeats in primary keys

Author: Jack Jacobs
See bottom of file for testing information
"""

import csv

master_table_path = input("Path of MASTER table (CSV format): ")
test_table_path = input("Path of TEST table (CSV format): ")

def table_format(csv_path):
    # This function returns a converted table
    # When set equal to a variable, calling a function drops the good data in that variable
    new_data = []

    with open(csv_path, newline="") as csv_file:
        # This 'with' statement reads the file to global list variable new_data
        csv_read_file = csv.reader(csv_file, delimiter=",")
    
        for row in csv_read_file:
            new_data.append(row)

    header = new_data.pop(0)

    for row in new_data:
        """ Data conversion config:
        THIS COULD BE A SEPARATE FUNCTION (or file) LATER"""
        row[2] = float(row[2])
        row[3] = float(row[3])
        row[5] = float(row[5])
        row[6] = float(row[6])
        """ These numbers are hard-coded because data conversion is unique to each master table.
        I'm using float rather than integer because it's a more versatile real number format. """

    new_data.insert(0, header)

    return(new_data)

def ident_comp(master_path, test_path):
    master_table_data, test_table_data = table_format(master_path), table_format(test_path)
    matches = []
    errors = []
    header_master, header_test = master_table_data.pop(0), test_table_data.pop(0)
    print(str(master_path))

    if len(master_table_data) == len(test_table_data):
        if len(header_master) == len(header_test):    
            for row_index in range(len(master_table_data)):
                master_row = master_table_data[row_index]
                test_row = test_table_data[row_index]
                
                for column_index in range(len(master_row)):
                    if master_row[column_index] == test_row[column_index]:
                        matches.append([header_master[column_index], (row_index + 2)])
                        # +2 because: 1) adding header back in, 2) starting from 1 instead of starting from 0.
                    else:
                        errors.append([header_master[column_index], "Row: {}".format(row_index + 2), \
                                       "Master: {}".format(master_table_data[row_index][column_index]), \
                                       "Test: {}".format(test_table_data[row_index][column_index])])
                        # Row +2 because: 1) adding header back in, 2) starting from 1 instead of starting from 0.
                
            entry_total = len(errors) + len(matches)
            error_ratio = float(len(errors) / entry_total)
            if error_ratio == 0:
                print("Tables are identical!")
            else:
                print("Tables are {:.2%} mismatched.".format(error_ratio))
                print("There are a total of {} errors:".format(len(errors)))
                for item in errors:
                    print(item," ")
        else:
            print("Table field amounts are unequal.")
            print("Master table fields: {}".format(len(header_master)))
            print("Test fields: {}".format(len(header_test)))
    else:
        print("Table row amounts are unequal")
        print("Master table rows: {}".format(len(master_table_data) + 1))
        print("Test table rows: {}".format(len(test_table_data) + 1))

ident_comp(master_table_path, test_table_path)

""" TESTING
    MASTER TABLE: test_master_table.csv

CSV documents are present in this folder to test the following cases:
- table contains extra field (column)
    test_extra_field.csv
    "Table field amounts are unequal."
    "Master table fields: 7"
    "Test fields: 8"

- tables are identical
    test_identical.csv
    "Tables are identical!"

- table contains multiple incorrect entries
    test_incorrect_entries.csv
    "Tables are 1.65% mismatched."
    "There are a total of 3 errors:"
    ['ssn_string', 'Row: 10', 'Master: 142-53-0508', 'Test: ZZ_error1_ZZ']
    ['hire_date', 'Row: 14', 'Master: 20021218', 'Test: 234432']
    ['company', 'Row: 18', 'Master: B', 'Test: ZZ_error3_ZZ']

- table's number fields contain a mix of integer & float values
    test_integer_float_switch.csv
    "Tables are identical!"

- table is missing rows
    test_missing_rows.csv
    "Table row amounts are unequal"
    "Master table rows: 27"
    "Test table rows: 25"
"""
