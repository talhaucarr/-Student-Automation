# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transKript.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
from OgrenciKayit import *

ogrenciIslem = OgrenciKontrol()
class Ui_Form(object):

    def transKriptYaz(self):
        pass
        #self.textEdit.setText(ogrenciIslem.transKript())

    def setupUi(self, Form):
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(771, 762)
        Form.setStyleSheet(" *{\n"
"font-family:century gothic;\n"
"font-size:16px;\n"
"}\n"
"#Form{\n"
"    background:url(:/images2/taslar.jpg);\n"
"}\n"
"QFrame{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton{\n"
"background:rgba(194,175,161,0.5);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"color:black;\n"
"border-radius:15px;\n"
"background:rgb(194,175,161);\n"
"}\n"
"QTableWidget{\n"
"Background-color:rgba(0,0,0,0.5);border-radius:14px;\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid white;\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"background:transparent\n"
"}\n"
"QComboBox{\n"
"color:white;\n"
"background:rgba(194,175,161,0.5);\n"
"}"
"QTextEdit{\n"
"color:white;\n"
"Background-color:rgba(0,0,0,0.5);border-radius:14px;\n"
"}\n"
                           )
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 50, 711, 681))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(30, 30, 651, 631))
        self.textEdit.setObjectName("textEdit")
        self.cikisB = QtWidgets.QPushButton(Form)
        self.cikisB.setGeometry(QtCore.QRect(730, 10, 31, 31))
        self.cikisB.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images2/icons8-exit-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cikisB.setIcon(icon)
        self.cikisB.setObjectName("cikisB")
        self.cikisB.setStyleSheet("""QPushButton:hover
        {
          border-radius:15px;
          background:rgba(255, 0, 0, 0.4);


        }""")

        self.cikisB.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        ogrenciIslem.transKript()
        self.transKriptYaz()
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
