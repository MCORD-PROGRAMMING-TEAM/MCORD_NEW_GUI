# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainKHIjLG.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1317, 767)
        MainWindow.setMinimumSize(QSize(1030, 716))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* #############################################\n"
"MAIN QSS FILE\n"
"EACH STYLE SHOULD BE CHANGE | ADD HERE NOT IN SEPARATED ELEMENTS \n"
"ONLY INDIVIDUALS STAFF SHOULD BE ADDED ALONE (ICONS,IMG) BUT NOT CORE\n"
"\n"
"############################################### */\n"
"\n"
"/* ######### WIDGET ############ */\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"/* ######### TOOLTIP ############ */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color:  #CC576574;\n"
"	border: 1px solid #8395a7;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid #c8d6e5;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"\n"
"/* ######### BACKGROUND ############ */\n"
"#background {\n"
"	background-color:  #2f3542;\n"
"	\n"
"		\n"
"}\n"
"\n"
"/* ######### LEFT MENU ############ */\n"
"#LeftMenuFrame {\n"
"	background-color:  #57606f;\n"
"}\n"
"/* ##"
                        "####### LEFT MENU HIDDEN ############ */\n"
"#ExtraLeftMenuFrame {\n"
"	background-color:  #227093;\n"
"    border-top: 4px solid #202c3b;\n"
"}\n"
"\n"
"/* ######### MAIN BUTTONS FRAME ############ */\n"
"#mainbuttonsframe {\n"
"	border-top: 4px solid #202c3b;\n"
"}\n"
"/* ######### TOGGLE BUTTON ############ */\n"
"#ToggleButton, #SettingsButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"    text-align: left;\n"
"	border-left: 20px solid transparent;\n"
"	padding-left: 44px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#SettingsButton:pressed, #ToggleButton:pressed {	\n"
"	background-color:  #f368e0;\n"
"	color: #000;\n"
"}\n"
"\n"
"/* ######### BUTTONS  MENU LEFT SIDE ############ */\n"
"#buttonsframe .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 15px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#buttonsframe .Q"
                        "PushButton:hover{\n"
"	background-color: #2f3542;\n"
"	border-left: 20px solid transparent;\n"
"}\n"
"#buttonsframe .QPushButton:pressed {	\n"
"	background-color:  #48dbfb;\n"
"	color: #000;\n"
"}\n"
"\n"
"/* ######### TOPBAR ############ */\n"
"#topbarframe{\n"
"	background-color:  #57606f;\n"
"}\n"
"\n"
"\n"
"/* ######### APPICON ############ */\n"
"#appicon{\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	border-left: 10px solid transparent;\n"
"}\n"
"\n"
"/* ######### TOP BUTTONS ############ */\n"
"#closebuttonframe .QPushButton{ \n"
"    background-color: transparent ;\n"
"    border: none;  \n"
"    border-radius: 5px; \n"
"}\n"
"#closebuttonframe .QPushButton:hover { \n"
"   border-style: solid; \n"
"   border-radius: 4px; \n"
"}\n"
"\n"
"#closeButton:hover{\n"
"   background-color: #ff6b6b;\n"
"}\n"
"\n"
"#maximizeButton:hover{\n"
"   background-color: #feca57;\n"
"}\n"
"\n"
"#minimizeButton:hover{\n"
"   backgrou"
                        "nd-color: #1dd1a1;\n"
"}\n"
"\n"
"#closebuttonframe .QPushButton:pressed{ \n"
"   border-style: solid; \n"
"   border-radius: 4px; \n"
"}\n"
"\n"
"#closeButton:pressed{\n"
"   background-color: #ee5253;\n"
"}\n"
"\n"
"#maximizeButton:pressed{\n"
"   background-color: #ff9f43;\n"
"}\n"
"\n"
"#minimizeButton:pressed{\n"
"   background-color: #159472;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ######### FOOTER ############ */\n"
"#footer { \n"
"    background-color: #3f4759;\n"
"}\n"
"#footer QLabel { \n"
"    font-size: 11px;\n"
"    color: #c8d6e5;\n"
"    padding-left: 12px; \n"
"    padding-right: 10px; \n"
"    padding-bottom: 2px;\n"
"}\n"
"#resizeicon{\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 10px solid transparent;\n"
"	border-top: 8px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"}\n"
"\n"
"/* ######### CENTRALFRAME ############ */\n"
"#centralframe {\n"
"	border-top: 4px solid #202c3b;\n"
"}\n"
"\n"
"\n"
"#hub_"
                        "page_content QLabel{\n"
"font: 700 11pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"/*############# EXTRA LEFT MENU #####################*/\n"
"#extralefttext{\n"
"	background:transparent;\n"
"	border:none;\n"
"}\n"
"")
        self.CentralAppMargins = QVBoxLayout(self.centralwidget)
        self.CentralAppMargins.setSpacing(0)
        self.CentralAppMargins.setObjectName(u"CentralAppMargins")
        self.CentralAppMargins.setContentsMargins(10, 10, 10, 10)
        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setToolTipDuration(-1)
        self.background.setFrameShape(QFrame.NoFrame)
        self.background.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.background)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuFrame = QFrame(self.background)
        self.LeftMenuFrame.setObjectName(u"LeftMenuFrame")
        self.LeftMenuFrame.setMinimumSize(QSize(60, 0))
        self.LeftMenuFrame.setMaximumSize(QSize(60, 16777215))
        self.LeftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.LeftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topbuttonframe = QFrame(self.LeftMenuFrame)
        self.topbuttonframe.setObjectName(u"topbuttonframe")
        self.topbuttonframe.setMaximumSize(QSize(16777215, 50))
        self.topbuttonframe.setFrameShape(QFrame.NoFrame)
        self.topbuttonframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.topbuttonframe)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ToggleButton = QPushButton(self.topbuttonframe)
        self.ToggleButton.setObjectName(u"ToggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToggleButton.sizePolicy().hasHeightForWidth())
        self.ToggleButton.setSizePolicy(sizePolicy)
        self.ToggleButton.setMinimumSize(QSize(0, 0))
        self.ToggleButton.setMaximumSize(QSize(16777215, 50))
        self.ToggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ToggleButton.setStyleSheet(u"background-image: url(:/icons/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.ToggleButton)


        self.verticalLayout_2.addWidget(self.topbuttonframe)

        self.mainbuttonsframe = QFrame(self.LeftMenuFrame)
        self.mainbuttonsframe.setObjectName(u"mainbuttonsframe")
        self.mainbuttonsframe.setStyleSheet(u"")
        self.mainbuttonsframe.setFrameShape(QFrame.NoFrame)
        self.mainbuttonsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mainbuttonsframe)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.buttonsframe = QFrame(self.mainbuttonsframe)
        self.buttonsframe.setObjectName(u"buttonsframe")
        self.buttonsframe.setStyleSheet(u"")
        self.buttonsframe.setFrameShape(QFrame.NoFrame)
        self.buttonsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.buttonsframe)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_hub = QPushButton(self.buttonsframe)
        self.btn_hub.setObjectName(u"btn_hub")
        sizePolicy.setHeightForWidth(self.btn_hub.sizePolicy().hasHeightForWidth())
        self.btn_hub.setSizePolicy(sizePolicy)
        self.btn_hub.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.btn_hub.setFont(font)
        self.btn_hub.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hub.setLayoutDirection(Qt.LeftToRight)
        self.btn_hub.setStyleSheet(u"background-image: url(:/icons/icons/chip.png);\n"
"")

        self.verticalLayout_6.addWidget(self.btn_hub)

        self.btn_statistic = QPushButton(self.buttonsframe)
        self.btn_statistic.setObjectName(u"btn_statistic")
        sizePolicy.setHeightForWidth(self.btn_statistic.sizePolicy().hasHeightForWidth())
        self.btn_statistic.setSizePolicy(sizePolicy)
        self.btn_statistic.setMinimumSize(QSize(0, 60))
        self.btn_statistic.setFont(font)
        self.btn_statistic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_statistic.setLayoutDirection(Qt.LeftToRight)
        self.btn_statistic.setStyleSheet(u"background-image: url(:/icons/icons/statistics.png);")

        self.verticalLayout_6.addWidget(self.btn_statistic)

        self.btn_plot = QPushButton(self.buttonsframe)
        self.btn_plot.setObjectName(u"btn_plot")
        sizePolicy.setHeightForWidth(self.btn_plot.sizePolicy().hasHeightForWidth())
        self.btn_plot.setSizePolicy(sizePolicy)
        self.btn_plot.setMinimumSize(QSize(0, 60))
        self.btn_plot.setFont(font)
        self.btn_plot.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plot.setLayoutDirection(Qt.LeftToRight)
        self.btn_plot.setStyleSheet(u"background-image: url(:/icons/icons/graph2.png);")

        self.verticalLayout_6.addWidget(self.btn_plot)

        self.btn_diagnostic = QPushButton(self.buttonsframe)
        self.btn_diagnostic.setObjectName(u"btn_diagnostic")
        self.btn_diagnostic.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_diagnostic.sizePolicy().hasHeightForWidth())
        self.btn_diagnostic.setSizePolicy(sizePolicy)
        self.btn_diagnostic.setMinimumSize(QSize(0, 60))
        self.btn_diagnostic.setFont(font)
        self.btn_diagnostic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_diagnostic.setLayoutDirection(Qt.LeftToRight)
        self.btn_diagnostic.setStyleSheet(u"background-image: url(:/icons/icons/diagnostic.png);")

        self.verticalLayout_6.addWidget(self.btn_diagnostic)

        self.btn_exit = QPushButton(self.buttonsframe)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 60))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_exit)

        self.btn_exit_2 = QPushButton(self.buttonsframe)
        self.btn_exit_2.setObjectName(u"btn_exit_2")
        self.btn_exit_2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_exit_2.sizePolicy().hasHeightForWidth())
        self.btn_exit_2.setSizePolicy(sizePolicy)
        self.btn_exit_2.setMinimumSize(QSize(0, 60))
        self.btn_exit_2.setFont(font)
        self.btn_exit_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit_2.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_exit_2)


        self.verticalLayout_3.addWidget(self.buttonsframe)

        self.sep_frame = QFrame(self.mainbuttonsframe)
        self.sep_frame.setObjectName(u"sep_frame")
        self.sep_frame.setFrameShape(QFrame.StyledPanel)
        self.sep_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.sep_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.sep_frame)

        self.extramenubuttonframe = QFrame(self.mainbuttonsframe)
        self.extramenubuttonframe.setObjectName(u"extramenubuttonframe")
        self.extramenubuttonframe.setMaximumSize(QSize(16777215, 50))
        self.extramenubuttonframe.setCursor(QCursor(Qt.PointingHandCursor))
        self.extramenubuttonframe.setFrameShape(QFrame.NoFrame)
        self.extramenubuttonframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extramenubuttonframe)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.SettingsButton = QPushButton(self.extramenubuttonframe)
        self.SettingsButton.setObjectName(u"SettingsButton")
        sizePolicy.setHeightForWidth(self.SettingsButton.sizePolicy().hasHeightForWidth())
        self.SettingsButton.setSizePolicy(sizePolicy)
        self.SettingsButton.setMinimumSize(QSize(0, 0))
        self.SettingsButton.setMaximumSize(QSize(16777215, 50))
        self.SettingsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SettingsButton.setStyleSheet(u"background-image: url(:/icons/icons/icon_settings.png);")

        self.verticalLayout_5.addWidget(self.SettingsButton)


        self.verticalLayout_3.addWidget(self.extramenubuttonframe)


        self.verticalLayout_2.addWidget(self.mainbuttonsframe)


        self.horizontalLayout.addWidget(self.LeftMenuFrame)

        self.MainContentFrame = QFrame(self.background)
        self.MainContentFrame.setObjectName(u"MainContentFrame")
        self.MainContentFrame.setFrameShape(QFrame.NoFrame)
        self.MainContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.MainContentFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.topbarframe = QFrame(self.MainContentFrame)
        self.topbarframe.setObjectName(u"topbarframe")
        self.topbarframe.setMinimumSize(QSize(0, 50))
        self.topbarframe.setMaximumSize(QSize(16777215, 50))
        self.topbarframe.setFrameShape(QFrame.NoFrame)
        self.topbarframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.topbarframe)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.titleframe = QFrame(self.topbarframe)
        self.titleframe.setObjectName(u"titleframe")
        self.titleframe.setFrameShape(QFrame.StyledPanel)
        self.titleframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleframe)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.appicon = QFrame(self.titleframe)
        self.appicon.setObjectName(u"appicon")
        self.appicon.setMaximumSize(QSize(16777215, 45))
        self.appicon.setStyleSheet(u"background-image: url(:/icons/icons/cil-terminal.png);")
        self.appicon.setFrameShape(QFrame.StyledPanel)
        self.appicon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.appicon)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.horizontalLayout_2.addWidget(self.appicon)

        self.label = QLabel(self.titleframe)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.titleframe)

        self.closebuttonframe = QFrame(self.topbarframe)
        self.closebuttonframe.setObjectName(u"closebuttonframe")
        self.closebuttonframe.setMinimumSize(QSize(0, 28))
        self.closebuttonframe.setFrameShape(QFrame.NoFrame)
        self.closebuttonframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.closebuttonframe)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.closebuttonframe)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(28, 28))
        self.minimizeButton.setMaximumSize(QSize(28, 28))
        self.minimizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)
        self.minimizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.closebuttonframe)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMinimumSize(QSize(28, 28))
        self.maximizeButton.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeButton.setFont(font1)
        self.maximizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximizeButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon1)
        self.maximizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.maximizeButton)

        self.closeButton = QPushButton(self.closebuttonframe)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(28, 28))
        self.closeButton.setMaximumSize(QSize(28, 28))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout_4.addWidget(self.closebuttonframe)


        self.verticalLayout_8.addWidget(self.topbarframe)

        self.bottomcontentframe = QFrame(self.MainContentFrame)
        self.bottomcontentframe.setObjectName(u"bottomcontentframe")
        self.bottomcontentframe.setFrameShape(QFrame.NoFrame)
        self.bottomcontentframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.bottomcontentframe)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ExtraLeftMenuFrame = QFrame(self.bottomcontentframe)
        self.ExtraLeftMenuFrame.setObjectName(u"ExtraLeftMenuFrame")
        self.ExtraLeftMenuFrame.setMinimumSize(QSize(0, 0))
        self.ExtraLeftMenuFrame.setMaximumSize(QSize(0, 16777215))
        self.ExtraLeftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.ExtraLeftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.ExtraLeftMenuFrame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.extralefttext = QTextEdit(self.ExtraLeftMenuFrame)
        self.extralefttext.setObjectName(u"extralefttext")
        self.extralefttext.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_18.addWidget(self.extralefttext)


        self.horizontalLayout_6.addWidget(self.ExtraLeftMenuFrame)

        self.centralmainframe = QFrame(self.bottomcontentframe)
        self.centralmainframe.setObjectName(u"centralmainframe")
        self.centralmainframe.setFrameShape(QFrame.NoFrame)
        self.centralmainframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.centralmainframe)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.centralframe = QFrame(self.centralmainframe)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setFrameShape(QFrame.StyledPanel)
        self.centralframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.centralframe)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.stackedWidget = QStackedWidget(self.centralframe)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setStyleSheet(u"background-color: transparent;")
        self.statistic_page = QWidget()
        self.statistic_page.setObjectName(u"statistic_page")
        self.verticalLayout = QVBoxLayout(self.statistic_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.statistic_page_content = QFrame(self.statistic_page)
        self.statistic_page_content.setObjectName(u"statistic_page_content")
        self.statistic_page_content.setFrameShape(QFrame.StyledPanel)
        self.statistic_page_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.statistic_page_content)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_3 = QLabel(self.statistic_page_content)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 36pt \"Segoe UI\";\n"
"color: rgb(255, 170, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.statistic_page_content)

        self.stackedWidget.addWidget(self.statistic_page)
        self.diagnostic_page = QWidget()
        self.diagnostic_page.setObjectName(u"diagnostic_page")
        self.verticalLayout_24 = QVBoxLayout(self.diagnostic_page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.diagnostic_page_content = QFrame(self.diagnostic_page)
        self.diagnostic_page_content.setObjectName(u"diagnostic_page_content")
        self.diagnostic_page_content.setFrameShape(QFrame.StyledPanel)
        self.diagnostic_page_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.diagnostic_page_content)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_16 = QLabel(self.diagnostic_page_content)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 700 36pt \"Segoe UI\";\n"
"color: rgb(11, 255, 161);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_16)


        self.verticalLayout_24.addWidget(self.diagnostic_page_content)

        self.stackedWidget.addWidget(self.diagnostic_page)
        self.graph_page = QWidget()
        self.graph_page.setObjectName(u"graph_page")
        self.verticalLayout_19 = QVBoxLayout(self.graph_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.graph_page_content = QFrame(self.graph_page)
        self.graph_page_content.setObjectName(u"graph_page_content")
        self.graph_page_content.setFrameShape(QFrame.StyledPanel)
        self.graph_page_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.graph_page_content)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_4 = QLabel(self.graph_page_content)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 36pt \"Segoe UI\";\n"
"color: rgb(85, 170, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_4)


        self.verticalLayout_19.addWidget(self.graph_page_content)

        self.stackedWidget.addWidget(self.graph_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_11 = QVBoxLayout(self.home_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.main_home_page = QFrame(self.home_page)
        self.main_home_page.setObjectName(u"main_home_page")
        self.main_home_page.setStyleSheet(u"background-image: url(:/images/images/nica.png);\n"
"background-repeat :none;\n"
"background-position: center;\n"
"")
        self.main_home_page.setFrameShape(QFrame.StyledPanel)
        self.main_home_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.main_home_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.textEdit = QTextEdit(self.main_home_page)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;\n"
"")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_14.addWidget(self.textEdit)

        self.textEdit_2 = QTextEdit(self.main_home_page)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(222, 0))
        self.textEdit_2.setStyleSheet(u"background: transparent;\n"
"")
        self.textEdit_2.setFrameShape(QFrame.NoFrame)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_14.addWidget(self.textEdit_2)


        self.verticalLayout_11.addWidget(self.main_home_page)

        self.stackedWidget.addWidget(self.home_page)
        self.hub_page = QWidget()
        self.hub_page.setObjectName(u"hub_page")
        self.verticalLayout_15 = QVBoxLayout(self.hub_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.hub_page_content = QFrame(self.hub_page)
        self.hub_page_content.setObjectName(u"hub_page_content")
        sizePolicy2.setHeightForWidth(self.hub_page_content.sizePolicy().hasHeightForWidth())
        self.hub_page_content.setSizePolicy(sizePolicy2)
        self.hub_page_content.setStyleSheet(u"")
        self.hub_page_content.setFrameShape(QFrame.NoFrame)
        self.hub_page_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.hub_page_content)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.Up_frame = QFrame(self.hub_page_content)
        self.Up_frame.setObjectName(u"Up_frame")
        sizePolicy2.setHeightForWidth(self.Up_frame.sizePolicy().hasHeightForWidth())
        self.Up_frame.setSizePolicy(sizePolicy2)
        self.Up_frame.setMaximumSize(QSize(16777215, 200))
        self.Up_frame.setFrameShape(QFrame.NoFrame)
        self.Up_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.Up_frame)
        self.horizontalLayout_16.setSpacing(45)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_16.setContentsMargins(9, 0, 10, 20)
        self.select_conn_frame = QFrame(self.Up_frame)
        self.select_conn_frame.setObjectName(u"select_conn_frame")
        self.select_conn_frame.setMaximumSize(QSize(400, 16777215))
        self.select_conn_frame.setFrameShape(QFrame.NoFrame)
        self.select_conn_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.select_conn_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Connection_label_frame = QFrame(self.select_conn_frame)
        self.Connection_label_frame.setObjectName(u"Connection_label_frame")
        self.Connection_label_frame.setMaximumSize(QSize(16777215, 50))
        self.Connection_label_frame.setStyleSheet(u"background-color: #01a3a4;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"")
        self.Connection_label_frame.setFrameShape(QFrame.NoFrame)
        self.Connection_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.Connection_label_frame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.Connection_label = QLabel(self.Connection_label_frame)
        self.Connection_label.setObjectName(u"Connection_label")
        self.Connection_label.setMaximumSize(QSize(16777215, 50))
        self.Connection_label.setStyleSheet(u"")
        self.Connection_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.Connection_label)


        self.verticalLayout_16.addWidget(self.Connection_label_frame)

        self.connection_body = QFrame(self.select_conn_frame)
        self.connection_body.setObjectName(u"connection_body")
        self.connection_body.setStyleSheet(u"background-color: rgb(68, 75, 89);\n"
"")
        self.connection_body.setFrameShape(QFrame.StyledPanel)
        self.connection_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.connection_body)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.connection_body)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.pushre_1 = QPushButton(self.connection_body)
        self.pushre_1.setObjectName(u"pushre_1")

        self.horizontalLayout_7.addWidget(self.pushre_1)

        self.label_5 = QLabel(self.connection_body)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_5)


        self.verticalLayout_16.addWidget(self.connection_body)

        self.connection_selection = QFrame(self.select_conn_frame)
        self.connection_selection.setObjectName(u"connection_selection")
        self.connection_selection.setStyleSheet(u"#connection_selection{\n"
"background-color: rgb(68, 75, 89);\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"}")
        self.connection_selection.setFrameShape(QFrame.StyledPanel)
        self.connection_selection.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.connection_selection)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.connection_selection_usb = QFrame(self.connection_selection)
        self.connection_selection_usb.setObjectName(u"connection_selection_usb")
        self.connection_selection_usb.setStyleSheet(u"")
        self.connection_selection_usb.setFrameShape(QFrame.NoFrame)
        self.connection_selection_usb.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.connection_selection_usb)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 0, 6, 0)
        self.label_6 = QLabel(self.connection_selection_usb)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.connection_combox = QComboBox(self.connection_selection_usb)
        self.connection_combox.setObjectName(u"connection_combox")
        self.connection_combox.setStyleSheet(u"QComboBox{\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	background-color: #444b59;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #018888;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	\n"
"	border-left-color: rgb(1, 163, 164);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/icons/cil-chevron-double-down.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: #01bfbf;\n"
"	background-color: #2f3542;\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.connection_combox)


        self.horizontalLayout_10.addWidget(self.connection_selection_usb)

        self.connection_selection_lan = QFrame(self.connection_selection)
        self.connection_selection_lan.setObjectName(u"connection_selection_lan")
        self.connection_selection_lan.setMaximumSize(QSize(0, 16777215))
        self.connection_selection_lan.setStyleSheet(u"")
        self.connection_selection_lan.setFrameShape(QFrame.StyledPanel)
        self.connection_selection_lan.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.connection_selection_lan)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(6, 0, 6, 0)
        self.label_7 = QLabel(self.connection_selection_lan)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.connection_edit = QLineEdit(self.connection_selection_lan)
        self.connection_edit.setObjectName(u"connection_edit")
        self.connection_edit.setMinimumSize(QSize(0, 28))
        self.connection_edit.setStyleSheet(u"QLineEdit {\n"
"border-radius:5px;\n"
"border: 2px solid #363c47;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"color: #fff;\n"
"background-color: #444b59;\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid   #018888;\n"
"background-color: #2f3542;\n"
"}")
        self.connection_edit.setAlignment(Qt.AlignCenter)
        self.connection_edit.setClearButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.connection_edit)


        self.horizontalLayout_10.addWidget(self.connection_selection_lan)


        self.verticalLayout_16.addWidget(self.connection_selection)


        self.horizontalLayout_16.addWidget(self.select_conn_frame)

        self.Setting_frame = QFrame(self.Up_frame)
        self.Setting_frame.setObjectName(u"Setting_frame")
        self.Setting_frame.setStyleSheet(u"QComboBox{\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	background-color: #444b59;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #3bb6cf;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	\n"
"	border-left-color: #3bb6cf;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/icons/cil-chevron-double-down.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: #3bb6cf;\n"
"	background-color: #2f3542;\n"
"	padding: 10px;\n"
"}\n"
"QLineEdit {\n"
"border-radius:5px;\n"
"border: 2px solid #363c47;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"color: #fff;\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid #39afc7;\n"
"background-color: #2f3542;\n"
"}\n"
"")
        self.Setting_frame.setFrameShape(QFrame.StyledPanel)
        self.Setting_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.Setting_frame)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.Settings_label_frame = QFrame(self.Setting_frame)
        self.Settings_label_frame.setObjectName(u"Settings_label_frame")
        self.Settings_label_frame.setMaximumSize(QSize(16777215, 50))
        self.Settings_label_frame.setStyleSheet(u"background-color: #42cce8;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"")
        self.Settings_label_frame.setFrameShape(QFrame.NoFrame)
        self.Settings_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.Settings_label_frame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.Settings_label = QLabel(self.Settings_label_frame)
        self.Settings_label.setObjectName(u"Settings_label")
        self.Settings_label.setMaximumSize(QSize(16777215, 50))
        self.Settings_label.setStyleSheet(u"")
        self.Settings_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.Settings_label)


        self.verticalLayout_27.addWidget(self.Settings_label_frame)

        self.Setting_choice_frame = QFrame(self.Setting_frame)
        self.Setting_choice_frame.setObjectName(u"Setting_choice_frame")
        self.Setting_choice_frame.setMaximumSize(QSize(16777215, 60))
        self.Setting_choice_frame.setStyleSheet(u"background-color: rgb(68, 75, 89);")
        self.Setting_choice_frame.setFrameShape(QFrame.NoFrame)
        self.Setting_choice_frame.setFrameShadow(QFrame.Raised)
        self.settings_choice_layout = QHBoxLayout(self.Setting_choice_frame)
        self.settings_choice_layout.setSpacing(15)
        self.settings_choice_layout.setObjectName(u"settings_choice_layout")
        self.label_17 = QLabel(self.Setting_choice_frame)
        self.label_17.setObjectName(u"label_17")

        self.settings_choice_layout.addWidget(self.label_17)

        self.board_combo = QComboBox(self.Setting_choice_frame)
        self.board_combo.setObjectName(u"board_combo")
        self.board_combo.setStyleSheet(u"")

        self.settings_choice_layout.addWidget(self.board_combo)

        self.label_18 = QLabel(self.Setting_choice_frame)
        self.label_18.setObjectName(u"label_18")

        self.settings_choice_layout.addWidget(self.label_18)

        self.simp_combo = QComboBox(self.Setting_choice_frame)
        self.simp_combo.setObjectName(u"simp_combo")

        self.settings_choice_layout.addWidget(self.simp_combo)

        self.settings_button = QPushButton(self.Setting_choice_frame)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setStyleSheet(u"QPushButton:pressed{\n"
"	background-color: rgb(170, 255, 0);\n"
"}")

        self.settings_choice_layout.addWidget(self.settings_button)


        self.verticalLayout_27.addWidget(self.Setting_choice_frame)

        self.frame = QFrame(self.Setting_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame)

        self.Settings_set_master_frame = QFrame(self.Setting_frame)
        self.Settings_set_master_frame.setObjectName(u"Settings_set_master_frame")
        self.Settings_set_master_frame.setMaximumSize(QSize(16777215, 0))
        self.Settings_set_master_frame.setStyleSheet(u"background-color: rgb(68, 75, 89);\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;")
        self.Settings_set_master_frame.setFrameShape(QFrame.NoFrame)
        self.Settings_set_master_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.Settings_set_master_frame)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, 0, 30, 0)
        self.label_19 = QLabel(self.Settings_set_master_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.settings_master_linedit = QLineEdit(self.Settings_set_master_frame)
        self.settings_master_linedit.setObjectName(u"settings_master_linedit")
        self.settings_master_linedit.setMaximumSize(QSize(80, 16777215))
        self.settings_master_linedit.setStyleSheet(u"")
        self.settings_master_linedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.settings_master_linedit)


        self.verticalLayout_27.addWidget(self.Settings_set_master_frame)

        self.Settings_set_slave_frame = QFrame(self.Setting_frame)
        self.Settings_set_slave_frame.setObjectName(u"Settings_set_slave_frame")
        self.Settings_set_slave_frame.setMaximumSize(QSize(16777215, 0))
        self.Settings_set_slave_frame.setStyleSheet(u"background-color: rgb(68, 75, 89);\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;")
        self.Settings_set_slave_frame.setFrameShape(QFrame.StyledPanel)
        self.Settings_set_slave_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.Settings_set_slave_frame)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 0, 30, 0)
        self.label_20 = QLabel(self.Settings_set_slave_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_20)

        self.settings_slave_linedit = QLineEdit(self.Settings_set_slave_frame)
        self.settings_slave_linedit.setObjectName(u"settings_slave_linedit")
        self.settings_slave_linedit.setMaximumSize(QSize(80, 16777215))
        self.settings_slave_linedit.setStyleSheet(u"")
        self.settings_slave_linedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.settings_slave_linedit)


        self.verticalLayout_27.addWidget(self.Settings_set_slave_frame)

        self.Settings_set_both_master_slave_frame = QFrame(self.Setting_frame)
        self.Settings_set_both_master_slave_frame.setObjectName(u"Settings_set_both_master_slave_frame")
        self.Settings_set_both_master_slave_frame.setMaximumSize(QSize(16777215, 0))
        self.Settings_set_both_master_slave_frame.setStyleSheet(u"background-color: rgb(68, 75, 89);\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;")
        self.Settings_set_both_master_slave_frame.setFrameShape(QFrame.StyledPanel)
        self.Settings_set_both_master_slave_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.Settings_set_both_master_slave_frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, 30, 0)
        self.label_21 = QLabel(self.Settings_set_both_master_slave_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_21)

        self.settings_set_both_master_editline = QLineEdit(self.Settings_set_both_master_slave_frame)
        self.settings_set_both_master_editline.setObjectName(u"settings_set_both_master_editline")
        self.settings_set_both_master_editline.setMaximumSize(QSize(80, 16777215))
        self.settings_set_both_master_editline.setStyleSheet(u"")
        self.settings_set_both_master_editline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.settings_set_both_master_editline)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.label_22 = QLabel(self.Settings_set_both_master_slave_frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_22)

        self.settings_set_both_slave_editline = QLineEdit(self.Settings_set_both_master_slave_frame)
        self.settings_set_both_slave_editline.setObjectName(u"settings_set_both_slave_editline")
        self.settings_set_both_slave_editline.setMaximumSize(QSize(80, 16777215))
        self.settings_set_both_slave_editline.setStyleSheet(u"")
        self.settings_set_both_slave_editline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.settings_set_both_slave_editline)


        self.verticalLayout_27.addWidget(self.Settings_set_both_master_slave_frame)


        self.horizontalLayout_16.addWidget(self.Setting_frame)

        self.Console_frame = QFrame(self.Up_frame)
        self.Console_frame.setObjectName(u"Console_frame")
        self.Console_frame.setFrameShape(QFrame.StyledPanel)
        self.Console_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.Console_frame)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.Console_label_frame = QFrame(self.Console_frame)
        self.Console_label_frame.setObjectName(u"Console_label_frame")
        self.Console_label_frame.setMinimumSize(QSize(0, 50))
        self.Console_label_frame.setMaximumSize(QSize(16777215, 50))
        self.Console_label_frame.setStyleSheet(u"background-color: #ff9f43;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"")
        self.Console_label_frame.setFrameShape(QFrame.NoFrame)
        self.Console_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.Console_label_frame)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.Consol_label = QLabel(self.Console_label_frame)
        self.Consol_label.setObjectName(u"Consol_label")
        self.Consol_label.setMaximumSize(QSize(16777215, 50))
        self.Consol_label.setStyleSheet(u"")
        self.Consol_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.Consol_label)


        self.verticalLayout_36.addWidget(self.Console_label_frame)

        self.Console_body_frame = QFrame(self.Console_frame)
        self.Console_body_frame.setObjectName(u"Console_body_frame")
        self.Console_body_frame.setStyleSheet(u"#Console_body_frame{\n"
"background-color: rgb(68, 75, 89);\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"font: 700 12pt \"Terminal\";\n"
"}")
        self.Console_body_frame.setFrameShape(QFrame.StyledPanel)
        self.Console_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.Console_body_frame)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(1, 0, 0, 0)
        self.console = QTextBrowser(self.Console_body_frame)
        self.console.setObjectName(u"console")
        self.console.setStyleSheet(u"border: None;\n"
"background:transparent;")
        self.console.setFrameShape(QFrame.NoFrame)
        self.console.setLineWrapMode(QTextEdit.WidgetWidth)

        self.verticalLayout_35.addWidget(self.console)


        self.verticalLayout_36.addWidget(self.Console_body_frame)


        self.horizontalLayout_16.addWidget(self.Console_frame)

        self.Setting_frame.raise_()
        self.Console_frame.raise_()
        self.select_conn_frame.raise_()

        self.verticalLayout_37.addWidget(self.Up_frame)

        self.Down_frame = QFrame(self.hub_page_content)
        self.Down_frame.setObjectName(u"Down_frame")
        sizePolicy2.setHeightForWidth(self.Down_frame.sizePolicy().hasHeightForWidth())
        self.Down_frame.setSizePolicy(sizePolicy2)
        self.Down_frame.setFrameShape(QFrame.NoFrame)
        self.Down_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.Down_frame)
        self.horizontalLayout_17.setSpacing(45)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(9, 0, 9, 10)
        self.PowerSupply_frame = QFrame(self.Down_frame)
        self.PowerSupply_frame.setObjectName(u"PowerSupply_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.PowerSupply_frame.sizePolicy().hasHeightForWidth())
        self.PowerSupply_frame.setSizePolicy(sizePolicy3)
        self.PowerSupply_frame.setStyleSheet(u"")
        self.PowerSupply_frame.setFrameShape(QFrame.NoFrame)
        self.PowerSupply_frame.setFrameShadow(QFrame.Raised)
        self.PowerSupply_layout = QVBoxLayout(self.PowerSupply_frame)
        self.PowerSupply_layout.setSpacing(0)
        self.PowerSupply_layout.setObjectName(u"PowerSupply_layout")
        self.PowerSupply_layout.setContentsMargins(0, 0, 0, 0)
        self.PowerButton_label_frame = QFrame(self.PowerSupply_frame)
        self.PowerButton_label_frame.setObjectName(u"PowerButton_label_frame")
        self.PowerButton_label_frame.setMaximumSize(QSize(16777215, 50))
        self.PowerButton_label_frame.setStyleSheet(u"background-color: #c59dec;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"")
        self.PowerButton_label_frame.setFrameShape(QFrame.NoFrame)
        self.PowerButton_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.PowerButton_label_frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.PowerButton_label = QLabel(self.PowerButton_label_frame)
        self.PowerButton_label.setObjectName(u"PowerButton_label")
        self.PowerButton_label.setMaximumSize(QSize(16777215, 50))
        self.PowerButton_label.setStyleSheet(u"")
        self.PowerButton_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.PowerButton_label)


        self.PowerSupply_layout.addWidget(self.PowerButton_label_frame)

        self.PowerButton_progressframe = QFrame(self.PowerSupply_frame)
        self.PowerButton_progressframe.setObjectName(u"PowerButton_progressframe")
        self.PowerButton_progressframe.setMaximumSize(QSize(16777215, 0))
        self.PowerButton_progressframe.setStyleSheet(u"background-color: rgb(68, 75, 89);\n"
"")
        self.PowerButton_progressframe.setFrameShape(QFrame.NoFrame)
        self.PowerButton_progressframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.PowerButton_progressframe)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.progressBar = QProgressBar(self.PowerButton_progressframe)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color:#748699;\n"
"color:#fff;\n"
"border-style:none;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.551, x2:1, y2:0.539773, stop:0.346591 rgba(226, 178, 229, 255), stop:0.897727 rgba(194, 137, 242, 255));\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout_23.addWidget(self.progressBar)


        self.PowerSupply_layout.addWidget(self.PowerButton_progressframe)

        self.PowerButton_body = QFrame(self.PowerSupply_frame)
        self.PowerButton_body.setObjectName(u"PowerButton_body")
        self.PowerButton_body.setStyleSheet(u"#PowerButton_body{\n"
"background-color: rgb(68, 75, 89);\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"border-radius:5px;\n"
"border: 2px solid #363c47;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"color: #fff;\n"
"background-color: #444b59;\n"
"font: italic 8pt;\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid #b793dc;\n"
"background-color: #2f3542;\n"
"}")
        self.PowerButton_body.setFrameShape(QFrame.StyledPanel)
        self.PowerButton_body.setFrameShadow(QFrame.Raised)
        self.PowerButton_layout = QVBoxLayout(self.PowerButton_body)
        self.PowerButton_layout.setSpacing(0)
        self.PowerButton_layout.setObjectName(u"PowerButton_layout")
        self.PowerButton_layout.setContentsMargins(0, 0, 0, 0)
        self.button_frame_1 = QFrame(self.PowerButton_body)
        self.button_frame_1.setObjectName(u"button_frame_1")
        self.button_frame_1.setStyleSheet(u"")
        self.button_frame_1.setFrameShape(QFrame.NoFrame)
        self.button_frame_1.setFrameShadow(QFrame.Raised)
        self.button_layout_1 = QHBoxLayout(self.button_frame_1)
        self.button_layout_1.setSpacing(30)
        self.button_layout_1.setObjectName(u"button_layout_1")
        self.button_layout_1.setContentsMargins(15, 0, 15, 0)
        self.label_8 = QLabel(self.button_frame_1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(60, 16777215))

        self.button_layout_1.addWidget(self.label_8)

        self.button_edit_1 = QLineEdit(self.button_frame_1)
        self.button_edit_1.setObjectName(u"button_edit_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.button_edit_1.sizePolicy().hasHeightForWidth())
        self.button_edit_1.setSizePolicy(sizePolicy4)
        self.button_edit_1.setMaximumSize(QSize(100, 25))
        self.button_edit_1.setStyleSheet(u"")
        self.button_edit_1.setAlignment(Qt.AlignCenter)
        self.button_edit_1.setPlaceholderText(u"Board Nr.")
        self.button_edit_1.setClearButtonEnabled(False)

        self.button_layout_1.addWidget(self.button_edit_1)

        self.pushre_2 = QPushButton(self.button_frame_1)
        self.pushre_2.setObjectName(u"pushre_2")

        self.button_layout_1.addWidget(self.pushre_2)


        self.PowerButton_layout.addWidget(self.button_frame_1)

        self.button_frame_2 = QFrame(self.PowerButton_body)
        self.button_frame_2.setObjectName(u"button_frame_2")
        self.button_frame_2.setStyleSheet(u"")
        self.button_frame_2.setFrameShape(QFrame.NoFrame)
        self.button_frame_2.setFrameShadow(QFrame.Raised)
        self.button_layout_2 = QHBoxLayout(self.button_frame_2)
        self.button_layout_2.setSpacing(30)
        self.button_layout_2.setObjectName(u"button_layout_2")
        self.button_layout_2.setContentsMargins(15, 0, 15, 0)
        self.label_9 = QLabel(self.button_frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(60, 16777215))

        self.button_layout_2.addWidget(self.label_9)

        self.button_edit_2 = QLineEdit(self.button_frame_2)
        self.button_edit_2.setObjectName(u"button_edit_2")
        sizePolicy4.setHeightForWidth(self.button_edit_2.sizePolicy().hasHeightForWidth())
        self.button_edit_2.setSizePolicy(sizePolicy4)
        self.button_edit_2.setMaximumSize(QSize(100, 25))
        self.button_edit_2.setStyleSheet(u"")
        self.button_edit_2.setAlignment(Qt.AlignCenter)
        self.button_edit_2.setClearButtonEnabled(False)

        self.button_layout_2.addWidget(self.button_edit_2)

        self.pushre_3 = QPushButton(self.button_frame_2)
        self.pushre_3.setObjectName(u"pushre_3")

        self.button_layout_2.addWidget(self.pushre_3)


        self.PowerButton_layout.addWidget(self.button_frame_2)

        self.button_frame_3 = QFrame(self.PowerButton_body)
        self.button_frame_3.setObjectName(u"button_frame_3")
        self.button_frame_3.setStyleSheet(u"")
        self.button_frame_3.setFrameShape(QFrame.NoFrame)
        self.button_frame_3.setFrameShadow(QFrame.Raised)
        self.button_layout_3 = QHBoxLayout(self.button_frame_3)
        self.button_layout_3.setSpacing(30)
        self.button_layout_3.setObjectName(u"button_layout_3")
        self.button_layout_3.setContentsMargins(15, 0, 15, 0)
        self.label_10 = QLabel(self.button_frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(60, 16777215))

        self.button_layout_3.addWidget(self.label_10)

        self.button_edit_3 = QLineEdit(self.button_frame_3)
        self.button_edit_3.setObjectName(u"button_edit_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.button_edit_3.sizePolicy().hasHeightForWidth())
        self.button_edit_3.setSizePolicy(sizePolicy5)
        self.button_edit_3.setMaximumSize(QSize(100, 25))
        self.button_edit_3.setStyleSheet(u"")
        self.button_edit_3.setAlignment(Qt.AlignCenter)
        self.button_edit_3.setClearButtonEnabled(False)

        self.button_layout_3.addWidget(self.button_edit_3)

        self.pushre_4 = QPushButton(self.button_frame_3)
        self.pushre_4.setObjectName(u"pushre_4")

        self.button_layout_3.addWidget(self.pushre_4)


        self.PowerButton_layout.addWidget(self.button_frame_3)

        self.button_frame_4 = QFrame(self.PowerButton_body)
        self.button_frame_4.setObjectName(u"button_frame_4")
        self.button_frame_4.setStyleSheet(u"")
        self.button_frame_4.setFrameShape(QFrame.NoFrame)
        self.button_frame_4.setFrameShadow(QFrame.Raised)
        self.button_layout_4 = QHBoxLayout(self.button_frame_4)
        self.button_layout_4.setSpacing(30)
        self.button_layout_4.setObjectName(u"button_layout_4")
        self.button_layout_4.setContentsMargins(15, 0, 15, 0)
        self.label_11 = QLabel(self.button_frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(60, 16777215))

        self.button_layout_4.addWidget(self.label_11)

        self.button_edit_4 = QLineEdit(self.button_frame_4)
        self.button_edit_4.setObjectName(u"button_edit_4")
        sizePolicy5.setHeightForWidth(self.button_edit_4.sizePolicy().hasHeightForWidth())
        self.button_edit_4.setSizePolicy(sizePolicy5)
        self.button_edit_4.setMaximumSize(QSize(100, 25))
        self.button_edit_4.setStyleSheet(u"")
        self.button_edit_4.setAlignment(Qt.AlignCenter)
        self.button_edit_4.setClearButtonEnabled(False)

        self.button_layout_4.addWidget(self.button_edit_4)

        self.pushre_5 = QPushButton(self.button_frame_4)
        self.pushre_5.setObjectName(u"pushre_5")

        self.button_layout_4.addWidget(self.pushre_5)


        self.PowerButton_layout.addWidget(self.button_frame_4)

        self.button_frame_5 = QFrame(self.PowerButton_body)
        self.button_frame_5.setObjectName(u"button_frame_5")
        self.button_frame_5.setStyleSheet(u"")
        self.button_frame_5.setFrameShape(QFrame.NoFrame)
        self.button_frame_5.setFrameShadow(QFrame.Raised)
        self.button_layout_5 = QHBoxLayout(self.button_frame_5)
        self.button_layout_5.setSpacing(30)
        self.button_layout_5.setObjectName(u"button_layout_5")
        self.button_layout_5.setContentsMargins(15, 0, 15, 0)
        self.label_12 = QLabel(self.button_frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(60, 16777215))

        self.button_layout_5.addWidget(self.label_12)

        self.button_edit_5 = QLineEdit(self.button_frame_5)
        self.button_edit_5.setObjectName(u"button_edit_5")
        sizePolicy5.setHeightForWidth(self.button_edit_5.sizePolicy().hasHeightForWidth())
        self.button_edit_5.setSizePolicy(sizePolicy5)
        self.button_edit_5.setMaximumSize(QSize(100, 25))
        self.button_edit_5.setStyleSheet(u"")
        self.button_edit_5.setAlignment(Qt.AlignCenter)
        self.button_edit_5.setClearButtonEnabled(False)

        self.button_layout_5.addWidget(self.button_edit_5)

        self.pushre_6 = QPushButton(self.button_frame_5)
        self.pushre_6.setObjectName(u"pushre_6")

        self.button_layout_5.addWidget(self.pushre_6)


        self.PowerButton_layout.addWidget(self.button_frame_5)

        self.button_frame_6 = QFrame(self.PowerButton_body)
        self.button_frame_6.setObjectName(u"button_frame_6")
        self.button_frame_6.setStyleSheet(u"")
        self.button_frame_6.setFrameShape(QFrame.NoFrame)
        self.button_frame_6.setFrameShadow(QFrame.Raised)
        self.button_layout_6 = QHBoxLayout(self.button_frame_6)
        self.button_layout_6.setSpacing(30)
        self.button_layout_6.setObjectName(u"button_layout_6")
        self.button_layout_6.setContentsMargins(15, 0, 15, 0)
        self.label_13 = QLabel(self.button_frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(60, 16777215))

        self.button_layout_6.addWidget(self.label_13)

        self.button_edit_6 = QLineEdit(self.button_frame_6)
        self.button_edit_6.setObjectName(u"button_edit_6")
        sizePolicy5.setHeightForWidth(self.button_edit_6.sizePolicy().hasHeightForWidth())
        self.button_edit_6.setSizePolicy(sizePolicy5)
        self.button_edit_6.setMaximumSize(QSize(100, 25))
        self.button_edit_6.setStyleSheet(u"")
        self.button_edit_6.setAlignment(Qt.AlignCenter)
        self.button_edit_6.setClearButtonEnabled(False)

        self.button_layout_6.addWidget(self.button_edit_6)

        self.pushre_7 = QPushButton(self.button_frame_6)
        self.pushre_7.setObjectName(u"pushre_7")

        self.button_layout_6.addWidget(self.pushre_7)


        self.PowerButton_layout.addWidget(self.button_frame_6)

        self.button_frame_7 = QFrame(self.PowerButton_body)
        self.button_frame_7.setObjectName(u"button_frame_7")
        self.button_frame_7.setStyleSheet(u"")
        self.button_frame_7.setFrameShape(QFrame.NoFrame)
        self.button_frame_7.setFrameShadow(QFrame.Raised)
        self.button_layout_7 = QHBoxLayout(self.button_frame_7)
        self.button_layout_7.setSpacing(30)
        self.button_layout_7.setObjectName(u"button_layout_7")
        self.button_layout_7.setContentsMargins(15, 0, 15, 0)
        self.label_14 = QLabel(self.button_frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(60, 16777215))

        self.button_layout_7.addWidget(self.label_14)

        self.button_edit_7 = QLineEdit(self.button_frame_7)
        self.button_edit_7.setObjectName(u"button_edit_7")
        sizePolicy5.setHeightForWidth(self.button_edit_7.sizePolicy().hasHeightForWidth())
        self.button_edit_7.setSizePolicy(sizePolicy5)
        self.button_edit_7.setMaximumSize(QSize(100, 25))
        self.button_edit_7.setStyleSheet(u"")
        self.button_edit_7.setAlignment(Qt.AlignCenter)
        self.button_edit_7.setClearButtonEnabled(False)

        self.button_layout_7.addWidget(self.button_edit_7)

        self.pushre_8 = QPushButton(self.button_frame_7)
        self.pushre_8.setObjectName(u"pushre_8")

        self.button_layout_7.addWidget(self.pushre_8)


        self.PowerButton_layout.addWidget(self.button_frame_7)

        self.button_frame_8 = QFrame(self.PowerButton_body)
        self.button_frame_8.setObjectName(u"button_frame_8")
        self.button_frame_8.setStyleSheet(u"")
        self.button_frame_8.setFrameShape(QFrame.NoFrame)
        self.button_frame_8.setFrameShadow(QFrame.Raised)
        self.button_layout_8 = QHBoxLayout(self.button_frame_8)
        self.button_layout_8.setSpacing(30)
        self.button_layout_8.setObjectName(u"button_layout_8")
        self.button_layout_8.setContentsMargins(15, 0, 15, 0)
        self.label_15 = QLabel(self.button_frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(60, 16777215))

        self.button_layout_8.addWidget(self.label_15)

        self.button_edit_8 = QLineEdit(self.button_frame_8)
        self.button_edit_8.setObjectName(u"button_edit_8")
        sizePolicy5.setHeightForWidth(self.button_edit_8.sizePolicy().hasHeightForWidth())
        self.button_edit_8.setSizePolicy(sizePolicy5)
        self.button_edit_8.setMaximumSize(QSize(100, 25))
        self.button_edit_8.setStyleSheet(u"")
        self.button_edit_8.setAlignment(Qt.AlignCenter)
        self.button_edit_8.setClearButtonEnabled(False)

        self.button_layout_8.addWidget(self.button_edit_8)

        self.pushre_9 = QPushButton(self.button_frame_8)
        self.pushre_9.setObjectName(u"pushre_9")

        self.button_layout_8.addWidget(self.pushre_9)


        self.PowerButton_layout.addWidget(self.button_frame_8)


        self.PowerSupply_layout.addWidget(self.PowerButton_body)


        self.horizontalLayout_17.addWidget(self.PowerSupply_frame)

        self.Parameters_frame = QFrame(self.Down_frame)
        self.Parameters_frame.setObjectName(u"Parameters_frame")
        self.Parameters_frame.setStyleSheet(u"QComboBox{\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	background-color: #444b59;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #ee5253;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	\n"
"	border-left-color: #ee5253;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/icons/cil-chevron-double-down.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: #ee5253;\n"
"	background-color: #2f3542;\n"
"	padding: 10px;\n"
"}\n"
"#Parameters_body_frame{\n"
"background-color: rgb(68, 75, 89);\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"}\n"
"")
        self.Parameters_frame.setFrameShape(QFrame.NoFrame)
        self.Parameters_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.Parameters_frame)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Parameters_label_frame = QFrame(self.Parameters_frame)
        self.Parameters_label_frame.setObjectName(u"Parameters_label_frame")
        self.Parameters_label_frame.setMaximumSize(QSize(16777215, 50))
        self.Parameters_label_frame.setStyleSheet(u"background-color: #ff6b6b;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"")
        self.Parameters_label_frame.setFrameShape(QFrame.NoFrame)
        self.Parameters_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.Parameters_label_frame)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.Parameters_label = QLabel(self.Parameters_label_frame)
        self.Parameters_label.setObjectName(u"Parameters_label")
        self.Parameters_label.setMaximumSize(QSize(16777215, 50))
        self.Parameters_label.setStyleSheet(u"")
        self.Parameters_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.Parameters_label)


        self.verticalLayout_29.addWidget(self.Parameters_label_frame)

        self.Parameters_body_frame = QFrame(self.Parameters_frame)
        self.Parameters_body_frame.setObjectName(u"Parameters_body_frame")
        self.Parameters_body_frame.setFrameShape(QFrame.NoFrame)
        self.Parameters_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.Parameters_body_frame)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.Parameters_dashinfo = QFrame(self.Parameters_body_frame)
        self.Parameters_dashinfo.setObjectName(u"Parameters_dashinfo")
        self.Parameters_dashinfo.setMaximumSize(QSize(16777215, 60))
        self.Parameters_dashinfo.setStyleSheet(u"background-color: rgb(68, 75, 89);")
        self.Parameters_dashinfo.setFrameShape(QFrame.StyledPanel)
        self.Parameters_dashinfo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.Parameters_dashinfo)
        self.horizontalLayout_15.setSpacing(50)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(150, 0, 150, 0)
        self.label_23 = QLabel(self.Parameters_dashinfo)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_15.addWidget(self.label_23)

        self.parameters_board_combo = QComboBox(self.Parameters_dashinfo)
        self.parameters_board_combo.setObjectName(u"parameters_board_combo")
        self.parameters_board_combo.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.parameters_board_combo)


        self.verticalLayout_34.addWidget(self.Parameters_dashinfo)

        self.Parameter_preview_frame = QFrame(self.Parameters_body_frame)
        self.Parameter_preview_frame.setObjectName(u"Parameter_preview_frame")
        self.Parameter_preview_frame.setStyleSheet(u"#Settings_preview_frame{\n"
"background-color: rgb(68, 75, 89);\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"}")
        self.Parameter_preview_frame.setFrameShape(QFrame.NoFrame)
        self.Parameter_preview_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.Parameter_preview_frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Master_frame = QFrame(self.Parameter_preview_frame)
        self.Master_frame.setObjectName(u"Master_frame")
        self.Master_frame.setFrameShape(QFrame.StyledPanel)
        self.Master_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.Master_frame)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.Master_frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 31))
        self.label_27.setMaximumSize(QSize(16777215, 31))
        self.label_27.setStyleSheet(u"background-color: #f368e0;")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_27)

        self.master_circ_frame = QFrame(self.Master_frame)
        self.master_circ_frame.setObjectName(u"master_circ_frame")
        self.master_circ_frame.setFrameShape(QFrame.NoFrame)
        self.master_circ_frame.setFrameShadow(QFrame.Raised)
        self.master_layout = QVBoxLayout(self.master_circ_frame)
        self.master_layout.setSpacing(0)
        self.master_layout.setObjectName(u"master_layout")
        self.master_layout.setContentsMargins(40, 40, 40, 40)

        self.verticalLayout_33.addWidget(self.master_circ_frame)


        self.horizontalLayout_11.addWidget(self.Master_frame)

        self.Slave_frame = QFrame(self.Parameter_preview_frame)
        self.Slave_frame.setObjectName(u"Slave_frame")
        self.Slave_frame.setFrameShape(QFrame.StyledPanel)
        self.Slave_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.Slave_frame)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.Slave_frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 31))
        self.label_24.setMaximumSize(QSize(16777215, 31))
        self.label_24.setStyleSheet(u"background-color: #54a0ff;")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_24)

        self.Slave_circ_frame = QFrame(self.Slave_frame)
        self.Slave_circ_frame.setObjectName(u"Slave_circ_frame")
        self.Slave_circ_frame.setFrameShape(QFrame.NoFrame)
        self.Slave_circ_frame.setFrameShadow(QFrame.Raised)
        self.slave_layout = QVBoxLayout(self.Slave_circ_frame)
        self.slave_layout.setSpacing(0)
        self.slave_layout.setObjectName(u"slave_layout")
        self.slave_layout.setContentsMargins(40, 40, 40, 40)

        self.verticalLayout_30.addWidget(self.Slave_circ_frame)


        self.horizontalLayout_11.addWidget(self.Slave_frame)

        self.Temperature_frame = QFrame(self.Parameter_preview_frame)
        self.Temperature_frame.setObjectName(u"Temperature_frame")
        self.Temperature_frame.setFrameShape(QFrame.StyledPanel)
        self.Temperature_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.Temperature_frame)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.Temperature_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 31))
        self.label_25.setMaximumSize(QSize(16777215, 31))
        self.label_25.setStyleSheet(u"background-color: #1dd1a1;")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_25)

        self.Temperature_circ_frame = QFrame(self.Temperature_frame)
        self.Temperature_circ_frame.setObjectName(u"Temperature_circ_frame")
        self.Temperature_circ_frame.setFrameShape(QFrame.NoFrame)
        self.Temperature_circ_frame.setFrameShadow(QFrame.Raised)
        self.temperature_layout = QVBoxLayout(self.Temperature_circ_frame)
        self.temperature_layout.setSpacing(0)
        self.temperature_layout.setObjectName(u"temperature_layout")
        self.temperature_layout.setContentsMargins(40, 40, 40, 40)

        self.verticalLayout_31.addWidget(self.Temperature_circ_frame)


        self.horizontalLayout_11.addWidget(self.Temperature_frame)


        self.verticalLayout_34.addWidget(self.Parameter_preview_frame)


        self.verticalLayout_29.addWidget(self.Parameters_body_frame)


        self.horizontalLayout_17.addWidget(self.Parameters_frame)


        self.verticalLayout_37.addWidget(self.Down_frame)


        self.verticalLayout_15.addWidget(self.hub_page_content)

        self.stackedWidget.addWidget(self.hub_page)

        self.verticalLayout_13.addWidget(self.stackedWidget)


        self.verticalLayout_9.addWidget(self.centralframe)

        self.footer = QFrame(self.centralmainframe)
        self.footer.setObjectName(u"footer")
        self.footer.setMaximumSize(QSize(16777215, 22))
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.credits = QLabel(self.footer)
        self.credits.setObjectName(u"credits")
        self.credits.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_5.addWidget(self.credits)

        self.version = QLabel(self.footer)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.resizeicon = QFrame(self.footer)
        self.resizeicon.setObjectName(u"resizeicon")
        self.resizeicon.setMaximumSize(QSize(20, 16777215))
        self.resizeicon.setStyleSheet(u"background-image: url(:/icons/icons/cil-size-grip.png);")
        self.resizeicon.setFrameShape(QFrame.NoFrame)
        self.resizeicon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.resizeicon)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.resizeicon)


        self.verticalLayout_9.addWidget(self.footer)


        self.horizontalLayout_6.addWidget(self.centralmainframe)


        self.verticalLayout_8.addWidget(self.bottomcontentframe)


        self.horizontalLayout.addWidget(self.MainContentFrame)


        self.CentralAppMargins.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_statistic, self.btn_plot)
        QWidget.setTabOrder(self.btn_plot, self.connection_edit)
        QWidget.setTabOrder(self.connection_edit, self.btn_diagnostic)
        QWidget.setTabOrder(self.btn_diagnostic, self.board_combo)
        QWidget.setTabOrder(self.board_combo, self.btn_exit)
        QWidget.setTabOrder(self.btn_exit, self.SettingsButton)
        QWidget.setTabOrder(self.SettingsButton, self.minimizeButton)
        QWidget.setTabOrder(self.minimizeButton, self.maximizeButton)
        QWidget.setTabOrder(self.maximizeButton, self.closeButton)
        QWidget.setTabOrder(self.closeButton, self.extralefttext)
        QWidget.setTabOrder(self.extralefttext, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.textEdit_2)
        QWidget.setTabOrder(self.textEdit_2, self.pushre_1)
        QWidget.setTabOrder(self.pushre_1, self.connection_combox)
        QWidget.setTabOrder(self.connection_combox, self.ToggleButton)
        QWidget.setTabOrder(self.ToggleButton, self.button_edit_1)
        QWidget.setTabOrder(self.button_edit_1, self.pushre_2)
        QWidget.setTabOrder(self.pushre_2, self.button_edit_2)
        QWidget.setTabOrder(self.button_edit_2, self.pushre_3)
        QWidget.setTabOrder(self.pushre_3, self.button_edit_3)
        QWidget.setTabOrder(self.button_edit_3, self.pushre_4)
        QWidget.setTabOrder(self.pushre_4, self.button_edit_4)
        QWidget.setTabOrder(self.button_edit_4, self.pushre_5)
        QWidget.setTabOrder(self.pushre_5, self.button_edit_5)
        QWidget.setTabOrder(self.button_edit_5, self.pushre_6)
        QWidget.setTabOrder(self.pushre_6, self.button_edit_6)
        QWidget.setTabOrder(self.button_edit_6, self.pushre_7)
        QWidget.setTabOrder(self.pushre_7, self.button_edit_7)
        QWidget.setTabOrder(self.button_edit_7, self.pushre_8)
        QWidget.setTabOrder(self.pushre_8, self.button_edit_8)
        QWidget.setTabOrder(self.button_edit_8, self.pushre_9)
        QWidget.setTabOrder(self.pushre_9, self.btn_hub)
        QWidget.setTabOrder(self.btn_hub, self.simp_combo)
        QWidget.setTabOrder(self.simp_combo, self.settings_button)
        QWidget.setTabOrder(self.settings_button, self.settings_master_linedit)
        QWidget.setTabOrder(self.settings_master_linedit, self.settings_slave_linedit)
        QWidget.setTabOrder(self.settings_slave_linedit, self.settings_set_both_master_editline)
        QWidget.setTabOrder(self.settings_set_both_master_editline, self.settings_set_both_slave_editline)
        QWidget.setTabOrder(self.settings_set_both_slave_editline, self.parameters_board_combo)
        QWidget.setTabOrder(self.parameters_board_combo, self.console)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ToggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_hub.setText(QCoreApplication.translate("MainWindow", u"     Hub Management", None))
        self.btn_statistic.setText(QCoreApplication.translate("MainWindow", u"     SiMP's Info", None))
        self.btn_plot.setText(QCoreApplication.translate("MainWindow", u"     Graph", None))
        self.btn_diagnostic.setText(QCoreApplication.translate("MainWindow", u"     Diagnostics", None))
        self.btn_exit.setText("")
        self.btn_exit_2.setText("")
        self.SettingsButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"MCORD GUI Application", None))
#if QT_CONFIG(tooltip)
        self.minimizeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeButton.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeButton.setText("")
        self.extralefttext.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An application created by</span><span style=\" color:#ffaaff;\"> kruksik </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">for the management and servicing of AFE</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Additional software settings may </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">appear in this panel in the future</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Will be information about all \n"
"working SiPM's here", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Will be diagnostic page here", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Will be graph here", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#2bd6df;\">Graphical User Interface for MCORD HUB management</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">The program was created to facilitate the "
                        "work and servicing of hubs and AFEs located on the boards of the MCORD system</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: kruksik</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-"
                        "top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">To start using this software, please click   </span><img src=\":/icons/icons/icon_menu.png\" />  <span style=\" font-size:12pt; color:#ffffff;\"> icon on the top right corner and then select an option from the menu </span></p></body></html>", None))
        self.Connection_label.setText(QCoreApplication.translate("MainWindow", u"Select connection ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"USB", None))
        self.pushre_1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LAN", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Select COM port: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Enter IP address:", None))
        self.connection_edit.setText("")
        self.connection_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"eg. 10.2.31.2", None))
        self.Settings_label.setText(QCoreApplication.translate("MainWindow", u"Settings ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Select Board:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Select SiPM: ", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Set voltage at Master SiPM:", None))
        self.settings_master_linedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"eg. 58.5", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Set voltage at Slave SiPM:", None))
        self.settings_slave_linedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"eg. 58.5", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Master voltage:     ", None))
        self.settings_set_both_master_editline.setPlaceholderText(QCoreApplication.translate("MainWindow", u"eg. 58.5", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Slave voltage:     ", None))
        self.settings_set_both_slave_editline.setPlaceholderText(QCoreApplication.translate("MainWindow", u"eg. 58.5", None))
        self.Consol_label.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.console.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt;&gt; Text will be here</p></body></html>", None))
        self.PowerButton_label.setText(QCoreApplication.translate("MainWindow", u"Power Supply", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Port 1 :", None))
        self.button_edit_1.setText("")
        self.pushre_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Port 2 :", None))
        self.button_edit_2.setText("")
        self.button_edit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Board Nr.", None))
        self.pushre_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Port 3 :", None))
        self.button_edit_3.setText("")
        self.button_edit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Board Nr.", None))
        self.pushre_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Port 4 :", None))
        self.button_edit_4.setText("")
        self.button_edit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Board Nr.", None))
        self.pushre_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Port 5 :", None))
        self.button_edit_5.setText("")
        self.button_edit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Board Nr.", None))
        self.pushre_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Port 6 :", None))
        self.button_edit_6.setText("")
        self.button_edit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Board Nr.", None))
        self.pushre_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Port 7 :", None))
        self.button_edit_7.setText("")
        self.button_edit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Board Nr.", None))
        self.pushre_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Port 8 :", None))
        self.button_edit_8.setText("")
        self.button_edit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Board Nr.", None))
        self.pushre_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Parameters_label.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Select Board:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Master SiMP voltage", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Slave SiMP voltage", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.credits.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

