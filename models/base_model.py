#!/usr/bin/python3
"""A class named (BaseModel) that defines all common
attributes/methods for other classes:"""


import uuid
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()
class BaseModel:
    """A Base class"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """initialization of object"""
        if kwargs and kwargs is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                elif (key == 'created_at'):
                    self.created_at = datetime.\
                            strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                elif (key == 'updated_at'):
                    self.updated_at = datetime.\
                            strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Prints the str repr of an object"""
        ret_value = "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)
        return (ret_value)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
__dict__ of the instance:"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        key = dict_copy.keys()
        if "_sa_instance_state" in key:
            del dict_copy["_sa_instance_state"]
        return (dict_copy)

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)
