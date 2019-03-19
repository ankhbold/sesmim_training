__author__ = 'Anna'

from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from Base import *


class Au2(Base):

    __tablename__ = 'au2'

    code = Column(String, primary_key=True)
    name = Column(String)
    area_m2 = Column(Float)
    geometry = Column(Geometry('POLYGON', 4326))

