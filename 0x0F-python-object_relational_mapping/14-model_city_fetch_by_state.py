#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':

    # Create a connection to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and retrieve all City objects, sorted by cities.id
    cities = session.query(State.name, City.id, City.name)\
        .join(City, State.id == City.state_id)\
        .order_by(City.id)\
        .all()

    # Print the City objects
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    # Close the session
    session.close()
