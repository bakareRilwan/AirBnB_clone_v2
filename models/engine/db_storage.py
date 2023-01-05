#!/usr/bin/python3
"""A database storage engine"""


import os
from sqlalchemy.orm import session_maker
from sqlalchemy import create_engine
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

hbnb_dev = os.getenv('HBNB_MYSQL_USER')
hbnb_dev_passwd = os.getenv('HBNB_MYSQL_PWD')
hbnb_dev_host = os.getenv('HBNB_MYSQL_HOST')
hbnb_dev_db = os.getenv('HBNB_MYSQL_DB')
hbnb_env = os.getenv('HBNB_ENV')


class DBStorage:
    """A database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """a method that creates engine"""
        self.engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(hbnb_dev, hbnb_dev_host, hbnb_dev_passwd, hbnb_dev_db), pool_pre_ping=True)
        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query that finds objects and print"""
        Session = sessionmaker(bind=engine)
        self.__session = Session()
        if cls:
            result = self.__session.query(cls).all()
            res = {f"{cls}.{val.id}": val for val in result}
        else:
            result = self.__session.query(User, State, City, Amenity, Place, Review).all()
            res = {f"{cls}.{val.id}": val for val in result}

        return (res)

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute """
        self.__session.close()
