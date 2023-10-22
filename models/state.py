#!/usr/bin/python3
""" module of state """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from os import getenv


class State(BaseModel, Base):
    """ class of state"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """cities list """
            from models import storage
            from models.city import City

            records = storage.all(City).values()
            response = []
            for city in records:
                if city.state_id == self.id:
                    response.append(city)
            return response
