#coding:utf-8

import sys
from PyQt4 import QtGui,QtCore

class MyWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setFixedSize(200,120)
        self.quit = QtGui.QPushButton("Close",self)
        self.quit.setGeometry(62,40,75,30)
        self.quit.setFont(QtGui.QFont("Times",18,QtGui.QFont.Bold))
        self.connect(self.quit, QtCore.SIGNAL("clicked()"),QtGui.qApp,QtCore.SLOT("quit()"))
        
app = QtGui.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())