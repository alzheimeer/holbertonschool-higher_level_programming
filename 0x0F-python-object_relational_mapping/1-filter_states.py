#!/usr/bin/python3
"""  lists all states with a name starting with N (upper N)
     from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        if data[1][0] == 'N':
            print(data)
    cursor.close()
    conn.close()
