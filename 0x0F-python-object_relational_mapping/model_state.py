#!/usr/bin/python3
"""
python file that contains the class definition
of a State and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """Class states"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
