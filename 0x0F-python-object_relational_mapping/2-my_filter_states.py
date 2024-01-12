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
                         db=argv[3],
                         state=argv[4])

    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    cursor.close()
    db.close()
