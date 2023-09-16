#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
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

    # Query and retrieve all State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.contains('a')).all()

    # Delete the State objects
    for state in states_with_a:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
