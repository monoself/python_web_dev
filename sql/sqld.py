# SELETE statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # iterate and print the entries
    for row in c.execute("SELECT firstname, lastname from employees"):
    	print(row)

    c.execute("SELECT firstname, lastname from employees")

    # retrieve all records
    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1])
