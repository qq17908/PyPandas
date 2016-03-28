# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QWidget

#-------------------------------------------------------------------------
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.myButton = QtGui.QPushButton(self)
        self.myButton.setObjectName(_fromUtf8("myButton"))
        self.myButton.setText(_fromUtf8("点击"))
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        reply = QMessageBox.information(self,_fromUtf8("标题"),_fromUtf8("消息"),QMessageBox.Yes | QMessageBox.No)

if __name__=="__main__":  
    import sys  
  
    app=QtGui.QApplication(sys.argv)  
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())
    print "ok,finish!"
