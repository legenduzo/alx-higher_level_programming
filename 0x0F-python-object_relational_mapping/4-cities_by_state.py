#!/usr/bin/python3
""" Python SQL ORMs """
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

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON states.id = cities.state_id \
            ORDER BY cities.id")

    lines = cur.fetchall()

    for line in lines:
        print(line)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
