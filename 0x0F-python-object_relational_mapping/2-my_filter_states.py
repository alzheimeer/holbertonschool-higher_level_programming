#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    sql = "SELECT * FROM states WHERE name = '{}'\
    ORDER BY states.id ASC".format(argv[4])
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        if data[1] == argv[4]:
            print(data)
    cursor.close()
    conn.close()
