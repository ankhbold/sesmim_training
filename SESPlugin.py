import os.path
# -*- encoding: utf-8 -*-
from trace import Trace

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *
from qgis.core import *
from controller.SesmimFirstDialog import *
from controller.SesmimSecondDialog import *

from view.resources_rc import *
import qgis.core

class SESPlugin:

    def __init__(self, iface):

        # Save reference to the QGIS interface
        self.iface = iface
        self.activeAction = None
        self.activeParcelAction = None
        self.parcel_no = None
        self.result_feature = None
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

    def initGui(self):

        # Create action that will start plugin configuration
        self.sesmim_first_action = QAction(QIcon(":/plugins/sesmim/crops.png"), QApplication.translate("Plugin", "Sesmim first dialog"), self.iface.mainWindow())
        self.sesmim_second_action = QAction(QIcon(":/plugins/sesmim/certf.png"), QApplication.translate("Plugin", "Sesmim second dialog"), self.iface.mainWindow())

        # connect the action to the run method
        self.sesmim_first_action.triggered.connect(self.__show_fist_dialog)
        self.sesmim_second_action.triggered.connect(self.__show_second_dialog)

        # self.reports_action.triggered.connect(self.__show_reports_dialog)


        # Add toolbar button and menu item
        self.lm_toolbar = self.iface.addToolBar(QApplication.translate("Plugin", "SESMIM porject"))

        self.lm_toolbar.addAction(self.sesmim_first_action)
        self.lm_toolbar.addAction(self.sesmim_second_action)


        # Retrieve main menu bar
        menu_bar = self.iface.mainWindow().menuBar()
        actions = menu_bar.actions()

        # Create menus
        self.lm_menu = QMenu()
        self.lm_menu.setTitle(QApplication.translate("Plugin", "&SESMIM"))
        menu_bar.addMenu(self.lm_menu)

        self.lm_menu.addAction(self.sesmim_first_action)
        self.lm_menu.addSeparator()
        self.lm_menu.addAction(self.sesmim_second_action)

    def unload(self):

        self.iface.removePluginMenu(QApplication.translate("Plugin", "&SESMIM"), self.sesmim_first_action)
        self.iface.removePluginMenu(QApplication.translate("Plugin", "&SESMIM"), self.sesmim_second_action)

    def __show_fist_dialog(self):

        print "-test sesmim plugin 1-"
        dlg = SesmimFirstDialog(self.iface, self.iface.mainWindow())
        dlg.exec_()

    def __show_second_dialog(self):

        print "-test sesmim plugin 1-"
        dlg = SesmimSecondDialog(self.iface, self.iface.mainWindow())
        dlg.exec_()