#!/usr/bin/python3
"""
Lists all cities from database hbtn_0e_4_usa
"""
from MySQLdb import connect
import sys


if __name__ == "__main__":
    db = connect(host="localhost",
                 port=3306,
                 user=sys.argv[1],
                 passwd=sys.argv[2],
                 db=sys.argv[3],
                 charset="utf8"
                 )
    cur = db.cursor()
    cur.execute("""SELECT cities.id as id, cities.name, states.name FROM cities
                INNER JOIN states ON state_id = states.id ORDER BY id""")
    [print(row) for row in cur.fetchall()]
    cur.close()
    db.close()
