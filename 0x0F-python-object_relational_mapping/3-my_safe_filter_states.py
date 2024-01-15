#!/usr/bin/python3
""" name matches argument """
import MySQLdb
from sys import argv


def main():
    """ Main function """
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s\
            ORDER BY id ASC", (state_name,))

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
