# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QToolBar,
    QWidget, QMessageBox)

import numpy as np
from pyqtgraph import PlotWidget
from pyflycap2.interface import Camera, CameraContext

shutter = "shutter"
gain = "gain"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"icons/spectrometer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u"icons/open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u"icons/floppy-disk.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSave.setIcon(icon2)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon3 = QIcon()
        icon3.addFile(u"icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionExit.setIcon(icon3)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        icon4 = QIcon()
        icon4.addFile(u"icons/link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionConnect.setIcon(icon4)
        self.actionDisconnect = QAction(MainWindow)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        icon5 = QIcon()
        icon5.addFile(u"icons/broken-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionDisconnect.setIcon(icon5)
        self.actionConfig = QAction(MainWindow)
        self.actionConfig.setObjectName(u"actionConfig")
        icon6 = QIcon()
        icon6.addFile(u"icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionConfig.setIcon(icon6)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon7 = QIcon()
        icon7.addFile(u"icons/information.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionHelp.setIcon(icon7)
        self.action_Capture = QAction(MainWindow)
        self.action_Capture.setObjectName(u"action_Capture")
        icon8 = QIcon()
        icon8.addFile(u"icons/audio-waves.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_Capture.setIcon(icon8)
        self.actionLiveView = QAction(MainWindow)
        self.actionLiveView.setCheckable(True)
        self.actionLiveView.setObjectName(u"actionLiveView")
        icon9 = QIcon()
        icon9.addFile(u"icons/live-news.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionLiveView.setIcon(icon9)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.GraphWidget = PlotWidget(self.centralwidget)
        self.GraphWidget.setObjectName(u"GraphWidget")
        self.GraphWidget.setGeometry(QRect(9, 9, 771, 481))

        self.horizontalLayout.addWidget(self.GraphWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuSerial = QMenu(self.menubar)
        self.menuSerial.setObjectName(u"menuSerial")
        self.menuConfig = QMenu(self.menubar)
        self.menuConfig.setObjectName(u"menuConfig")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuSerial.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionExit)
        self.menuSerial.addAction(self.actionConnect)
        self.menuSerial.addAction(self.actionDisconnect)
        self.menuSerial.addAction(self.action_Capture)
        self.menuSerial.addAction(self.actionLiveView)
        self.menuConfig.addAction(self.actionConfig)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addAction(self.actionDisconnect)
        self.toolBar.addAction(self.actionLiveView)
        self.toolBar.addAction(self.action_Capture)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConfig)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FTIR Data Acquisition Software", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"&Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Open existing file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"Save the data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
#if QT_CONFIG(tooltip)
        self.actionExit.setToolTip(QCoreApplication.translate("MainWindow", u"Exit the application", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"&Connect", None))
#if QT_CONFIG(tooltip)
        self.actionConnect.setToolTip(QCoreApplication.translate("MainWindow", u"Connect through serial port", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionConnect.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionDisconnect.setText(QCoreApplication.translate("MainWindow", u"&Disconnect", None))
#if QT_CONFIG(tooltip)
        self.actionDisconnect.setToolTip(QCoreApplication.translate("MainWindow", u"Disconnect serial port", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionDisconnect.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionConfig.setText(QCoreApplication.translate("MainWindow", u"&Config", None))
#if QT_CONFIG(tooltip)
        self.actionConfig.setToolTip(QCoreApplication.translate("MainWindow", u"Configeration for settings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionConfig.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+K", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.actionHelp.setToolTip(QCoreApplication.translate("MainWindow", u"About ", None))
#endif // QT_CONFIG(tooltip)
        self.action_Capture.setText(QCoreApplication.translate("MainWindow", u"&Capture", None))
#if QT_CONFIG(shortcut)
        self.action_Capture.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionLiveView.setText(QCoreApplication.translate("MainWindow", u"LiveView", None))
#if QT_CONFIG(shortcut)
        self.actionLiveView.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSerial.setTitle(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.menuConfig.setTitle(QCoreApplication.translate("MainWindow", u"&Settings", None))
#if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi
    
        

