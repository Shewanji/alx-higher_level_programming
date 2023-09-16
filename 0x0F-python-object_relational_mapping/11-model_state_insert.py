#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    # Create a new State object for "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new State object to the session and commit it to the database
    session.add(new_state)
    session.commit()

    # Print the new state's ID
    print(new_state.id)

    # Close the session
    session.close()
