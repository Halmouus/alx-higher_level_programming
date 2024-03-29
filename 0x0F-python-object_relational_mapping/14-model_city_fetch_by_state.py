#!/usr/bin/python3
"""script  that prints all City objects from the database"""

import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True,)

    Session = sessionmaker(bind=engine)
    MySession = Session()

    for city, state in MySession.query(City, State).\
            filter(City.state_id == State.id).\
            order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")

    MySession.close()
