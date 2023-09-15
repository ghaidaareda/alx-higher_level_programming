#!/usr/bin/python3
"""
script that displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = """SELECT * FROM states WHERE name = %s ORDER BY states.id ASC """
    cursor.execute(query,(sys.argv[4]))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
