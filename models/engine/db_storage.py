#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import  City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import Session, sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """initiate the dbstorage"""
        self.__engine = create_engine('mysql'+'mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns the list of objects of one type of class"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    new_dict[key] = value
            return new_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from __objects if it is inside, otherwise do nothing"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        create the current database session
        (self.__session) from the engine (self.__engine)"""
        Base.metadata.create_all(self.__engine)
        session_s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_s)
    

    def close(self):
        """$"""
        #self.reload()
