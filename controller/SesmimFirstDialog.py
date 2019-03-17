# coding=utf8
__author__ = 'B.Ankhbold'

from PyQt4.QtGui import *
from qgis.core import *
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
        self.session = DbSession.session_instance()

    #Жагсаалт харуулах
    @pyqtSlot()
    def on_refresh_button_clicked(self):

        print 'list'
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
