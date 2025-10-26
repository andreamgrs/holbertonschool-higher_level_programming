#!/usr/bin/python3
"""
Lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


# To prevent not running from import just run this by calling it directly
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()  # To execute query
    cursor.execute("SELECT * \
    FROM states WHERE name LIKE 'N%' \
    AND name NOT LIKE 'n%'\
    ORDER BY id ASC;")  # Add query
    states = cursor.fetchall()

    for state in states:
        print(state)
