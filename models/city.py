#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModeli, Base):
        """ The city class, contains state ID and name """
        __tablename__ = 'cities'
        name = Column(String(128), nullble=False)
        state_id = Column(String(60), nullable=False, ForeignKey=('states.id'))
        places = relationship('Place', backref='cities')
else:
    class City(BaseModel):
        """base model class"""
