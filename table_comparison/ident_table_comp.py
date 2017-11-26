"""
ident_table_comp.py is intended to check that two tables contain equivalent data.
This program does not check only for identical entries,
    but compensates for equivalent entries stored in different formats,
        e.g., 1.0 = 1, 20170814 = 8/14/2017, repeats in primary keys

Author: Jack Jacobs
"""

import csv

a_path = input("Path of MASTER file A: ")
b_path = input("Path of TEST file B: ")

def table_format(csv_path):
    # This function returns a converted table
    # When set equal to a variable, calling a function drops the good data in that variable
    new_data = []

    with open(csv_path, newline="") as samp_file:
        # This 'with' statement reads the file to global list variable new_data
        samp_read = csv.reader(samp_file, delimiter=",")
    
        for row in samp_read:
            new_data.append(row)

    header = new_data.pop(0)

    for row in new_data:
        """ Data conversion config
        THIS COULD BE A SEPARATE FUNCTION LATER """
        row[2] = int(row[2])
        row[3] = int(row[3])
        row[5] = int(row[5])
        row[6] = int(row[6])

    new_data.insert(0, header)

    return(new_data)

def ident_comp(file_a, file_b):
    data_a, data_b = table_format(file_a), table_format(file_b)
    match = []
    error = []

    if len(data_a) == len(data_b) and len(data_a[0]):
        if len(data_a[0]) == len(data_b[0]):    
            for row in range(len(data_a)):
                a_row = data_a[row]
                b_row = data_b[row]
                for item in range(len(a_row)):
                    if a_row[item] == b_row[item]:
                        match.append([data_a[0][item], (row + 1)])
                    else:
                        error.append([data_a[0][item], (row + 1), data_a[row][item], data_b[row][item]])
                
            error_ratio = len(error) / (len(error) + len(match))
            if error_ratio == 0:
                print("Tables are identical!")
            else:
                print("Tables are %.2f%% mismatched" % (error_ratio * 100))
                for item in error:
                    print(item," ")
        else:
            print("Table field amounts are unequal.")
            print("Table A fields: %s" % len(data_a[0]))
            print("Table B fields: %s" % len(data_b[0]))
    else:
        print("Table row amounts are unequal")
        print("Table A rows: %s" % len(data_a))
        print("Table B rows: %s" % len(data_b))

ident_comp(a_path, b_path)

"""
data_a & data_b are lists of lists which each equal one CSV
the ident_comp(...) function should compare each item of the CSV to check for equal tables
I'm thinking that it'll include nested for statements
"""
