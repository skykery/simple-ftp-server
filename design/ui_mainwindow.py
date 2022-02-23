# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(410, 435)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(10, 200, 113, 32))
        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(130, 200, 113, 32))
        self.address_box = QGroupBox(self.centralwidget)
        self.address_box.setObjectName(u"address_box")
        self.address_box.setGeometry(QRect(20, 260, 371, 51))
        self.label_address = QLabel(self.address_box)
        self.label_address.setObjectName(u"label_address")
        self.label_address.setGeometry(QRect(10, 0, 351, 61))
        self.path_box = QGroupBox(self.centralwidget)
        self.path_box.setObjectName(u"path_box")
        self.path_box.setGeometry(QRect(20, 320, 371, 51))
        self.label_path = QLabel(self.path_box)
        self.label_path.setObjectName(u"label_path")
        self.label_path.setGeometry(QRect(10, 10, 351, 41))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 411, 181))
        self.label_user = QLabel(self.widget)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setGeometry(QRect(10, 20, 61, 20))
        self.input_port = QLineEdit(self.widget)
        self.input_port.setObjectName(u"input_port")
        self.input_port.setGeometry(QRect(81, 120, 51, 21))
        self.input_password = QLineEdit(self.widget)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(81, 70, 311, 21))
        self.label_port = QLabel(self.widget)
        self.label_port.setObjectName(u"label_port")
        self.label_port.setGeometry(QRect(10, 120, 61, 20))
        self.label_password = QLabel(self.widget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(10, 70, 61, 20))
        self.input_user = QLineEdit(self.widget)
        self.input_user.setObjectName(u"input_user")
        self.input_user.setGeometry(QRect(81, 20, 311, 21))
        self.btn_path = QPushButton(self.centralwidget)
        self.btn_path.setObjectName(u"btn_path")
        self.btn_path.setGeometry(QRect(250, 200, 113, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.address_box.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_address.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.path_box.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_path.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_user.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_port.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_path.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

