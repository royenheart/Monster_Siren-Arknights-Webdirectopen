# coding=utf-8

#the software itself is made by royenheart
#the contents of the web are created by MONSTER-SIREN/HYPERGRYPH
#using PyQt5
#Arknights Forever

import sys
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

    # 重写creatwindow
    def createWindow(self, webWindowType):
        new_webview = WebView(self.father)
        self.father.open_web(new_webview,QUrl('https://monster-siren.hypergryph.com/'))
        return new_webview

    # 设置自定义菜单
    def right_menushow(self):
        rightmenu = QMenu(self)
        rightmenu.font()
        # 关闭窗口选项
        self.actionA = QAction(QIcon('img/close.ico'),'CLOSE')
        self.actionA.setObjectName("func1")
        self.actionA.triggered.connect(lambda :self.father.close())
        # 全屏选项
        self.actionB = QAction(QIcon('img/fullsc.ico'),'FULLSCREEN')
        self.actionB.setObjectName("func2")
        self.actionB.triggered.connect(self.funcB)
        # 重载窗口选项
        self.actionC = QAction(QIcon('img/reload.ico'),'RELOAD')
        self.actionC.setObjectName("func3")
        self.actionC.triggered.connect(self.funcC)
        rightmenu.addAction(self.actionA)
        rightmenu.addAction(self.actionB)
        rightmenu.addAction(self.actionC)
        rightmenu.exec_(QCursor.pos())

    def funcB(self):
        if self.father.isFullScreen() == False:
            self.father.showFullScreen()
        else:
            self.father.showNormal()
        self.father.show()

    def funcC(self):
        self.father.open_web(WebView(self.father),QUrl('https://monster-siren.hypergryph.com/'))

class MainDemo(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗口设置
        self.setWindowTitle('MONSTER-SIREN')
        self.setWindowIcon(QIcon('img/web.ico'))
        self.resize(1200, 800)
        self.show()
        # 调用函数打开网页
        self.open_web(WebView(self),QUrl('https://monster-siren.hypergryph.com/'))

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
    def open_web(self, webob, qurl=QUrl('')):
        # 设置浏览器
        self.browser = webob
        self.browser.load(qurl)
        # 设置中心窗口
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    my_application = QApplication(sys.argv)  # 创建QApplication类的实例
    main_siren = MainDemo()
    main_siren.show()
    my_application.exec_()


