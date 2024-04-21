#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


dbORfs = getenv("HBNB_TYPE_STORAGE")
if dbORfs == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)
        else:
            if 'created_at' in kwargs and 'updated_at' in kwargs:
                kwargs['created_at'] = \
                    datetime.fromisoformat(kwargs['created_at'])
                kwargs['updated_at'] = \
                    datetime.fromisoformat(kwargs['updated_at'])
            else:
                kwargs['created_at'] = datetime.now()
                kwargs['updated_at'] = datetime.now()
            kwargs.pop('__class__', None)
            self.__dict__.update(kwargs)

            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Instance from Storage, you are going to be deleted."""
        from models import storage
        storage.delete(self)
