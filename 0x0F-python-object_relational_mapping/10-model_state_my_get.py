#!/usr/bin/python3
"""script that prints the State object with the name
passed as argument from the database """

import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True,)

    Session = sessionmaker(bind=engine)
    MySession = Session()

    result = MySession.query(State).filter_by(name=sys.argv[4]).first()

    if result:
        print(result.id)
    else:
        print("Not found")

    MySession.close()
