#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from os import getenv
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Place(BaseModel):
        """ A place to stay """
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place')
        amenities = relationship(
                'Amenity',secondary='place_amenity',viewonly=False)

else:
    class Place(BaseModel):
        """ A place to stay """
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def amenities(self):
        from models import storage
        return self.amenity_ids

    @amenities.setter
    def amenities(self, cls):
        from models.amenity import Amenity
        if cls.__class__ == Amenity:
            self.amenity_ids.append(cls.id)
