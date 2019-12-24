# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notGiris.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3

from OgrenciKayit import *

notGirisIslem = DersKayit()

class Ui_Form(object):

    def loadData(self,dersAddi):
        connection = sqlite3.connect("Ogrenciler.db")
        sorgu = "select * from {}".format(dersAddi)
        result = connection.execute(sorgu)
        self.notGirisTablo.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.notGirisTablo.insertRow(row_number)
            for col_number, col_data in enumerate(row_data):
                self.notGirisTablo.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(col_data)))

        connection.close()

    def loadData2(self):
        self.notGiriscomboBox.clear()
        connection = sqlite3.connect("Ogrenciler.db")
        sorgu = "select * from dersler"
        result = connection.execute(sorgu)
        for i in result:
            self.notGiriscomboBox.addItem(i[1])

        connection.close()

    def Secim(self,index):

        print(self.notGiriscomboBox.itemText(index))
        self.loadData(self.notGiriscomboBox.itemText(index))
        self.sinifIsmi = self.notGiriscomboBox.itemText(index)

    def bilgileriGetir(self):

        if self.notGirisTablo.selectionModel().hasSelection():
            row = self.notGirisTablo.currentRow()
            self.notGirisAd.setText(self.notGirisTablo.item(row, 0).text())
            self.notGirisSoyad.setText(self.notGirisTablo.item(row, 1).text())
            self.notGirisNo.setText(self.notGirisTablo.item(row, 2).text())
            self.notGirisVize.setText(self.notGirisTablo.item(row, 3).text())
            self.notGirisFinal.setText(self.notGirisTablo.item(row, 4).text())
            self.notGirisHarfNotu.setText(self.notGirisTablo.item(row, 5).text())
            self.notGirisOrtalama.setText(self.notGirisTablo.item(row, 6).text())

    def notGirr(self):
        vize = self.notGirisVize.text()
        final = self.notGirisFinal.text()
        no = self.notGirisNo.text()
        sinif = self.sinifIsmi

        try:
            notGirisIslem.notGir(no, vize, final, sinif)
            self.loadData(self.sinifIsmi)
            self.Clear()
        except Exception:
            print("ulla")

    def Clear(self):

        self.notGirisSoyad.setText("Form", "Soyad")
        self.notGirisNo.setText("Form", "No")
        self.notGirisVize.setText("Form", "Vize")
        self.notGirisAd.setText("Form", "Ad")
        self.notGirisHarfNotu.setText("Form", "Harf Notu")
        self.notGirisFinal.setText("Form", "Final")
        self.notGirisOrtalama.setText("Form", "Ortalama")

    def setupUi(self, Form):
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(1303, 771)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Downloads/icons8-university-25.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
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
        self.frame.setGeometry(QtCore.QRect(100, 20, 1091, 731))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.notGirisEkle = QtWidgets.QPushButton(self.frame)
        self.notGirisEkle.setGeometry(QtCore.QRect(930, 660, 41, 41))
        self.notGirisEkle.setText("")
        #930, 660, 41, 41
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images2/icons8-plus-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notGirisEkle.setIcon(icon1)
        self.notGirisEkle.setIconSize(QtCore.QSize(20, 20))
        self.notGirisEkle.setObjectName("notGirisEkle")
        self.notGirisSil = QtWidgets.QPushButton(self.frame)
        self.notGirisSil.setGeometry(QtCore.QRect(870, 660, 41, 41))
        self.notGirisSil.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images2/icons8-delete-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notGirisSil.setIcon(icon2)
        self.notGirisSil.setIconSize(QtCore.QSize(20, 20))
        self.notGirisSil.setObjectName("notGirisSil")

        self.notGirisGunc = QtWidgets.QPushButton(self.frame)
        self.notGirisGunc.setGeometry(QtCore.QRect(810, 660, 41, 41))
        self.notGirisGunc.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images2/icons8-update-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notGirisGunc.setIcon(icon3)
        self.notGirisGunc.setIconSize(QtCore.QSize(20, 20))
        self.notGirisGunc.setObjectName("notGirisGunc")


        self.notGirisGetir = QtWidgets.QPushButton(self.frame)
        self.notGirisGetir.setGeometry(QtCore.QRect(750, 660, 41, 41))
        self.notGirisGetir.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images2/icons8-syllabus-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notGirisGetir.setIcon(icon3)
        self.notGirisGetir.setIconSize(QtCore.QSize(20, 20))
        self.notGirisGetir.setObjectName("notGirisGunc")

        self.notGiriscomboBox = QtWidgets.QComboBox(self.frame)
        self.notGiriscomboBox.setGeometry(QtCore.QRect(110, 20, 131, 21))
        self.notGiriscomboBox.setCurrentText("")
        self.notGiriscomboBox.setObjectName("notGiriscomboBox")
        self.notGirisTablo = QtWidgets.QTableWidget(self.frame)
        self.notGirisTablo.setGeometry(QtCore.QRect(110, 60, 881, 241))
        self.notGirisTablo.setColumnCount(7)
        self.notGirisTablo.setObjectName("notGirisTablo")
        self.notGirisTablo.setRowCount(0)
        self.notGirisSoyad = QtWidgets.QLineEdit(self.frame)
        self.notGirisSoyad.setGeometry(QtCore.QRect(120, 380, 211, 22))
        self.notGirisSoyad.setInputMask("")
        self.notGirisSoyad.setText("")
        self.notGirisSoyad.setObjectName("notGirisSoyad")
        self.notGirisNo = QtWidgets.QLineEdit(self.frame)
        self.notGirisNo.setGeometry(QtCore.QRect(120, 440, 211, 22))
        self.notGirisNo.setInputMask("")
        self.notGirisNo.setText("")
        self.notGirisNo.setObjectName("notGirisNo")
        self.notGirisVize = QtWidgets.QLineEdit(self.frame)
        self.notGirisVize.setGeometry(QtCore.QRect(120, 500, 211, 22))
        self.notGirisVize.setInputMask("")
        self.notGirisVize.setText("")
        self.notGirisVize.setObjectName("notGirisVize")
        self.notGirisAd = QtWidgets.QLineEdit(self.frame)
        self.notGirisAd.setGeometry(QtCore.QRect(120, 320, 211, 22))
        self.notGirisAd.setInputMask("")
        self.notGirisAd.setText("")
        self.notGirisAd.setObjectName("notGirisAd")
        self.notGirisHarfNotu = QtWidgets.QLineEdit(self.frame)
        self.notGirisHarfNotu.setGeometry(QtCore.QRect(120, 630, 211, 22))
        self.notGirisHarfNotu.setInputMask("")
        self.notGirisHarfNotu.setText("")
        self.notGirisHarfNotu.setObjectName("notGirisHarfNotu")
        self.notGirisFinal = QtWidgets.QLineEdit(self.frame)
        self.notGirisFinal.setGeometry(QtCore.QRect(120, 570, 211, 22))
        self.notGirisFinal.setInputMask("")
        self.notGirisFinal.setText("")
        self.notGirisFinal.setObjectName("notGirisFinal")
        self.notGirisOrtalama = QtWidgets.QLineEdit(self.frame)
        self.notGirisOrtalama.setGeometry(QtCore.QRect(120, 680, 211, 22))
        self.notGirisOrtalama.setInputMask("")
        self.notGirisOrtalama.setText("")
        self.notGirisOrtalama.setObjectName("notGirisOrtalama")

        self.CikisB = QtWidgets.QPushButton(Form)
        self.CikisB.setGeometry(QtCore.QRect(1255, 4, 41, 41))
        self.CikisB.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images2/icons8-exit-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CikisB.setIcon(icon4)
        self.CikisB.setIconSize(QtCore.QSize(20, 20))
        self.CikisB.setObjectName("OgrenciCikisB")
        self.CikisB.setStyleSheet("""QPushButton:hover
        {
          border-radius:15px;
          background:rgba(255, 0, 0, 0.4);


        }""")

        self.notGiriscomboBox.activated.connect(self.Secim)
        self.notGirisGetir.clicked.connect(self.bilgileriGetir)
        self.notGirisEkle.clicked.connect(self.notGirr)
        self.CikisB.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.notGirisSoyad.setPlaceholderText(_translate("Form", "Soyad"))
        self.notGirisNo.setPlaceholderText(_translate("Form", "No"))
        self.notGirisVize.setPlaceholderText(_translate("Form", "Vize"))
        self.notGirisAd.setPlaceholderText(_translate("Form", "Ad"))
        self.notGirisHarfNotu.setPlaceholderText(_translate("Form", "Harf Notu"))
        self.notGirisFinal.setPlaceholderText(_translate("Form", "Final"))
        self.notGirisOrtalama.setPlaceholderText(_translate("Form", "Ortalama"))
        self.loadData2()
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
