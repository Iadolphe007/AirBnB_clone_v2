#!/usr/bin/python3
"""Module contains database engine"""

from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User
from models.state import State
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from os import getenv
from models.base_model import BaseModel

class DBStorage():
    """new engine"""
    __engine = None
    __session = None

    def __init__(self):
        """public instance"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, db), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(sel, cls=None):
        """class query"""
        class_dict = {'User': User, 'State': State, 'City': City,
                'Amenity': Amenity, 'Place': Place, 'Review': Review}
        obj_dict = {}
        
        try:
            for key, value in clas_dict.items():
                if cls is None or key == cls:
                    query_result = self.__session.query(value).all()
                    for obj in query_result:
                        obj_dict[obj.__class__.__name__+'.' + obj.id] = obj
         except Exception:
             pass
         return obj_dict

     def new(self, obj):
         """add obj to database"""
         self.__session.add(obj)
         self.save()
    def save(self):
        """commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete current database"""
        if obj:
            self.__name.delete(obj)
        self.save()
    
    def reload(self):
        """ create table and database """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """close session"""
        self.__session.remove()





        
