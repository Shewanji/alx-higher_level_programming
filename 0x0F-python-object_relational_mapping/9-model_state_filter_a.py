#!/usr/bin/python3
"""
Lists all State objects containing the letter 'a'
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Create a connection to the MySQL database
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]))

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query and retrieve all State objects containing
# the letter 'a', sorted by states.id
states_with_a = session.query(State)\
    .filter(State.name.like('%a%'))\
    .order_by(State.id)\
    .all()

# Print the State objects
for state in states_with_a:
    print("{}: {}".format(state.id, state.name))

# Close the session
session.close()
