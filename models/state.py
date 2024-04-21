#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan",
                              backref="state")
    else:
        name = ""
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """returns the list of city instances with state_id equals
            to the current state.id"""
            stored_objs = models.storage.all()
            list_of_cities = []
            for obj in stored_objs:
                inst_of = obj.split('.')[0]
                if inst_of == 'City':
                    if stored_objs[obj].state_id == self.id:
                        list_of_cities.append(stored_objs[obj])
            return list_of_cities
