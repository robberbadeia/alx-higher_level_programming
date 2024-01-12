#!/usr/bin/python3
"""
T05: Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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
            SELECT
                cities.name
            FROM
                states
            INNER JOIN
                cities
            ON
                states.id = cities.state_id
            WHERE
                states.name = %s
            GROUP BY
                cities.name
            ORDER BY
                cities.name DESC
            '''
    cursor.execute(query, (argv[4], ))
    rows = cursor.fetchall()

    for row in rows:
        print(row[0], )

    cursor.close()
    db.close()
