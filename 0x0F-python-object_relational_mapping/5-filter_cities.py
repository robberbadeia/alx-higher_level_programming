#!/usr/bin/python3
"""
T05: Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    main function
    """

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

    _list = []
    for row in rows:
        _list.append(row[0])
    print(', '.join(_list))

    cursor.close()
    db.close()
