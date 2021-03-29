# coding=utf-8

#the software itself is made by royenheart
#the contents of the web are created by MONSTER-SIREN/HYPERGRYPH
#using PyQt5
#Arknights Forever

import sys,os
from PyQt5.QtCore import (Qt,QUrl,QRect,QPoint)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class WebView(QWebEngineView):
    def __init__(self, parent):
        super().__init__(parent)
        # 设置自定义菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.right_menushow)
        self.father = parent

    def createWindow(self, webWindowType):
        return main_siren.browser

    def right_menushow(self):
        rightmenu = QMenu(self)
        self.actionA = QAction(QIcon('img/close.ico'),'CLOSE')
        self.actionA.setObjectName("func1")
        self.actionA.triggered.connect(lambda :self.father.close())
        self.actionB = QAction(QIcon('img/fullsc.ico'),'FULLSCREEN')
        self.actionB.setObjectName("func2")
        self.actionB.triggered.connect(self.funcB)
        rightmenu.addAction(self.actionA)
        rightmenu.addAction(self.actionB)
        rightmenu.exec_(QCursor.pos())

    def funcB(self):
        if self.father.isFullScreen() == False:
            self.father.showFullScreen()
        else:
            self.father.showNormal()
        self.father.show()

class MainDemo(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗口设置
        self.setWindowTitle('MONSTER-SIREN')
        self.setWindowIcon(QIcon('img/web.ico'))
        self.resize(1200, 800)
        self.show()
        # 调用函数打开网页
        self.open_tab(QUrl('https://monster-siren.hypergryph.com/'))
        self.setCentralWidget(self.browser)

    # 按键对应操作
    def keyPressEvent(self, event):
        whatkey = event.key()
        if whatkey == Qt.Key_F11:
            if self.isFullScreen() == False:
                self.showFullScreen()
            else:
                self.showNormal()
            self.show()
        elif whatkey == Qt.Key_Q:
            if self.isFullScreen() == True:
                self.showNormal()
                self.show()
            else:
                self.close()

    # 网页打开
    def open_tab(self, qurl=QUrl('')):
        # 设置浏览器
        self.browser = WebView(self)
        self.browser.load(qurl)


if __name__ == '__main__':
    my_application = QApplication(sys.argv)  # 创建QApplication类的实例
    main_siren = MainDemo()
    main_siren.show()
    my_application.exec_()


