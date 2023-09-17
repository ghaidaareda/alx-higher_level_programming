#!/usr/bin/python3
"""
python file that contains the class definition
of a city and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy import ForeignKey

Base = declarative_base()


class City(Base):
    """Class states"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'),
                      nullable=False)
