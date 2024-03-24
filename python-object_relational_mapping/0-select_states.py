#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb


def connect_to_database():
    """Establishes a connection to the MySQL database."""
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            charset='utf8'
        )
        return db
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)


def fetch_and_print_data(db):
    """Fetches data from the 'states' table and prints it."""
    try:
        with db.cursor() as cur:
            cur.execute("SELECT * FROM states ORDER BY id ASC")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")


def main():
    """Main function to execute the script."""
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    db = connect_to_database()
    fetch_and_print_data(db)
    db.close()


if __name__ == "__main__":
    main()
