#!/usr/bin/python3
"""A script that lists all cities in a database."""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, name = sys.argv[1:]
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=name
    )
    cur = db.cursor()
    cur.execute((
        "SELECT cities.id, cities.name, states.name"
        "FROM cities INNER JOIN states ON cities.state_id=states.id"
        "ORDER BY cities.id ASC;"
    ))
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
