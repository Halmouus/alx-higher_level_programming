#!/usr/bin/python3
"""script that lists all State objects from the database"""

import sys
from sqlalchemy import create_engine, select
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True,)

    with engine.connect() as connection:
        result = connection.execute(select(State).order_by(State.id.asc()))
        for el in result:
            print(f"{el.id}: {el.name}")

    engine.dispose()
