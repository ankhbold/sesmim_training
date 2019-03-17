
__author__ = 'B.Ankhbold'
from sqlalchemy import Column, String, Float, Date, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from Landuse import *
from Base import *

class Subject(Base):

    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    register = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(String)
    comment = Column(String)
