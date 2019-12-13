#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
    Your script should connect to a MySQL server running on localhost
    at port 3306
    sorted in ascending order by states.id
    should not be executed when imported """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    sql = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)
    cursor.close()
    conn.close()
