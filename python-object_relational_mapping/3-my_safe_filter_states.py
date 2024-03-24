#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
from MySQLdb import connect
import sys


if __name__ == "__main__":
    db = connect(host="localhost",
                 port=3306,
                 user=sys.argv[1],
                 passwd=sys.argv[2],
                 db=sys.argv[3],
                 charset='utf8'
                 )
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name = %s
                ORDER BY id ASC""", (sys.argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
