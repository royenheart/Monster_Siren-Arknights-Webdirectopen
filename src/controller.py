# 声明相关类的性质及操作

from PyQt5.QtCore import (Qt,QUrl)
from PyQt5.QtWidgets import (QMenu,QAction)
from PyQt5.QtGui import (QIcon,QCursor)
from PyQt5.QtWebEngineWidgets import (QWebEngineView)

# qss加载相关类
class QssLoad:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()

class WebView(QWebEngineView):
    def __init__(self, parent):
        super().__init__(parent)
        # 设置自定义菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.right_menushow)
        # 标记父类
        self.father = parent

    # 重写creatwindow
    def createWindow(self, webWindowType):
        # 添加历史记录
        self.father.hisWeb.append(self.father.browser.url())
        # 创建新WebView对象
        new_webview = WebView(self.father)
        self.father.open_web(new_webview,QUrl(new_webview.url()))
        # 返回新的窗口
        return self.father.browser

    # 设置自定义菜单
    def right_menushow(self):
        # 创建对象
        rightmenu = QMenu(self)
        # 加载外部qss样式表
        styleFile = "./src/rightmenu.qss"
        qssStyle = QssLoad.readQss(styleFile)
        rightmenu.setStyleSheet(qssStyle)
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
        # 更多音乐（游戏内未被正式上传文件）
        self.actionD = QAction(QIcon('img/more.ico'), 'MORE')
        self.actionD.setObjectName("func4")
        self.actionD.triggered.connect(self.funcD)
        # 返回选项（上一个网页）
        self.actionE = QAction(QIcon('img/back.ico'),'BACK')
        self.actionE.setObjectName("func5")
        self.actionE.triggered.connect(self.funcE)
        # 添加选项
        rightmenu.addAction(self.actionA)
        rightmenu.addAction(self.actionB)
        rightmenu.addAction(self.actionC)
        rightmenu.addAction(self.actionD)
        rightmenu.addAction(self.actionE)
        # 菜单栏显示于鼠标处
        rightmenu.exec_(QCursor.pos())

    def funcB(self):
        if self.father.isFullScreen() == False:
            self.father.showFullScreen()
        else:
            self.father.showNormal()
        self.father.show()

    # 重载窗口函数
    def funcC(self):
        self.father.open_web(self.father.browser,QUrl('https://monster-siren.hypergryph.com/'))

    # 更多音乐
    def funcD(self):
        self.father.hisWeb.append(self.father.browser.url())
        self.father.open_web(self.father.browser, QUrl('http://akmsc.royenheart.com'))

    # 返回上一个打开的窗口
    def funcE(self):
        if len(self.father.hisWeb) >= 1:
            self.father.open_web(self.father.browser, self.father.hisWeb.pop())
        else:
            self.father.open_web(self.father.browser, QUrl('https://monster-siren.hypergryph.com/'))


