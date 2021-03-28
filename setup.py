#the software itself is made by royenheart
#the contents of the web are created by MONSTER-SIREN/HYPERGRYPH
#using PyQt5
#Arknights Forever

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class WebView(QWebEngineView):
    def __init__(self, parent):
        super().__init__(parent)

    def createWindow(self, webWindowType):
        return main_demo.browser


class MainDemo(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('MONSTER-SIREN')
        self.setWindowIcon(QIcon('web.ico'))
        self.resize(1200, 800)
        self.show()
        # 调用函数打开网页
        self.open_tab(QUrl('https://monster-siren.hypergryph.com/'))
        self.setCentralWidget(self.browser)


    # 网页打开
    def open_tab(self, qurl=QUrl('')):
        # 设置浏览器
        self.browser = WebView(self)
        self.browser.load(qurl)

def full():
    main_demo.showFullScreen()

if __name__ == '__main__':
    my_application = QApplication(sys.argv)  # 创建QApplication类的实例
    main_demo = MainDemo()
    main_demo.show()
    my_application.exec_()

