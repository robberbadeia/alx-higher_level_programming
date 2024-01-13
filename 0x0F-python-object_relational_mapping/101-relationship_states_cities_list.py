#!/usr/bin/python3
"""
script that lists all State objects,
and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    main function
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all().order_by(State.id, City.id)
    for state in session.query(State).order_by(State.id):
        print(state.id, state.name, sep=": ")
        for cities in state.cities:
            print("\t{}: {}".format(cities.id, cities.name))
    session.close()
