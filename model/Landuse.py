__author__ = 'B.Ankhbold'

from sqlalchemy import Column, String, Integer
from Base import *

class Landuse(Base):

    __tablename__ = 'landuse'

    code = Column(Integer, primary_key=True)
    description = Column(String)