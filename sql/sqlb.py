# INSERT Command

import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
    cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

    # commit the changes: INSERT, UPDATE, DELETE
    conn.commit()
except sqlite3.OperationalError:
    print("Try again...")

conn.close()