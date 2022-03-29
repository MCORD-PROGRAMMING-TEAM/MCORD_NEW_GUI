# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenSVIdkn.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from .. import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1180, 755)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#main_frame{\n"
"border-top-left-radius: 45px;\n"
"border-bottom-left-radius: 45px;\n"
"border-left-style: solid;\n"
"border-top-style: solid;\n"
"border-bottom-style: solid;\n"
"border-left-width:2px;\n"
"border-top-width:2px;\n"
"border-bottom-width:2px;\n"
"border-color: #2f3542;\n"
"\n"
"}\n"
"\n"
"#logo_frame{\n"
"border-top-right-radius: 45px;\n"
"border-bottom-right-radius: 45px;\n"
"border-top-style: solid;\n"
"border-right-style: solid;\n"
"border-bottom-style: solid;\n"
"border-right-width:2px;\n"
"border-top-width:2px;\n"
"border-bottom-width:2px;\n"
"border-color: #2f3542;\n"
"}\n"
"\n"
"#label {\n"
"color: #ff9ff3;\n"
"font: 36pt \"Segoe UI\";\n"
"}\n"
"\n"
"#desc{\n"
"color: #48dbfb;\n"
"font: 18pt \"Segoe UI\";\n"
"}\n"
"\n"
"QProgressBar{\n"
"background-color:#748699;\n"
"color:#fff;\n"
"border-style:none;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.551, x2:1, y2:0.53977"
                        "3, stop:0.346591 rgba(226, 178, 229, 255), stop:0.897727 rgba(194, 137, 242, 255));\n"
"}\n"
"\n"
"#loading{\n"
"color:#fff;\n"
"font: 12pt;\n"
"}\n"
"\n"
"#credits{\n"
"font: 700 8pt;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(120, 90, 631, 511))
        self.main_frame.setStyleSheet(u"#main_frame{\n"
"background-color: qlineargradient(spread:pad, x1:0.482955, y1:0.234, x2:0.489, y2:0.994318, stop:0.0454545 rgba(87, 101, 116, 248), stop:0.482955 rgba(114, 126, 138, 246), stop:1 rgba(255, 255, 255, 129));\n"
"}")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.main_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 401, 61))
        font = QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.desc = QLabel(self.main_frame)
        self.desc.setObjectName(u"desc")
        self.desc.setGeometry(QRect(100, 120, 421, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.desc.setFont(font1)
        self.desc.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.main_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 420, 491, 23))
        self.progressBar.setValue(24)
        self.loading = QLabel(self.main_frame)
        self.loading.setObjectName(u"loading")
        self.loading.setGeometry(QRect(160, 360, 341, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.loading.setFont(font2)
        self.loading.setAlignment(Qt.AlignCenter)
        self.credits = QLabel(self.main_frame)
        self.credits.setObjectName(u"credits")
        self.credits.setGeometry(QRect(250, 480, 151, 20))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setItalic(False)
        self.credits.setFont(font3)
        self.credits.setAlignment(Qt.AlignCenter)
        self.logo_frame = QFrame(self.centralwidget)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setGeometry(QRect(750, 90, 361, 511))
        self.logo_frame.setStyleSheet(u"#logo_frame{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 159, 243, 228), stop:1 rgba(86, 221, 251, 215));\n"
"}")
        self.logo_frame.setFrameShape(QFrame.NoFrame)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.logo_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 100, 321, 311))
        self.frame.setStyleSheet(u"image: url(:/images/images/mcord.png);\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.logo_frame.raise_()
        self.main_frame.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">MCORD </span>service </p></body></html>", None))
        self.desc.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Service GUI for manage <span style=\" font-weight:700;\">MCORD HUB</span></p></body></html>", None))
        self.loading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>loading ...</p></body></html>", None))
        self.credits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>created by: kruksik v1.0.2</p></body></html>", None))
    # retranslateUi

