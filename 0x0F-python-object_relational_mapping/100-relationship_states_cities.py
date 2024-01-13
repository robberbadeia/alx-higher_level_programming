#!/usr/bin/python3

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

    _state = State(id=1, name="California")
    _city = City(id=1, name="San Francisco")
    _state.cities.append(_city)

    session.add(_state)
    session.add(_city)

    session.commit()
    session.close()
