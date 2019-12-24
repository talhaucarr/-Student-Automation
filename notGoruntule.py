# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notGoruntule.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from OgrenciKayit import *

ogrenciIslem = OgrenciKontrol()

class Ui_Form(object):

    def cikis(self):
        pass

    def dosyaOku(self):
        dosyaOku = open("OgrenciNotemp.txt", "r")
        self.noTemp = dosyaOku.read()

    def loadData3(self,dersAddi):
        connection = sqlite3.connect("Ogrenciler.db")
        sorgu = "select * from {}".format(dersAddi)
        result = connection.execute(sorgu)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for col_number, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(col_data)))

        connection.close()

    def loadData2(self):
        self.comboBox.clear()

        temp = ogrenciIslem.sinifNott()

        for i in temp:

            self.comboBox.addItem(i)

    def Secim(self,index):

        self.loadData3(self.comboBox.itemText(index))
        self.sinifIsmi = self.comboBox.itemText(index)

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
"color:white;\n"
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
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 40, 711, 681))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(40, 70, 631, 591))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(50, 20, 151, 21))
        self.comboBox.setObjectName("comboBox")
        self.cikisB = QtWidgets.QPushButton(Form)
        self.cikisB.setGeometry(QtCore.QRect(730, 5, 31, 31))
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

        self.comboBox.activated.connect(self.Secim)
        self.cikisB.clicked.connect(Form.close)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loadData2()
        self.dosyaOku()
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
