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
from ..model.Au2 import *
from xlsxwriter.utility import xl_rowcol_to_cell, xl_col_to_name
import xlsxwriter
from docxtpl import DocxTemplate, RichText
import os

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

        subjects  = self.session.query(Subject).all()
        for value in subjects:
            print value.id
            item_id = QTableWidgetItem(str(value.id))
            item_id.setData(Qt.UserRole, value.id)
            item_id.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_register = QTableWidgetItem(value.register)
            item_register.setData(Qt.UserRole, value.register)
            item_register.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_firstname = QTableWidgetItem(value.firstname)
            item_firstname.setData(Qt.UserRole, value.firstname)
            item_firstname.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_lastname = QTableWidgetItem(value.lastname)
            item_lastname.setData(Qt.UserRole, value.lastname)
            item_lastname.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_address = QTableWidgetItem(value.address)
            item_address.setData(Qt.UserRole, value.address)
            item_address.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_comment = QTableWidgetItem(value.comment)
            item_comment.setData(Qt.UserRole, value.comment)
            item_comment.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            row = self.subject_twidget.rowCount()
            self.subject_twidget.insertRow(row)
            self.subject_twidget.setItem(row, 0, item_id)
            self.subject_twidget.setItem(row, 1, item_register)
            self.subject_twidget.setItem(row, 2, item_firstname)
            self.subject_twidget.setItem(row, 3, item_lastname)
            self.subject_twidget.setItem(row, 4, item_address)
            self.subject_twidget.setItem(row, 5, item_comment)

    def __spatial_filter(self):

        parcels = self.session.query(Parcel).\
            filter(Au2.geometry.ST_Within(Au2.geometry.ST_Within(Parcel.geometry))).\
            filter(Au2.code == '01122').all()

        for value in parcels:
            print value.parcel_id

    def __report_docx(self):

        path = os.path.join(os.path.dirname(__file__), "../report")

        tpl = DocxTemplate(path + 'first_doc_template.docx')

        register = u'ИБ87122501'
        firstname = u'Дорж'
        lastname = u'Бат'

        context = {
            'register': register,
            'firstname': firstname,
            'lastname': lastname,
        }

        tpl.render(context)
        tpl.save(path + 'first_doc_report.docx')

        QDesktopServices.openUrl(
            QUrl.fromLocalFile(path + 'first_doc_report.docx'))

    def report_xls(self):

        workbook = xlsxwriter.Workbook("D:/first_xls_report.xlsx")
        worksheet = workbook.add_worksheet()

        worksheet.set_column('A:A', 8)
        worksheet.set_column('B:B', 15)
        worksheet.set_column('C:C', 15)

        worksheet.set_landscape()
        worksheet.set_margins(left=0.2, right=0.1)

        format_title = workbook.add_format()
        format_title.set_text_wrap()
        format_title.set_align('center')
        format_title.set_align('vcenter')
        # format1.set_rotation(90)
        format_title.set_font_name('Times New Roman')
        format_title.set_font_size(10)
        format_title.set_border(1)
        format_title.set_bold()

        worksheet.merge_range('A2:K2', u' Эхний тайлан', format_title)

        worksheet.write('A4', u"Регистрийн дугаар", format_title)
        worksheet.write('B4', u"Овог", format_title)
        worksheet.write('C4', u"Нэр", format_title)

        subjects = self.session.query(Subject).all()
        row_count = 4
        col = 0
        for value in subjects:
            worksheet.write(row_count, col, value.register, format_title)
            worksheet.write(row_count, col + 1, value.lastname, format_title)
            worksheet.write(row_count, col + 2, value.firstname, format_title)
            row_count += 1

        workbook.close()
        QDesktopServices.openUrl(QUrl.fromLocalFile("D:/first_xls_report.xlsx"))