#!/usr/bin/python3
"""
script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
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

    Session = sessionmaker(bind=engine)
    session = Session()

    new_s = State(name="California")
    new_c = City(name="San Francisco")
    new_s.cities.append(new_c)

    session.add(new_s)
    session.add(new_c)

    session.commit()
    session.close()
