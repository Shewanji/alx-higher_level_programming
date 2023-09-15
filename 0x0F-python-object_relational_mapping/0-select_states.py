#!/usr/bin/python3
"""
 script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Retrieve and display a list of states from a MySQL database.
    """

    # Connect to the MySQL database
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select states and order them by id
    cursor.execute("SELECT id, name FROM states ORDER BY id")

    # Fetch all the rows and display them
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
