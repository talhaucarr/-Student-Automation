# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dersKayit.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from OgrenciKayit import *

dersIslem = DersKayit()


class Ui_Form(object):

    def ranndom(self):

        return random.randint(1000,10000)

    def loadData(self):
        """connection = sqlite3.connect("Ogrenciler.db")
        sorgu = "select * from dersler"
        result = connection.execute(sorgu)"""

        ths = open("OgretmenTemp.txt", "r")

        self.a = ths.read()
        ths.close()

        result = dersIslem.dersYayinla(self.a)


        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for col_number, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(col_data)))

        #connection.close()

    def dersEkleQ(self):

        dersAdi = self.dersAdi.text()
        dersSaati = self.dersSaati.text()
        dersKredi = self.dersKredi.text()
        vize = self.dersVize.text()
        final = self.dersFinal.text()
        dersSinif = self.dersSinif.text()
        dersOgr = self.a

        try:
            yeni_ders = Ders(self.ranndom(), dersAdi.capitalize(), dersSaati, dersKredi, vize, final,dersOgr , dersSinif)
            dersIslem.dersEkle(yeni_ders)
            self.label_9.setText("Ders Başarıyla Eklendi!")
            self.Temizle2()
            self.loadData()
        except Exception:
            print("ulaa")

    def dersSilQ(self):
        try:
            dersIslem.dersSil(self.tutucu)
            self.label_9.setText("Ders Başarıyla Silindi!")
            self.Temizle2()
            self.loadData()
        except Exception:
            print("ulaa")

    def dersGunc(self):

        dersAdi = self.dersAdi.text()
        dersSaati = self.dersSaati.text()
        dersKredi = self.dersKredi.text()
        vize = self.dersVize.text()
        final = self.dersFinal.text()
        dersSinif = self.dersSinif.text()
        dersOgr = self.dersOgretmen.text()
        try:
            gunclle= Ders(self.tutucu,dersAdi.capitalize(), dersSaati, dersKredi, vize, final, dersOgr.capitalize(),dersSinif)
            dersIslem.dersGuncelle(gunclle)
            self.label_9.setText("Ders Başarıyla Güncellendi!")
            self.Temizle2()
            self.loadData()
        except Exception:
            print("ulaa")

    def dersGetir(self):
        if self.tableWidget.selectionModel().hasSelection():
            row = self.tableWidget.currentRow()
            self.tutucu = self.tableWidget.item(row, 0).text()
            self.dersAdi.setText(self.tableWidget.item(row, 1).text())
            self.dersSaati.setText(self.tableWidget.item(row, 2).text())
            self.dersKredi.setText(self.tableWidget.item(row, 3).text())
            self.dersVize.setText(self.tableWidget.item(row, 4).text())
            self.dersFinal.setText(self.tableWidget.item(row, 5).text())
            #self.dersOgretmen.setText(self.tableWidget.item(row, 6).text())
            self.dersSinif.setText(self.tableWidget.item(row, 7).text())

    def Temizle2(self):

        self.dersAdi.setText("")
        self.dersSaati.setText("")
        self.dersKredi.setText("")
        self.dersVize.setText("")
        self.dersFinal.setText("")
        self.dersSinif.setText("")



    def setupUi(self, Form):
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(1460, 900)
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
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 20, 1381, 851))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dersEkleB = QtWidgets.QPushButton(self.frame)
        self.dersEkleB.setGeometry(QtCore.QRect(1270, 640, 41, 41))
        self.dersEkleB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images2/icons8-plus-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dersEkleB.setIcon(icon1)
        self.dersEkleB.setIconSize(QtCore.QSize(20, 20))
        self.dersEkleB.setObjectName("dersEkleB")

        self.dersGetirB = QtWidgets.QPushButton(self.frame)
        self.dersGetirB.setGeometry(QtCore.QRect(1090, 640, 41, 41))
        self.dersGetirB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images2/icons8-syllabus-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dersGetirB.setIcon(icon1)
        self.dersGetirB.setIconSize(QtCore.QSize(20, 20))
        self.dersGetirB.setObjectName("dersEkleB")

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(420, 50, 901, 571))
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.dersAdi = QtWidgets.QLineEdit(self.frame)
        self.dersAdi.setGeometry(QtCore.QRect(30, 100, 361, 22))
        self.dersAdi.setInputMask("")
        self.dersAdi.setText("")
        self.dersAdi.setObjectName("dersAdi")
        self.dersSaati = QtWidgets.QLineEdit(self.frame)
        self.dersSaati.setGeometry(QtCore.QRect(30, 210, 361, 22))
        self.dersSaati.setInputMask("")
        self.dersSaati.setText("")
        self.dersSaati.setObjectName("dersSaati")
        self.dersKredi = QtWidgets.QLineEdit(self.frame)
        self.dersKredi.setGeometry(QtCore.QRect(30, 310, 361, 22))
        self.dersKredi.setInputMask("")
        self.dersKredi.setText("")
        self.dersKredi.setObjectName("dersKredi")
        self.dersVize = QtWidgets.QLineEdit(self.frame)
        self.dersVize.setGeometry(QtCore.QRect(30, 410, 361, 22))
        self.dersVize.setInputMask("")
        self.dersVize.setText("")
        self.dersVize.setObjectName("dersVize")
        self.dersFinal = QtWidgets.QLineEdit(self.frame)
        self.dersFinal.setGeometry(QtCore.QRect(30, 510, 361, 22))
        self.dersFinal.setInputMask("")
        self.dersFinal.setText("")
        self.dersFinal.setObjectName("dersFinal")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 50, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 380, 111, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 470, 111, 21))
        self.label_5.setObjectName("label_5")
        self.dersEkleSil = QtWidgets.QPushButton(self.frame)
        self.dersEkleSil.setGeometry(QtCore.QRect(1210, 640, 41, 41))
        self.dersEkleSil.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images2/icons8-delete-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dersEkleSil.setIcon(icon2)
        self.dersEkleSil.setIconSize(QtCore.QSize(20, 20))
        self.dersEkleSil.setObjectName("dersEkleSil")
        self.dersGuncB = QtWidgets.QPushButton(self.frame)
        self.dersGuncB.setGeometry(QtCore.QRect(1150, 640, 41, 41))
        self.dersGuncB.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images2/icons8-update-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dersGuncB.setIcon(icon3)
        self.dersGuncB.setIconSize(QtCore.QSize(20, 20))
        self.dersGuncB.setObjectName("dersGuncB")

        self.dersSinif = QtWidgets.QLineEdit(self.frame)
        self.dersSinif.setGeometry(QtCore.QRect(30, 600, 361, 22))
        self.dersSinif.setInputMask("")
        self.dersSinif.setText("")
        self.dersSinif.setObjectName("dersSinif")

        """self.dersOgretmen = QtWidgets.QLineEdit(self.frame)
        self.dersOgretmen.setGeometry(QtCore.QRect(30, 600, 361, 22))
        self.dersOgretmen.setInputMask("")
        self.dersOgretmen.setText("")
        self.dersOgretmen.setObjectName("dersOgretmen")"""

        """self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 570, 111, 21))
        self.label_7.setObjectName("label_7")"""

        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 570, 111, 21))
        self.label_6.setObjectName("label_6")

        self.CikisB = QtWidgets.QPushButton(Form)
        self.CikisB.setGeometry(QtCore.QRect(1414, 4, 41, 41))
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

        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(33, 640, 200, 50))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("""
                QLabel{
                color:red;
                }
                """)

        self.dersEkleB.clicked.connect(self.dersEkleQ)
        self.dersEkleSil.clicked.connect(self.dersSilQ)
        self.dersGuncB.clicked.connect(self.dersGunc)
        self.dersGetirB.clicked.connect(self.dersGetir)
        self.CikisB.clicked.connect(Form.close)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dersAdi.setPlaceholderText(_translate("Form", "Ders Adı"))
        self.dersSaati.setPlaceholderText(_translate("Form", "Ders Saati"))
        self.dersKredi.setPlaceholderText(_translate("Form", "Ders Kredi"))
        self.dersVize.setPlaceholderText(_translate("Form", "Vize Ağırlık"))
        self.dersFinal.setPlaceholderText(_translate("Form", "Final Ağırlık"))
        #self.dersOgretmen.setPlaceholderText(_translate("Form", "Öğretmen"))
        self.label.setText(_translate("Form", "Ders Adı"))
        self.label_2.setText(_translate("Form", "Ders Saati"))
        self.label_3.setText(_translate("Form", "Ders Kredi"))
        self.label_4.setText(_translate("Form", "Vize Ağırlık"))
        self.label_5.setText(_translate("Form", "Final Ağırlık"))
        self.dersSinif.setPlaceholderText(_translate("Form", "Sınıf"))
        self.label_6.setText(_translate("Form", "Açıldığı Sınıf"))
        self.label_9.setText(_translate("Form", ""))
        #self.label_7.setText(_translate("Form", "Öğretmeni"))
        self.loadData()
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
