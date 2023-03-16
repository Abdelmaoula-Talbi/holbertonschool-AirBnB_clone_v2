#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

place_amenity = Table("place_amenity", Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity, back_populates="place_amenities", viewonly=False)
    else:
        @property
        def reviews(self):
            """returns the list of Review instances"""
            all_reviews = []
            for key, value in models.storage.all(Review).items():
                if self.id == value.place_id:
                    all_reviews.append(value)
            return all_reviews

        @property
        def amenities(self):
            """returns the list of Amenity instances"""
            all_amenities = []
            for key, value in models.storage.all(Amenity).items():
                if value.id in self.amenity_ids:
                    all_amenities.append(value)
            return all_amenities
        
        @amenities.setter
        def amenities(self, amenit):
            if type(amenit) == Amenity:
                self.amenity_ids.append(amenit.id)
