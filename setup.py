# coding=utf-8

#the software itself is made by royenheart
#the contents of the web are created by MONSTER-SIREN/HYPERGRYPH
#using PyQt5
#Arknights Forever

import sys
sys.path.append(r'./src')
from controller import *
from PyQt5.QtCore import (Qt,QUrl)
from PyQt5.QtGui import (QIcon)
from PyQt5.QtWidgets import (QApplication,QMainWindow)

class MainDemo(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 窗口设置
        self.setWindowTitle('MONSTER-SIREN')
        self.setWindowIcon(QIcon('img/web.ico'))
        self.resize(1200, 800)
        # 打开窗口
        self.show()
        # 调用函数打开网页
        self.open_web(WebView(self),QUrl('https://monster-siren.hypergryph.com/'))
        # 历史列表
        self.hisWeb = []

    # 按键对应操作
    def keyPressEvent(self, event):
        whatkey = event.key()
        if whatkey == Qt.Key_F11: # 全屏
            if self.isFullScreen() == False:
                self.showFullScreen()
            else:
                self.showNormal()
            self.show()
        elif whatkey == Qt.Key_Q: # 退出
            if self.isFullScreen() == True:
                self.showNormal()
                self.show()
            else:
                self.close()
        elif whatkey == Qt.Key_R: # 重载
            self.browser.load(QUrl('https://monster-siren.hypergryph.com/'))

    # 网页打开
    def open_web(self, webob, qurl=QUrl('')):
        # 设置浏览器
        self.browser = webob
        self.browser.load(qurl)
        # 设置中心窗口
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    # 创建QApplication类的实例
    my_application = QApplication(sys.argv)
    # 创建QWebEngineView类实例
    main_siren = MainDemo()
    my_application.exec_()


