#!/usr/bin/python3
import MySQLdb
import sys
"""
Lists all states from the database hbtn_0e_0_usa
Give permissions first with chmod +x .py
"""
#Take the argument
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

#To prevent not running from import just run this by calling it directly
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()  # To execute query 
    cursor.execute("SELECT * FROM states ORDER BY id ASC")  # Add query
    states = cursor.fetchall();

    for state in states:
        print(state)





    
