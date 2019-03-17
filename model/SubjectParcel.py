__author__ = 'B.Ankhbold'

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Base import *


class SubjectParcel(Base):
    __tablename__ = 'subject_parcel'
    person_id = Column(Integer, ForeignKey('subject.id'), primary_key=True)
    person_id_ref = relationship("Subject")

    parcel_id = Column(Integer, ForeignKey('parcel.parcel_id'), primary_key=True)
    parcel_id_ref = relationship("Parcel")