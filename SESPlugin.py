# -*- encoding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from view.resources_rc import *
from controller.SesmimFirstDialog import *
import qgis.core
import os.path

class SESPlugin:

    def __init__(self, iface):

        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

    def initGui(self):

        # Retrieve main menu bar
        menu_bar = self.iface.mainWindow().menuBar()

        # Create menus
        self.ses_menu = QMenu()
        self.ses_menu.setTitle(QApplication.translate("Plugin", "&SESMIM"))
        menu_bar.addMenu(self.ses_menu)

        # Create action that will start plugin configuration
        self.sesmim_first_action = QAction(QIcon(":/plugins/sesmim/crops.png"), QApplication.translate("Plugin", "Sesmim first dialog"), self.iface.mainWindow())
        self.sesmim_second_action = QAction(QIcon(":/plugins/sesmim/certf.png"), QApplication.translate("Plugin", "Sesmim second dialog"), self.iface.mainWindow())

        self.ses_menu.addAction(self.sesmim_first_action)
        self.ses_menu.addSeparator()
        self.ses_menu.addAction(self.sesmim_second_action)

        # Add toolbar button and menu item
        self.ses_toolbar = self.iface.addToolBar(QApplication.translate("Plugin", "SESMIM porject"))

        self.ses_toolbar.addAction(self.sesmim_first_action)
        self.ses_toolbar.addAction(self.sesmim_second_action)

        self.sesmim_first_action.triggered.connect(self.__show_fist_dialog)

    def __show_fist_dialog(self):

        print "-test sesmim plugin 1-"
        dlg = SesmimFirstDialog(self.iface, self.iface.mainWindow())
        dlg.exec_()

    def __first_function(self):

        print 'my first text'

    def unload(self):

        self.iface.removePluginMenu(QApplication.translate("Plugin", "&SESMIM"), self.sesmim_first_action)
        self.iface.removePluginMenu(QApplication.translate("Plugin", "&SESMIM"), self.sesmim_second_action)
