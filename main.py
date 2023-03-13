from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from components import titleBar, tab, webPage
from browserUi import Ui_Form
import sys


class BrowserApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(BrowserApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.tabDict = {}
        self.tabId = 0
        self.actTab = 0
        self.tabCount = 0

        self.tBar = titleBar.TitleBar(self)
        self.verticalLayout.addWidget(self.tBar)
        self.addTab()
        self.tBar.tbPushButton_4.clicked.connect(self.addTab)

    def addTab(self):
        try:
            self.tabDict[self.actTab][0].setActive(0)
            self.tabDict[self.actTab][1].hide()
        except:
            pass
        tabB = tab.Tab()
        tabB.setId(self.tabId)
        self.tBar.insertTab(tabB)
        page = webPage.WebPage()
        self.verticalLayout.addWidget(page)

        self.actTab = self.tabId
        self.tabDict[self.tabId] = [tabB, page]
        tabB.clicked.connect(self.selTab)
        tabB.tabPushButton.clicked.connect(self.delTab)
        self.tabId += 1
        self.tabCount += 1

    def selTab(self, tId):
        try:
            self.tabDict[self.actTab][0].setActive(0)
            self.tabDict[self.actTab][1].hide()
        except:
            pass
        self.tabDict[tId][0].setActive(1)
        self.tabDict[tId][1].show()
        self.actTab = tId

    def delTab(self):
        dId = int(self.sender().objectName())
        temp = list(self.tabDict)
        tempId = temp.index(dId)
        lastId = len(temp) - 1
        if self.tabCount > 1:
            if dId == self.actTab:
                if lastId > tempId:
                    sId = temp[tempId + 1]
                else:
                    sId = temp[tempId - 1]
                self.selTab(sId)
            self.tabDict[dId][0].deleteLater()
            self.tabDict[dId][1].deleteLater()
            self.tabDict.pop(dId)
            self.tabCount -= 1
        else:
            sys.exit()
        


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = BrowserApp()
        Form.show()
        sys.exit(app.exec_())
