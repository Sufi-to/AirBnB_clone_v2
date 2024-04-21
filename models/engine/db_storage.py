#!/usr/bin/python3
""" Contains a database engine class that uses sqlalchemy"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine


class DBStorage:
    """ Builds tables using if a db storage is selected """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the class DBStorage"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all the objects depending of the given cls argument"""
        all_objs = {}
        all_instances = [User, State, City, Amenity, Place, Review]
        if cls:
            query_inst = self.__session.query(cls)
            for inst in query_inst.all():
                inst_key = f"{type(inst).__name__}.{inst.id}"
                all_objs[inst_key] = inst
        else:
            for inst in all_instances:
                query = self.__session.query(inst)
                for inst in query:
                    key = f"{type(inst).__name__}.{inst.id}"
                    all_objs[key] = inst
        return all_objs

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """saves the object created to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from the current database session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh)
        self.__session = Session()
