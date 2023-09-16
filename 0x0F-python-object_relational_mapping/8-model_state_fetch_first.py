#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    # Create a connection to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and retrieve the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Check if there is a first state and print it
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
