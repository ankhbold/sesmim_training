# coding=utf8
__author__ = 'B.Ankhbold'

from PyQt4.QtGui import *
from qgis.core import *
from sqlalchemy.exc import DatabaseError, SQLAlchemyError
from ..view.Ui_SesmimFirstDialog import *
from ..utils.DbSession import *
from ..model.Subject import *
from ..model.Parcel import *
from ..model.Landuse import *
from ..model.SubjectParcel import *

class SesmimFirstDialog(QDialog, Ui_SesmimFirstDialog):

    def __init__(self, iface, parent=None):

        super(SesmimFirstDialog,  self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.setWindowTitle(self.tr("Sesmim first dialog"))
        self.session = None
        self.user = 'sesmim_user'
        self.password = 'sesmim_user'
        self.host = 'localhost'
        self.port = 5432
        self.database = 'tr_sesmim'

    #Холболт үүсгэх
    @pyqtSlot()
    def on_connect_button_clicked(self):

        try:
            if not DbSession().create_session(self.user, self.password, self.host, self.port, self.database):
                return
            else:
                print 'Successfully'
                self.session = DbSession().session_instance()
                self.connect_button.setEnabled(False)
        except (DatabaseError, SQLAlchemyError), e:
            print "User name or password is not correct!!!"
            self.connect_button.setEnabled(True)
            return

    #Жагсаалт харуулах
    @pyqtSlot()
    def on_refresh_button_clicked(self):

        print 'list'
        print self.session
        subjects  = self.session.query(Subject).all()
        for value in subjects:
            item_id = QTableWidgetItem(value.id)
            item_id.setData(Qt.UserRole, value.id)
            item_id.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_register = QTableWidgetItem(value.register)
            item_register.setData(Qt.UserRole, value.register)
            item_register.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            row = self.subject_twidget.rowCount()
            self.subject_twidget.setItem(row, 0, item_id)
            self.subject_twidget.setItem(row, 1, item_register)
