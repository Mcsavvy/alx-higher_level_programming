#!/usr/bin/python3
"""
A script that lists all states in a database.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, name = sys.argv[1:]
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=name)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)
