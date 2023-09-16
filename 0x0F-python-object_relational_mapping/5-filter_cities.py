#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # Connect to the MySQL database
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use a prepared statement to avoid SQL injection
    query = "SELECT cities.id, cities.name FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "WHERE states.name LIKE BINARY %(state_name)s " \
            "ORDER BY cities.id"

    state_name = argv[4]

    # Execute the SQL query with a parameterized query
    cursor.execute(query, {"state_name": state_name})

    # Fetch all the rows and display them
    results = cursor.fetchall()

    # Check if there are results
    if results is not None:
        print(", ".join([row[1] for row in results]))
    # Close the cursor and database connection
    cursor.close()
    db.close()
