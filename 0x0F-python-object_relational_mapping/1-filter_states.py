#!/usr/bin/python3
""" Write a script that lists all states
with a name starting with N (upper N) from...
    ...the database hbtn_0e_0_usa """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb


    server = MySQLdb.connect(host="localhost",  port=3306,
                           user=sys.argv[1], password=sys.argv[2],
                           database=sys.argv[3])

    c = server.cursor()
    stateName = sys.argv[4]
    c.execute(
        "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
            stateName))
    rows = c.fetchall()
    for row in rows:
        if row[1] == stateName:
            print(row)
    c.close()
    server.close()
