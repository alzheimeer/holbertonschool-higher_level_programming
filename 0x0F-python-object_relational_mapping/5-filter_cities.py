#!/usr/bin/python3
"""Lists all cities by state passed by user"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities\
        LEFT JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id ASC"
    cursor.execute(sql, (argv[4], ))
    cities = []
    for data in cursor.fetchall():
        cities.append(data[1])
    print(', '.join(cities))
    cursor.close()
    conn.close()
