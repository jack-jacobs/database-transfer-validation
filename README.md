# database-transfer-validation

Dad wants me to validate a new database of client employees.
    Specifically, I should confirm that the contents of the new database are entirely consistent with the contents of the old database(s).
He is migrating databases. ("30 databases" ???)
Vendors own storage & database structure. MedHQ owns data.

Things I need to complete project:
- schemas for databases in DOCX (or any DOC or PDF) format
- all data at issue for comparison in CSV (or any Excel) format

1) be able to validate data between tables
    a) create dummy tables
        i) with and without errors
    b) remember to write errors to a txt file
        i) quantify item errors and report errors as proportion of total entries
    c) be able to validate across different data type formatting
        i) different datetime stuff
        ii) integer/float
        iii) checking for repeats in primary keys
2) receive data from MedHQ databases
    a) raw CSV export with schemas
    b) consider how database structure affects table alignment
        i) There will theoretically be many fewer tables in the single database
        ii) might require some pre-cleaning in SQL on my end
3) validate data
    a) Write errors to file
