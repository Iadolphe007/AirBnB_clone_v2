#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              backref='states',
                              cascade='all,
                              delete-orphan')
    else:
        @property
        def cities(self):
            """cities method"""
            from models import storage
            from models.city import City

            cities = storage.all(City).values()
            list_to_return = []
            for value in cities:
                if value.state_id == self.id:
                    list_to_return.append(value)
            return list_to_return
