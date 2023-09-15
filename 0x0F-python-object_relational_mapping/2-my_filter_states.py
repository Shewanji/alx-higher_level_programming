#!/usr/bin/python3
"""
Script that retrieves and displays states from the database hbtn_0e_0_usa
where the name matches a user-supplied argument.
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

    # Get the state name from the command line arguments

    """
    Construct the SQL query using format with
    the state_name as a parameter
    """
    query = "SELECT id, name FROM states WHERE name = '{}' \
             ORDER BY id".format(argv[4])

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows and display them
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
