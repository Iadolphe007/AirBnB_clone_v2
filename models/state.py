#!/usr/bin/python3
""" module of state """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.city import City
import models


class State(BaseModel, Base):
    """ class of state"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """cities list """
        records = models.storage.all()
        res = []
        for city in records.values():
            if self.id == city.state_id:
                res.append(city)
        return res