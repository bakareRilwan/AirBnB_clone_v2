#!/usr/bin/python3
"""
Class that defines a state
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """class to create a state"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    @property
    def cities(self):
        """Getter attribute in case of file storage"""
        return [city for city in models.storage.all(City).values()
                if city.state_id == self.id]
