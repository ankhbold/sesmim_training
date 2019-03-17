# -*- coding: utf-8
__author__ = 'B.Ankhbold'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import DatabaseError, SQLAlchemyError
from ..model.Singleton import Singleton

class DbSession(QObject):

    __metaclass__ = Singleton

    def __init__(self, parent=None):

        super(QObject, self).__init__(parent)
        self.parent = parent
        self.session = None
        self.engine = None
        self.password = None
        self.set_search_path = "SET search_path to sesmim, public"

    def session_instance(self):

        return self.session

    def create_session(self, user, password, host, port, database):

        if self.session is not None:
            self.session.close()
        try:
            self.engine = create_engine("postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database))
            self.password = password
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            self.session.autocommit = False
            self.session.execute(self.set_search_path)
            self.session.commit()
            return True
        except SQLAlchemyError, e:
            self.session = None
            self.engine = None
            self.password = None
            raise e