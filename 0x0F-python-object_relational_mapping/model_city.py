#!/usr/bin/python3
"""
City Model
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import State, Base


class City(Base):
    """
    The City Model.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship(State, back_populates="cities")


State.cities = relationship(City, back_populates="state")
