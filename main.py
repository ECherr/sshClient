#!/usr/bin/python3

import sys, os

from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96"

widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        # UI 转换后的类
        self.ui = Ui_MainWindow()
        
        # 将类捆绑到自定义的widgets上?
        global widgets
        widgets = self.ui
        
        # 设置 title 以及 description
        title = "xxxx"
        # description = "xxxxxx"
        self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)
        
        # toggle menu
        # 将展开按钮的点击事件连接到处理函数
        # widgets.btnToggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        
        # UI DEFINITIONS
        UIFunctions.uiDefinitions(self)
        
        # QTableWidget PARAMETERS
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # BUTTON CLICK
        # widgets.btnHome.clicked.connect(self.buttonClick)
        # xxx 
        
        # EXTRA LEFT BOX
        # def openCloseLeftBox():
        #     UIFunctions.toggleLeftBox(self, True)
        # widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        # widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        
        # EXTRAT RIGHT BOX
        
        # SHOW APP
        self.show()
        
        # SET CUSTOM THEME
        useCustomTheme = False
        themeFile = "theme/py_dracula_light.qss"
        
        # SET THEME AND HACKS
        if useCustomTheme:
            UIFunctions.theme(self, themeFile, True)
            
            # SET HACKS
            AppFunctions.setThemeHack(self)
            
        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.setStyleSheet()))
        
    
    # BUTTON CLICK
    # Post here your function for clicked buttons
    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            
            
            
    # RESIZE EVENTS
    def resizeEvent(self, event):
        # SET DRAG POS WINDOWS
        self.dragPos = event.globalPos()
        
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Left Click')
        if event.buttons() == Qt.RightButton:
            print('Right Click')
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon())
    window = MainWindow()
    sys.exit(app.exec())
    