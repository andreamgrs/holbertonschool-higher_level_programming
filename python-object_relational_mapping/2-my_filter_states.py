#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


# To prevent not running from import just run this by calling it directly
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()  # To execute query
    state_name = sys.argv[4]
    cursor.execute("SELECT * \
    FROM states WHERE BINARY name LIKE '{}' \
    ORDER BY id ASC;".format(state_name))  # Add query
    states = cursor.fetchall()

    for state in states:
        print(state)
