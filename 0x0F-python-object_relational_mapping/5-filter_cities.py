#!/usr/bin/python3
"""A script that lists all cities in a database."""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, name, search = sys.argv[1:]
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=name
    )
    search = search.split()[0].strip("\"';")
    cur = db.cursor()
    count = cur.execute((
        "SELECT cities.name FROM cities"
        "INNER JOIN states ON cities.state_id=states.id"
        "WHERE states.name='{search}'"
        "ORDER BY cities.id ASC;"
    ))
    for state in cur.fetchall():
        count -= 1
        if count == 0:
            print(state[0], end='')
        else:
            print(state[0], end=', ')
    print()
    cur.close()
    db.close()
