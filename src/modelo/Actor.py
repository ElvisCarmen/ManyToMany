from sqlite3 import Date

import sqlalchemy

from src.modelo import base

from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import relationship
from src.modelo.base import Base
from src.modelo.Movie import Movie


class Actor(base.Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday