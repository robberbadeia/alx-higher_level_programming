#!/usr/bin/python3
"""
T02: Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    query = '''
            SELECT *
            FROM states
            WHERE name
            LIKE '{:s}'
            ORDER BY id ASC
            '''.format(argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
