#!/usr/bin/python3
"""A script that lists all states in a database."""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, name, search = sys.argv[1:]
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=name
    )
    search = search.split()[0].strip("';\"")
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC;"
        .format(search))
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
