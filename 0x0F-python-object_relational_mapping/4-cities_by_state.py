#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities\
        LEFT JOIN states ON cities.state_id = states.id\
        ORDER BY cities.id ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)
    cursor.close()
    conn.close()
