#!/usr/bin/python3
"""
Defines city
"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """Inherits from BaseModel and defines city"""
    __tablename__ = 'cities'
    name = Column(String(128))
    state_id = Column(String(60), nullable=False, ForeignKey='states.id')

