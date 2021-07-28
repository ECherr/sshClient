#!/usr/bin/python3

import sys, os

from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96"

widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        # 设置为全局的 widgets
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        
        # 自定义标题
        Settings.ENABLE_CUSTOM_TITLE_BAR =True
        
        # 设置标题
        title = "XXX - XXX"
        self.setWindowTitle(title)
        
        # 隐藏菜单
        widgets.btnToggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        
        UIFunctions.uiDefinitions(self)
        
        # 连接按钮函数
        widgets.btnDisconnectHome.clicked.connect(self.buttonClick)
        widgets.btnDisconnectConfig.clicked.connect(self.buttonClick)
        widgets.btnConnectHome.clicked.connect(self.buttonClick)
        widgets.btnConnectConfig.clicked.connect(self.buttonClick)
        widgets.btnConnectLog.clicked.connect(self.buttonClick)
        widgets.btnConnectChange.clicked.connect(self.buttonClick)
        widgets.btnConnectUpdate.clicked.connect(self.buttonClick)
        widgets.btnConnectRestart.clicked.connect(self.buttonClick)
        widgets.btnConnectStart.clicked.connect(self.buttonClick)
        widgets.btnConnectStop.clicked.connect(self.buttonClick)
        
        self.show()
        
        useCustomTheme = False
        themeFile = r"resource\themes\py_dracula_light.qss"
        
        if useCustomTheme:
            UIFunctions.theme(self, themeFile, True)
            
            # Set Hacks
            AppFunctions.setThemeHack(self)
        
        
    # 按钮点击事件函数
    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        
        # Home Page(disconnect)
        if btnName == "btnDisconnectHome":
            print("btnDisconnectHome clicked!")
        
        # Config Page(disconnect)
        if btnName == "btnDisconnectConfig":
            print("btnDisconnectConfig clicked!")
            
        # Home Page(connect)
        if btnName == "btnConnectHome":
            # widgets.stackedWidget.setCurrentWidget(widgets.pagesConnect)
            # UIFunctions.resetStyle(self.btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            print("btnConnectHome clicked!")
            
        # Config Page(connect)
        if btnName == "btnConnectConfig":
            print("btnConnectConfig clicked!")
            
        # Log Page(connect)
        if btnName == "btnConnectLog":
            print("btnConnectLog clicked!")
            
        # Handover Page(connect)
        if btnName == "btnConnectChange":
            print("btnConnectChange clicked!")
            
        # Update Page(connect)
        if btnName == "btnConnectUpdate":
            print("btnConnectUpdate clicked!")
            
        # Restart
        if btnName == "btnConnectRestart":
            print("btnConnectRestart clicked!")
            
        # Start
        if btnName == "btnConnectStart":
            print("btnConnectStart clicked")
            
        # Stop
        if btnName == "btnConnectStop":
            print("btnConnectStop clicked!")
            
        print(f'Button "{btnName}" pressed!')
        
    # Mouse Click Events
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
        if event.buttons() == Qt.LeftButton:
            print("Mouse Click: LEFT CLICK")
        if event.buttons() == Qt.RightButton:
            print("Mouse Click: RIGHT CLICK")
        # if event.button(
    
    # Resize Events
    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)
        
    
        
        
        
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon())
    window = MainWindow()
    sys.exit(app.exec())
    