#!/usr/bin/python3
"""
Takse in the name of a state as an argument and lists all cities of the states
using the database `hbtn_0e_4_usa`
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
    cur.execute("""SELECT cities.name FROM cities where state_id =
                (SELECT id FROM states WHERE name = '{}')
                """.format(sys.argv[4]))
    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))
    cur.close()
    db.close()
