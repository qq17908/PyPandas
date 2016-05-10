#coding:utf-8

import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "stockframe.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
     
    def butClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + 'ok!')
    
    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, '输入', '输入姓名')
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())