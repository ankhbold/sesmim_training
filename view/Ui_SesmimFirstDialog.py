# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SesmimFirstDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SesmimFirstDialog(object):
    def setupUi(self, SesmimFirstDialog):
        SesmimFirstDialog.setObjectName(_fromUtf8("SesmimFirstDialog"))
        SesmimFirstDialog.resize(600, 600)
        SesmimFirstDialog.setMinimumSize(QtCore.QSize(600, 600))
        SesmimFirstDialog.setMaximumSize(QtCore.QSize(600, 600))
        SesmimFirstDialog.setBaseSize(QtCore.QSize(600, 600))
        self.groupBox = QtGui.QGroupBox(SesmimFirstDialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 571, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.save_button = QtGui.QPushButton(self.groupBox)
        self.save_button.setGeometry(QtCore.QRect(400, 120, 75, 23))
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.register_edit = QtGui.QLineEdit(self.groupBox)
        self.register_edit.setGeometry(QtCore.QRect(10, 40, 171, 20))
        self.register_edit.setObjectName(_fromUtf8("register_edit"))
        self.firstname_edit = QtGui.QLineEdit(self.groupBox)
        self.firstname_edit.setGeometry(QtCore.QRect(210, 40, 171, 20))
        self.firstname_edit.setObjectName(_fromUtf8("firstname_edit"))
        self.lastname_edit = QtGui.QLineEdit(self.groupBox)
        self.lastname_edit.setGeometry(QtCore.QRect(400, 40, 150, 20))
        self.lastname_edit.setObjectName(_fromUtf8("lastname_edit"))
        self.address_edit = QtGui.QTextEdit(self.groupBox)
        self.address_edit.setGeometry(QtCore.QRect(10, 90, 171, 51))
        self.address_edit.setObjectName(_fromUtf8("address_edit"))
        self.comment_edit = QtGui.QTextEdit(self.groupBox)
        self.comment_edit.setGeometry(QtCore.QRect(210, 90, 171, 51))
        self.comment_edit.setObjectName(_fromUtf8("comment_edit"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 97, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 97, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(400, 20, 97, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 97, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(210, 70, 97, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.refresh_button = QtGui.QPushButton(self.groupBox)
        self.refresh_button.setGeometry(QtCore.QRect(490, 120, 75, 23))
        self.refresh_button.setObjectName(_fromUtf8("refresh_button"))
        self.subject_twidget = QtGui.QTableWidget(SesmimFirstDialog)
        self.subject_twidget.setGeometry(QtCore.QRect(20, 210, 571, 351))
        self.subject_twidget.setObjectName(_fromUtf8("subject_twidget"))
        self.subject_twidget.setColumnCount(6)
        self.subject_twidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.subject_twidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.subject_twidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.subject_twidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.subject_twidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.subject_twidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.subject_twidget.setHorizontalHeaderItem(5, item)
        self.close_button = QtGui.QPushButton(SesmimFirstDialog)
        self.close_button.setGeometry(QtCore.QRect(520, 570, 75, 23))
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.connect_button = QtGui.QPushButton(SesmimFirstDialog)
        self.connect_button.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.connect_button.setObjectName(_fromUtf8("connect_button"))

        self.retranslateUi(SesmimFirstDialog)
        QtCore.QMetaObject.connectSlotsByName(SesmimFirstDialog)

    def retranslateUi(self, SesmimFirstDialog):
        SesmimFirstDialog.setWindowTitle(_translate("SesmimFirstDialog", "Dialog", None))
        self.groupBox.setTitle(_translate("SesmimFirstDialog", "Person register", None))
        self.save_button.setText(_translate("SesmimFirstDialog", "Save", None))
        self.label.setText(_translate("SesmimFirstDialog", "Register", None))
        self.label_2.setText(_translate("SesmimFirstDialog", "Firstname", None))
        self.label_3.setText(_translate("SesmimFirstDialog", "Lastname", None))
        self.label_4.setText(_translate("SesmimFirstDialog", "Address", None))
        self.label_5.setText(_translate("SesmimFirstDialog", "Comment", None))
        self.refresh_button.setText(_translate("SesmimFirstDialog", "refresh", None))
        item = self.subject_twidget.horizontalHeaderItem(0)
        item.setText(_translate("SesmimFirstDialog", "ID", None))
        item = self.subject_twidget.horizontalHeaderItem(1)
        item.setText(_translate("SesmimFirstDialog", "Register", None))
        item = self.subject_twidget.horizontalHeaderItem(2)
        item.setText(_translate("SesmimFirstDialog", "Firstname", None))
        item = self.subject_twidget.horizontalHeaderItem(3)
        item.setText(_translate("SesmimFirstDialog", "Lastname", None))
        item = self.subject_twidget.horizontalHeaderItem(4)
        item.setText(_translate("SesmimFirstDialog", "Address", None))
        item = self.subject_twidget.horizontalHeaderItem(5)
        item.setText(_translate("SesmimFirstDialog", "Comment", None))
        self.close_button.setText(_translate("SesmimFirstDialog", "Close", None))
        self.connect_button.setText(_translate("SesmimFirstDialog", "Connect", None))

import resources_rc
