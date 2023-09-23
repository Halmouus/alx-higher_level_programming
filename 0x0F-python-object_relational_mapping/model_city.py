#!/usr/bin/python3
"""class definition of a City and an instance
Base = declarative_base()"""

import sqlalchemy
from model_state import Base


class City(Base):
    """City class"""

    __tablename__ = 'cities'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    state_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey('states.id'))
