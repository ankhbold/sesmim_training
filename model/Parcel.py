
__author__ = 'B.Ankhbold'
from sqlalchemy import Column, String, Float, Date, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from Landuse import *
from Base import *

class Parcel(Base):

    __tablename__ = 'ca_parcel'

    parcel_id = Column(String, primary_key=True)
    area_m2 = Column(Float)
    address = Column(String)
    geometry = Column(Geometry('POLYGON', 4326))

    # foreign keys:
    landuse = Column(Integer, ForeignKey('landuse.code'))
    landuse_ref = relationship("Landuse")