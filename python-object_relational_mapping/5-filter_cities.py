#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()  # To execute query
    cursor.execute("SELECT cities.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name LIKE %s \
    ORDER BY cities.id ASC;", (sys.argv[4],))  # Add query
    # This return tuples like [('Dallas,'), ('Houston',), etc..]
    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]
    print(", ".join(city_names))
