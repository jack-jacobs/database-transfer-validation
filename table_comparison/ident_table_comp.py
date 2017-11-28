"""
ident_table_comp.py is intended to check that two tables contain equivalent data.
This program does not check only for identical entries,
    but compensates for equivalent entries stored in different formats,
        e.g., 1.0 = 1, 20170814 = 8/14/2017, repeats in primary keys
Author: Jack Jacobs
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
            THIS COULD BE A SEPARATE FUNCTION (or file) LATER
            These numbers are hard-coded because data conversion is unique to each master table."""
        row[2] = int(row[2])
        row[3] = int(row[3])
        row[5] = int(row[5])
        row[6] = int(row[6])

    new_data.insert(0, header)

    return(new_data)

def ident_comp(master_data_path, file_b):
    master_table_data, test_table_data = table_format(master_table_path), table_format(test_table_path)
    matches = []
    errors = []
    header_master, header_test = master_table_data.pop(0), test_table_data.pop(0)

    if len(master_table_data) == len(test_table_data):
        if len(header_master) == len(header_test):    
            for row_index in range(len(master_table_data)):
                master_row = master_table_data[row_index]
                test_row = master_table_data[row_index]
                
                for column_index in range(len(master_row)):
                    if master_row[column_index] == test_row[column_index]:
                        matches.append([header_master[column_index], (row_index + 2)])
                        # +2 because: 1) adding header back in, 2) starting from 1 instead of starting from 0.
                    else:
                        errors.append([header_master[column_index], "Row: {}".format(row_index + 2), \
                                       "Master: {}".format(master_table_data[row_index][column_index]), \
                                       "Test: {}".format(test_table_data[row_index][colulmn_index]))
                        # Row +2 because: 1) adding header back in, 2) starting from 1 instead of starting from 0.
                
            error_ratio = len(errors) / (len(errors) + len(matches))
            if error_ratio == 0:
                print("Tables are identical!")
            else:
                print("Tables are {:.3%} mismatched.".format(error_ratio * 100))
                print("There are a total of {} errors:".format(len(errors)))
                for item in errors:
                    print(item," ")
        else:
            print("Table field amounts are unequal.")
            print("Master table fields: {}".format(len(master_table_data[0])))
            print("Test fields: {}".format(len(test_table_data[0])))
    else:
        print("Table row amounts are unequal")
        print("Master table rows: {}".format(len(master_table_data)))
        print("Test table rows: {}".format(len(test_table_data)))

ident_comp(master_table_path, test_table_path)
