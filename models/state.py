#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship

storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='states')
    else:
        name = ""
        @property
        def cities(self):
            """cities method"""
            from models import storage
            from models.city import City
            citiesList = []
            cities = storage.all(City).values()
            list_to_return = []
            for value in cities:
                if value.state_id == self.id:
                    list_to_return.append(value)
            return citiesList
