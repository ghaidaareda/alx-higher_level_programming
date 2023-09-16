#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],)
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
