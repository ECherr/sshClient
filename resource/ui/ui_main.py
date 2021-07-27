# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 715)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 10pt \"Segoe UI\"\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	back"
                        "ground-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#menu {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#logo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/resource/images/icons/video-game-mario-3-32.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"	border-right: 5px solid transparent;\n"
"	border-top: 10px solid transparent;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"\n"
"\n"
"/* MENUS */\n"
"#menuBox .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 15px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#menuBox .QPushButton:hover {\n"
"	back"
                        "ground-color: rgb(40, 44, 52);\n"
"}\n"
"#menuBox .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 15px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 40px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#btnToggle {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 15px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 40px;\n"
"	color: rgb(113, 126, 149);\n"
"	\n"
"}\n"
"#btnToggle:hover "
                        "{\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#btnToggle:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"#contentTop{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"#contentFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"\n"
"/* MENU BUTTON FRAME */\n"
"#menuButtonFrame .QPushButton {	\n"
"	background-color: rgba(255, 255, 255, 0); \n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"}\n"
"#menuButtonFrame .QPushButton:hover {\n"
"	background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px;\n"
"}\n"
"#menuButtonFrame .QPushButton:pressed {	\n"
"	background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px;\n"
"	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-col"
                        "or: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.bgApp)
        self.menu.setObjectName(u"menu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(120)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setMinimumSize(QSize(50, 0))
        self.menu.setMaximumSize(QSize(50, 16777215))
        self.menu.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logoInfo = QFrame(self.menu)
        self.logoInfo.setObjectName(u"logoInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.logoInfo.sizePolicy().hasHeightForWidth())
        self.logoInfo.setSizePolicy(sizePolicy1)
        self.logoInfo.setMinimumSize(QSize(0, 50))
        self.logoInfo.setMaximumSize(QSize(16777215, 50))
        self.logoInfo.setFrameShape(QFrame.StyledPanel)
        self.logoInfo.setFrameShadow(QFrame.Raised)
        self.logo = QFrame(self.logoInfo)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 0, 50, 50))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy2)
        self.logo.setMinimumSize(QSize(50, 50))
        self.logo.setMaximumSize(QSize(50, 50))
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.logoInfo)

        self.leftMenuFrame = QFrame(self.menu)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(50, 0))
        self.leftMenuFrame.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMinimumSize(QSize(50, 50))
        self.toggleBox.setMaximumSize(QSize(50, 50))
        self.verticalLayout_7 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btnToggle = QPushButton(self.toggleBox)
        self.btnToggle.setObjectName(u"btnToggle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnToggle.sizePolicy().hasHeightForWidth())
        self.btnToggle.setSizePolicy(sizePolicy3)
        self.btnToggle.setMinimumSize(QSize(50, 50))
        self.btnToggle.setMaximumSize(QSize(16777215, 16777215))
        self.btnToggle.setStyleSheet(u"background-image: url(:/resource/images/icons/toggle-16.png)")
        self.btnToggle.setIconSize(QSize(12, 12))

        self.verticalLayout_7.addWidget(self.btnToggle)


        self.verticalLayout_5.addWidget(self.toggleBox)

        self.menuBox = QFrame(self.leftMenuFrame)
        self.menuBox.setObjectName(u"menuBox")
        self.menuBox.setMinimumSize(QSize(50, 0))
        self.menuBox.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.menuBox)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.menuStackWidget = QStackedWidget(self.menuBox)
        self.menuStackWidget.setObjectName(u"menuStackWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.menuStackWidget.sizePolicy().hasHeightForWidth())
        self.menuStackWidget.setSizePolicy(sizePolicy4)
        self.connectMenu = QWidget()
        self.connectMenu.setObjectName(u"connectMenu")
        self.connectMenu.setAutoFillBackground(False)
        self.connectFrame = QFrame(self.connectMenu)
        self.connectFrame.setObjectName(u"connectFrame")
        self.connectFrame.setGeometry(QRect(0, 0, 120, 541))
        self.connectFrame.setMinimumSize(QSize(50, 0))
        self.verticalLayout_9 = QVBoxLayout(self.connectFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btnConnectHome = QPushButton(self.connectFrame)
        self.btnConnectHome.setObjectName(u"btnConnectHome")
        sizePolicy3.setHeightForWidth(self.btnConnectHome.sizePolicy().hasHeightForWidth())
        self.btnConnectHome.setSizePolicy(sizePolicy3)
        self.btnConnectHome.setMinimumSize(QSize(0, 50))
        self.btnConnectHome.setStyleSheet(u"background-image: url(:/resource/images/icons/home-16.png)")

        self.verticalLayout_9.addWidget(self.btnConnectHome)

        self.btnConnectConfig = QPushButton(self.connectFrame)
        self.btnConnectConfig.setObjectName(u"btnConnectConfig")
        sizePolicy3.setHeightForWidth(self.btnConnectConfig.sizePolicy().hasHeightForWidth())
        self.btnConnectConfig.setSizePolicy(sizePolicy3)
        self.btnConnectConfig.setMinimumSize(QSize(0, 50))
        self.btnConnectConfig.setStyleSheet(u"background-image: url(:/resource/images/icons/config-16.png)")

        self.verticalLayout_9.addWidget(self.btnConnectConfig)

        self.btnConnectLog = QPushButton(self.connectFrame)
        self.btnConnectLog.setObjectName(u"btnConnectLog")
        sizePolicy3.setHeightForWidth(self.btnConnectLog.sizePolicy().hasHeightForWidth())
        self.btnConnectLog.setSizePolicy(sizePolicy3)
        self.btnConnectLog.setMinimumSize(QSize(0, 50))
        self.btnConnectLog.setStyleSheet(u"background-image: url(:/resource/images/icons/log-16.png)")

        self.verticalLayout_9.addWidget(self.btnConnectLog)

        self.btnConnectChange = QPushButton(self.connectFrame)
        self.btnConnectChange.setObjectName(u"btnConnectChange")
        sizePolicy3.setHeightForWidth(self.btnConnectChange.sizePolicy().hasHeightForWidth())
        self.btnConnectChange.setSizePolicy(sizePolicy3)
        self.btnConnectChange.setMinimumSize(QSize(0, 50))
        self.btnConnectChange.setStyleSheet(u"background-image: url(:/resource/images/icons/change-version-16.png)")

        self.verticalLayout_9.addWidget(self.btnConnectChange)

        self.btnConnectUpdate = QPushButton(self.connectFrame)
        self.btnConnectUpdate.setObjectName(u"btnConnectUpdate")
        sizePolicy3.setHeightForWidth(self.btnConnectUpdate.sizePolicy().hasHeightForWidth())
        self.btnConnectUpdate.setSizePolicy(sizePolicy3)
        self.btnConnectUpdate.setMinimumSize(QSize(0, 50))
        self.btnConnectUpdate.setStyleSheet(u"background-image: url(:/resource/images/icons/16_update_version-16.png)")

        self.verticalLayout_9.addWidget(self.btnConnectUpdate)

        self.verticalSpacer = QSpacerItem(50, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.btnConnectRestart = QPushButton(self.connectFrame)
        self.btnConnectRestart.setObjectName(u"btnConnectRestart")
        sizePolicy3.setHeightForWidth(self.btnConnectRestart.sizePolicy().hasHeightForWidth())
        self.btnConnectRestart.setSizePolicy(sizePolicy3)
        self.btnConnectRestart.setMinimumSize(QSize(0, 50))
        self.btnConnectRestart.setMaximumSize(QSize(50, 50))
        self.btnConnectRestart.setStyleSheet(u"background-image: url(:/resource/images/icons/Restart-16.png)")

        self.verticalLayout_9.addWidget(self.btnConnectRestart)

        self.btnConnectStart = QPushButton(self.connectFrame)
        self.btnConnectStart.setObjectName(u"btnConnectStart")
        sizePolicy3.setHeightForWidth(self.btnConnectStart.sizePolicy().hasHeightForWidth())
        self.btnConnectStart.setSizePolicy(sizePolicy3)
        self.btnConnectStart.setMinimumSize(QSize(0, 50))
        self.btnConnectStart.setMaximumSize(QSize(50, 50))
        self.btnConnectStart.setStyleSheet(u"background-image: url(:/resource/images/icons/start-16.png)")

        self.verticalLayout_9.addWidget(self.btnConnectStart)

        self.btnConnectStop = QPushButton(self.connectFrame)
        self.btnConnectStop.setObjectName(u"btnConnectStop")
        self.btnConnectStop.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.btnConnectStop.sizePolicy().hasHeightForWidth())
        self.btnConnectStop.setSizePolicy(sizePolicy3)
        self.btnConnectStop.setMinimumSize(QSize(0, 50))
        self.btnConnectStop.setMaximumSize(QSize(50, 50))
        self.btnConnectStop.setStyleSheet(u"background-image: url(:/resource/images/icons/stop-16.png)")

        self.verticalLayout_9.addWidget(self.btnConnectStop)

        self.menuStackWidget.addWidget(self.connectMenu)
        self.disconnectMenu = QWidget()
        self.disconnectMenu.setObjectName(u"disconnectMenu")
        self.disconnectFrame = QFrame(self.disconnectMenu)
        self.disconnectFrame.setObjectName(u"disconnectFrame")
        self.disconnectFrame.setGeometry(QRect(0, 0, 60, 531))
        self.disconnectFrame.setMinimumSize(QSize(60, 0))
        self.verticalLayout_10 = QVBoxLayout(self.disconnectFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btnDisconnectHome = QPushButton(self.disconnectFrame)
        self.btnDisconnectHome.setObjectName(u"btnDisconnectHome")
        self.btnDisconnectHome.setMinimumSize(QSize(50, 50))
        self.btnDisconnectHome.setStyleSheet(u"background-image: url(:/resource/images/icons/home-16.png)")

        self.verticalLayout_10.addWidget(self.btnDisconnectHome)

        self.btnDisconnectConfig = QPushButton(self.disconnectFrame)
        self.btnDisconnectConfig.setObjectName(u"btnDisconnectConfig")
        self.btnDisconnectConfig.setMinimumSize(QSize(50, 50))
        self.btnDisconnectConfig.setStyleSheet(u"background-image: url(:/resource/images/icons/Connect-16.png)")

        self.verticalLayout_10.addWidget(self.btnDisconnectConfig)

        self.verticalSpacer_2 = QSpacerItem(100, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.menuStackWidget.addWidget(self.disconnectMenu)

        self.verticalLayout_8.addWidget(self.menuStackWidget)


        self.verticalLayout_5.addWidget(self.menuBox)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMinimumSize(QSize(50, 50))
        self.bottomMenu.setMaximumSize(QSize(50, 50))
        self.verticalLayout_6 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnSetting = QPushButton(self.bottomMenu)
        self.btnSetting.setObjectName(u"btnSetting")
        sizePolicy3.setHeightForWidth(self.btnSetting.sizePolicy().hasHeightForWidth())
        self.btnSetting.setSizePolicy(sizePolicy3)
        self.btnSetting.setMinimumSize(QSize(50, 50))
        self.btnSetting.setStyleSheet(u"background-image: url(:/resource/images/icons/setting-16.png)")
        self.btnSetting.setCheckable(False)
        self.btnSetting.setAutoRepeat(False)
        self.btnSetting.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.btnSetting)


        self.verticalLayout_5.addWidget(self.bottomMenu)


        self.verticalLayout_2.addWidget(self.leftMenuFrame)


        self.horizontalLayout.addWidget(self.menu)

        self.extraMenu = QFrame(self.bgApp)
        self.extraMenu.setObjectName(u"extraMenu")
        self.extraMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.extraMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.extraMenu)

        self.content = QFrame(self.bgApp)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(60, 0))
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentTop = QFrame(self.content)
        self.contentTop.setObjectName(u"contentTop")
        self.contentTop.setMinimumSize(QSize(0, 50))
        self.contentTop.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.contentTop)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleFrame = QFrame(self.contentTop)
        self.titleFrame.setObjectName(u"titleFrame")
        self.horizontalLayout_4 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout_2.addWidget(self.titleFrame)

        self.menuButtonFrame = QFrame(self.contentTop)
        self.menuButtonFrame.setObjectName(u"menuButtonFrame")
        self.menuButtonFrame.setMinimumSize(QSize(90, 0))
        self.menuButtonFrame.setMaximumSize(QSize(60, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.menuButtonFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnMin = QPushButton(self.menuButtonFrame)
        self.btnMin.setObjectName(u"btnMin")
        self.btnMin.setMinimumSize(QSize(20, 20))
        self.btnMin.setMaximumSize(QSize(20, 20))
        self.btnMin.setAutoFillBackground(False)
        self.btnMin.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/resource/images/icons/min-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMin.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btnMin)

        self.btnMax = QPushButton(self.menuButtonFrame)
        self.btnMax.setObjectName(u"btnMax")
        self.btnMax.setMinimumSize(QSize(20, 20))
        self.btnMax.setMaximumSize(QSize(20, 20))
        self.btnMax.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/resource/images/icons/max-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMax.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btnMax)

        self.btnClose = QPushButton(self.menuButtonFrame)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(20, 20))
        self.btnClose.setMaximumSize(QSize(20, 20))
        self.btnClose.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/resource/images/icons/close-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btnClose)


        self.horizontalLayout_2.addWidget(self.menuButtonFrame)


        self.verticalLayout_3.addWidget(self.contentTop)

        self.contentFrame = QFrame(self.content)
        self.contentFrame.setObjectName(u"contentFrame")
        self.verticalLayout_11 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.contentFrame)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.verticalLayout_12 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pagesConnect = QWidget()
        self.pagesConnect.setObjectName(u"pagesConnect")
        self.stackedWidget.addWidget(self.pagesConnect)
        self.pagesDisconnect = QWidget()
        self.pagesDisconnect.setObjectName(u"pagesDisconnect")
        self.stackedWidget.addWidget(self.pagesDisconnect)

        self.verticalLayout_12.addWidget(self.stackedWidget)


        self.verticalLayout_11.addWidget(self.pagesContainer)


        self.verticalLayout_3.addWidget(self.contentFrame)


        self.horizontalLayout.addWidget(self.content)


        self.verticalLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.menuStackWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnToggle.setText("")
        self.btnConnectHome.setText("")
        self.btnConnectConfig.setText("")
        self.btnConnectLog.setText("")
        self.btnConnectChange.setText("")
        self.btnConnectUpdate.setText("")
        self.btnConnectRestart.setText("")
        self.btnConnectStart.setText("")
        self.btnConnectStop.setText("")
        self.btnDisconnectHome.setText("")
        self.btnDisconnectConfig.setText("")
        self.btnSetting.setText("")
        self.btnMin.setText("")
        self.btnMax.setText("")
        self.btnClose.setText("")
    # retranslateUi

