#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa
    where name matches the argumentsafe from MySQL injections! """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    sql = "SELECT * FROM states WHERE name = %s\
    ORDER BY states.id ASC"
    cursor.execute(sql, (argv[4], ))
    result = cursor.fetchall()
    for data in result:
        print(data)
    cursor.close()
    conn.close()
