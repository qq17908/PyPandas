# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QWidget
  
class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.myButton = QtGui.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        reply = QMessageBox.information(self,                         #使用infomation信息框
                                    "标题",
                                    "消息",
                                    QMessageBox.Yes | QMessageBox.No)

if __name__=="__main__":  
    import sys  
  
    app=QtGui.QApplication(sys.argv)  
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())      