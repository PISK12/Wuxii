# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\GoogleDrive\Informatyka\Projekty\Desktop\Wuxii\Wuxii\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.setEnabled(True)
        Window.resize(431, 370)
        Window.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBoxTop = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxTop.setObjectName("comboBoxTop")
        self.verticalLayout.addWidget(self.comboBoxTop)
        spacerItem = QtWidgets.QSpacerItem(316, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.comboBoxbottom = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxbottom.setObjectName("comboBoxbottom")
        self.verticalLayout.addWidget(self.comboBoxbottom)
        spacerItem1 = QtWidgets.QSpacerItem(316, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.startDownloadButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startDownloadButton.setAutoDefault(True)
        self.startDownloadButton.setDefault(False)
        self.startDownloadButton.setFlat(False)
        self.startDownloadButton.setObjectName("startDownloadButton")
        self.verticalLayout.addWidget(self.startDownloadButton)
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 431, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuOther = QtWidgets.QMenu(self.menubar)
        self.menuOther.setObjectName("menuOther")
        Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)
        self.actionSelect_Catalog = QtWidgets.QAction(Window)
        self.actionSelect_Catalog.setObjectName("actionSelect_Catalog")
        self.actionStop = QtWidgets.QAction(Window)
        self.actionStop.setObjectName("actionStop")
        self.actionReload = QtWidgets.QAction(Window)
        self.actionReload.setObjectName("actionReload")
        self.actionPreferences = QtWidgets.QAction(Window)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout_me = QtWidgets.QAction(Window)
        self.actionAbout_me.setObjectName("actionAbout_me")
        self.actionAbout_App = QtWidgets.QAction(Window)
        self.actionAbout_App.setObjectName("actionAbout_App")
        self.menuMenu.addAction(self.actionSelect_Catalog)
        self.menuMenu.addAction(self.actionStop)
        self.menuMenu.addAction(self.actionPreferences)
        self.menuOther.addAction(self.actionAbout_App)
        self.menuOther.addAction(self.actionAbout_me)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuOther.menuAction())

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MainWindow"))
        self.startDownloadButton.setText(_translate("Window", "Download"))
        self.menuMenu.setTitle(_translate("Window", "Menu"))
        self.menuOther.setTitle(_translate("Window", "Other"))
        self.actionSelect_Catalog.setText(_translate("Window", "Open"))
        self.actionStop.setText(_translate("Window", "Stop Download"))
        self.actionReload.setText(_translate("Window", "Reload"))
        self.actionPreferences.setText(_translate("Window", "Preferences"))
        self.actionAbout_me.setText(_translate("Window", "About Me"))
        self.actionAbout_App.setText(_translate("Window", "About App"))

