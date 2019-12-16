#!/usr/bin/python3
""" Start link class to table in database """

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_s = State(name="California")
    mew_c = City(name="San Francisco")
    new_s.cities.append(new_c)
    session.add(new_c)

    session.commit()
    session.close()
