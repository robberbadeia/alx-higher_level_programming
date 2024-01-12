#!/usr/bin/python3
"""
T03: Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument
hint : This way is used to prevent from SQL INJECTING
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
            WHERE name = %s
            ORDER BY id ASC
            '''
    cursor.execute(query, (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
