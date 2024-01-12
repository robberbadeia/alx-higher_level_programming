#!/usr/bin/python3
"""
Defines class State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(128))
