#!/usr/bin/python3
""" lists all states with a name starting with N """
import MySQLdb
from sys import argv


def main():
    """ Main function """
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    cur = db.cursor()

    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
            )

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
