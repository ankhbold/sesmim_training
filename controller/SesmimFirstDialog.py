# coding=utf8
__author__ = 'B.Ankhbold'

from PyQt4.QtGui import *
from qgis.core import *
from ..view.Ui_SesmimFirstDialog import *
from ..utils.DbSession import *

class SesmimFirstDialog(QDialog, Ui_SesmimFirstDialog):

    def __init__(self, iface, parent=None):

        super(SesmimFirstDialog,  self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.setWindowTitle(self.tr("Sesmim first dialog"))
        self.session = DbSession.session_instance()
