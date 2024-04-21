#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
    # __tablename__ = 'amenities'
    # name = Column(String(128), nullable=False)

    # if getenv('HBNB_TYPE_STORAGE') != 'db':
    #     name = ""
