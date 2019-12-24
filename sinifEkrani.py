# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sinifEkrani.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from OgrenciKayit import *

sinifIslem = SinifKayit()

class Ui_Form(object):



    def loadData3(self,dersAddi):
        connection = sqlite3.connect("Ogrenciler.db")
        sorgu = "select * from {}".format(dersAddi)
        result = connection.execute(sorgu)
        self.sinifGirisTabloBuyuk.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.sinifGirisTabloBuyuk.insertRow(row_number)
            for col_number, col_data in enumerate(row_data):
                self.sinifGirisTabloBuyuk.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(col_data)))

        connection.close()

    def loadData2(self):
        self.sinifGiriscomboBox.clear()
        connection = sqlite3.connect("Ogrenciler.db")
        sorgu = "select * from dersler"
        result = connection.execute(sorgu)
        for i in result:
            self.sinifGiriscomboBox.addItem(i[1])

        #connection.close()

    def Secim(self,index):

        print(self.sinifGiriscomboBox.itemText(index))
        self.loadData3(self.sinifGiriscomboBox.itemText(index))
        self.sinifIsmi = self.sinifGiriscomboBox.itemText(index)

    def ranndom(self):

        return random.randint(1000,10000)

    def loadData(self):
        connection = sqlite3.connect("Ogrenciler.db")
        sorgu = "select * from siniflar"
        result = connection.execute(sorgu)
        self.sinifGiristablo.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.sinifGiristablo.insertRow(row_number)
            for col_number, col_data in enumerate(row_data):
                self.sinifGiristablo.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(col_data)))

        connection.close()

    def sinifEkleQ(self):
        sinifADi = self.sinifGirisSinifAdi.text()
        sinifNo = self.ranndom()

        try:
            yeni_sinif=Sinif(sinifADi.upper(),sinifNo)
            sinifIslem.sinifEkle(yeni_sinif)
            self.label_9.setText("Sınıf Başarıyla Eklendi!")
            self.loadData()
            self.sinifGirisSinifAdi.setText("")
        except Exception:
            print("ulaa")

    def sinifSilQ(self):

        sinifAdi = self.sinifGirisSinifAdi.text()
        try:
            sinifIslem.sinifSil(sinifAdi)
            self.label_9.setText("Sınıf Başarıyla Silindi!")
            self.loadData()
            self.sinifGirisSinifAdi.setText("")
        except Exception:
            print("ulaa")

    def sinifGunc(self):
        sinifADi = self.sinifGirisSinifAdi.text()
        try:
            sinifIslem.sinifGuncelle(sinifADi,self.temp)
            self.label_9.setText("Sınıf Başarıyla Güncellendi!")
            self.loadData()
            self.sinifGirisSinifAdi.setText("")
        except Exception:
            print("ulaa")

    def sinifGetirr(self):
        if self.sinifGiristablo.selectionModel().hasSelection():
            row = self.sinifGiristablo.currentRow()
            self.sinifGirisSinifAdi.setText(self.sinifGiristablo.item(row, 0).text())
            self.temp = self.sinifGiristablo.item(row, 1).text()

    def setupUi(self, Form):
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(1303, 769)
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

        self.sinifGirisEkle = QtWidgets.QPushButton(self.frame)
        self.sinifGirisEkle.setGeometry(QtCore.QRect(430, 150, 41, 41))
        self.sinifGirisEkle.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images2/icons8-plus-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sinifGirisEkle.setIcon(icon1)
        self.sinifGirisEkle.setIconSize(QtCore.QSize(20, 20))
        self.sinifGirisEkle.setObjectName("sinifGirisEkle")

        self.sinifGiristablo = QtWidgets.QTableWidget(self.frame)
        self.sinifGiristablo.setGeometry(QtCore.QRect(710, 60, 281, 211))
        self.sinifGiristablo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sinifGiristablo.setGridStyle(QtCore.Qt.SolidLine)
        self.sinifGiristablo.setRowCount(2)
        self.sinifGiristablo.setColumnCount(2)
        self.sinifGiristablo.setObjectName("sinifGiristablo")

        self.sinifGirisSinifAdi = QtWidgets.QLineEdit(self.frame)
        self.sinifGirisSinifAdi.setGeometry(QtCore.QRect(110, 100, 361, 22))
        self.sinifGirisSinifAdi.setInputMask("")
        self.sinifGirisSinifAdi.setText("")
        self.sinifGirisSinifAdi.setObjectName("sinifGirisSinifAdi")

        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(110, 50, 111, 21))
        self.label_7.setObjectName("label_7")

        self.sinifGirisSil = QtWidgets.QPushButton(self.frame)
        self.sinifGirisSil.setGeometry(QtCore.QRect(370, 150, 41, 41))
        self.sinifGirisSil.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images2/icons8-delete-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sinifGirisSil.setIcon(icon2)
        self.sinifGirisSil.setIconSize(QtCore.QSize(20, 20))
        self.sinifGirisSil.setObjectName("sinifGirisSil")

        self.sinifGirisGunc = QtWidgets.QPushButton(self.frame)
        self.sinifGirisGunc.setGeometry(QtCore.QRect(310, 150, 41, 41))
        self.sinifGirisGunc.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images2/icons8-update-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sinifGirisGunc.setIcon(icon3)
        self.sinifGirisGunc.setIconSize(QtCore.QSize(20, 20))
        self.sinifGirisGunc.setObjectName("sinifGirisGunc")

        self.sinifGetir = QtWidgets.QPushButton(self.frame)
        self.sinifGetir.setGeometry(QtCore.QRect(250, 150, 41, 41))
        self.sinifGetir.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images2/icons8-syllabus-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sinifGetir.setIcon(icon3)
        self.sinifGetir.setIconSize(QtCore.QSize(20, 20))
        self.sinifGetir.setObjectName("sinifGetir")

        self.sinifGiriscomboBox = QtWidgets.QComboBox(self.frame)
        self.sinifGiriscomboBox.setGeometry(QtCore.QRect(110, 390, 131, 21))
        self.sinifGiriscomboBox.setCurrentText("")
        self.sinifGiriscomboBox.setObjectName("sinifGiriscomboBox")


        self.sinifGirisTabloBuyuk = QtWidgets.QTableWidget(self.frame)
        self.sinifGirisTabloBuyuk.setGeometry(QtCore.QRect(110, 460, 881, 161))
        self.sinifGirisTabloBuyuk.setColumnCount(7)
        self.sinifGirisTabloBuyuk.setObjectName("sinifGirisTabloBuyuk")
        self.sinifGirisTabloBuyuk.setRowCount(0)

        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(50, 330, 981, 22))
        self.lineEdit_8.setInputMask("")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.CikisB = QtWidgets.QPushButton(Form)
        self.CikisB.setGeometry(QtCore.QRect(1254, 4, 41, 41))
        self.CikisB.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images2/icons8-exit-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CikisB.setIcon(icon4)
        self.CikisB.setIconSize(QtCore.QSize(20, 20))
        self.CikisB.setObjectName("OgrenciCikisB")
        self.CikisB.setStyleSheet("""
        
        QPushButton:hover
        {
          border-radius:15px;
          background:rgba(255, 0, 0, 0.4);


        }""")

        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(110, 200, 200, 50))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("""
                        QLabel{
                        color:red;
                        }
                        """)

        self.sinifGirisEkle.clicked.connect(self.sinifEkleQ)
        self.sinifGirisSil.clicked.connect(self.sinifSilQ)
        self.sinifGetir.clicked.connect(self.sinifGetirr)
        self.sinifGirisGunc.clicked.connect(self.sinifGunc)
        self.sinifGiriscomboBox.activated.connect(self.Secim)
        self.CikisB.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sinifGirisSinifAdi.setPlaceholderText(_translate("Form", "Sınıf Adı"))
        self.label_7.setText(_translate("Form", "Sınıf Adı"))
        self.label_9.setText(_translate("Form", ""))
        self.loadData()
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
