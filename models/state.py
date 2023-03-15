#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", back_populates='state', cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
            (It will be the FileStorage relationship between State and City)"""
            all_cities = []
            for key, value in models.storage.all(City).items():
                if self.id == value.state_id:
                    all_cities.append(value)
            return all_cities


