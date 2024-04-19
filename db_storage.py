#!/usr/bin/python3
"""Defines the DBStorage engine."""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages storage of hbnb
    models in a MySQL database """
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and session attributes"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}"
            .format(getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
            )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session all
        objects depending on the class name
        """
        objects = {}
        classes = [State, City, User, Place, Review, Amenity]
        if cls:
            classes = [cls]
            for clss in classes:
                for obj in self.__session.query(clss).all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
            return objects

    def new(self, obj):
        """
        Add current Object
        """
        self.__session.add(obj)
        

    def save(self, obj):
        """
        commit current changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from the current
        database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database
        and the current database session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
                )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close the session"""
        self.__session.close()
