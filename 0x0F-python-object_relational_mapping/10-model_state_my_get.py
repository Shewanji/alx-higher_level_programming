#!/usr/bin/python3
"""
Prints the State object with the specified name from the database hbtn_0e_6_usa
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

    # Extract the state name to search from the command-line arguments
    state_name = sys.argv[4]

    # Query and retrieve the State object with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    # Check if a state was found and print its ID or "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
