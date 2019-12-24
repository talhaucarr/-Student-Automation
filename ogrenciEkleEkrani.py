# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ogrenciEkleEkrani.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from OgrenciKayit import *

ogrenciIslem = OgrenciKayit()

class Ui_Form2(object):



    def Temizle(self):

        self.OgrenciAd.setText("")
        self.OgrenciSoyad.setText("")
        self.OgrenciNo.setText("")
        self.OgrenciSinif.setText("")
        self.OgrenciEmail.setText("")
        """self.OgrenciAd.setPlaceholderText("Öğrenci Adı")
        self.OgrenciSoyad.setPlaceholderText( "Öğrenci Soyadı")
        self.OgrenciNo.setPlaceholderText("Öğrenci No")
        self.OgrenciSinif.setPlaceholderText( "Sınıf")
        self.OgrenciEmail.setPlaceholderText( "E-mail")"""

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Close?', 'Close application?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def ogrenciGetirr(self):

        if self.tableWidget.selectionModel().hasSelection():
            row = self.tableWidget.currentRow()
            self.OgrenciAd.setText(self.tableWidget.item(row, 0).text())
            self.OgrenciSoyad.setText(self.tableWidget.item(row, 1).text())
            self.OgrenciNo.setText(self.tableWidget.item(row, 2).text())
            self.OgrenciSinif.setText(self.tableWidget.item(row, 3).text())
            self.OgrenciEmail.setText(self.tableWidget.item(row, 4).text())
            """query = session.query(Product).filter(Product.product_id == 'product_id').first()
            session.delete(query)
            session.commit()
            # self.dbCursor.execute(DELETE FROM Main WHERE username=?, currentUsername)
            # self.dbConn.commit()
            self.products_table.removeRow(row)"""

    def bilgileriGetir(self):

        sa = self.tableWidget.currentRow()
        self.loadData()
        for i in range(5):

            thing = self.tableWidget.item(sa, i)
            if thing is not None and thing.text() != '':
                print(thing.text())

    def ogrenciSilll(self):

        no = self.OgrenciNo.text()

        try:
            ogrenciIslem.ogrenciSil(no)
            print(no)
            self.label_9.setText("Ogrenci Başarıyla Silindi!")
            self.Temizle()
            self.loadData()
        except Exception:
            print("yanlıs")

    def ogrenciGuncelle(self):
        ad = self.OgrenciAd.text()
        soyad = self.OgrenciSoyad.text()
        no = self.OgrenciNo.text()
        sinif = self.OgrenciSinif.text()
        email = self.OgrenciEmail.text()
        try:
            ogrenciIslem.ogrenciGuncelle(ad,soyad,no,sinif,email)
            self.label_9.setText("Ogrenci Başarıyla Guncellendi!")
            self.Temizle()
            self.loadData()

        except Exception:
            print("sg")

    def loadData(self):
        connection = sqlite3.connect("Ogrenciler.db")
        sorgu = "select * from ogrenciler"
        result = connection.execute(sorgu)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for col_number, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(col_data)))

        connection.close()

    def ogrenciEkle(self):
        ad = self.OgrenciAd.text()
        soyad = self.OgrenciSoyad.text()
        no = self.OgrenciNo.text()
        sinif = self.OgrenciSinif.text()
        email = self.OgrenciEmail.text()
        try:
            """self.connection = sqlite3.connect("Ogrenciler.db")
            self.c = self.connection.cursor()
            self.c.execute("INSERT INTO ogrenciler Values(?,?,?,?,?)", (ad, soyad, no, sinif, email))
            self.connection.commit()
            self.c.close()
            self.connection.close()
            self.loadData()"""
            yeni_Ogrenci = Ogrenci(ad.capitalize(), soyad.capitalize(), no, sinif,
                                           email)
            ogrenciIslem.ogrenciEkle(yeni_Ogrenci)
            self.label_9.setText("Ogrenci Başarıyla Eklendi!")
            self.Temizle()
            self.loadData()
        except Exception:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox, "Ulaa")

    def setupUi2(self, Form):

        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        Form.setObjectName("Form")
        Form.resize(1303, 771)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/icons8-university-25.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.frame.setGeometry(QtCore.QRect(100, 20, 1091, 731))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.OgrenciEkleB = QtWidgets.QPushButton(self.frame)
        self.OgrenciEkleB.setGeometry(QtCore.QRect(1010, 550, 41, 41))
        self.OgrenciEkleB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images2/icons8-plus-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OgrenciEkleB.setIcon(icon1)
        self.OgrenciEkleB.setIconSize(QtCore.QSize(20, 20))
        self.OgrenciEkleB.setObjectName("OgrenciEkleB")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(420, 50, 651, 481))
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.OgrenciAd = QtWidgets.QLineEdit(self.frame)
        self.OgrenciAd.setGeometry(QtCore.QRect(30, 100, 361, 22))
        self.OgrenciAd.setInputMask("")
        self.OgrenciAd.setText("")
        self.OgrenciAd.setObjectName("OgrenciAd")
        self.OgrenciSoyad = QtWidgets.QLineEdit(self.frame)
        self.OgrenciSoyad.setGeometry(QtCore.QRect(30, 210, 361, 22))
        self.OgrenciSoyad.setInputMask("")
        self.OgrenciSoyad.setText("")
        self.OgrenciSoyad.setObjectName("OgrenciSoyad")
        self.OgrenciNo = QtWidgets.QLineEdit(self.frame)
        self.OgrenciNo.setGeometry(QtCore.QRect(30, 310, 361, 22))
        self.OgrenciNo.setInputMask("")
        self.OgrenciNo.setText("")
        self.OgrenciNo.setObjectName("OgrenciNo")
        self.OgrenciSinif = QtWidgets.QLineEdit(self.frame)
        self.OgrenciSinif.setGeometry(QtCore.QRect(30, 410, 361, 22))
        self.OgrenciSinif.setInputMask("")
        self.OgrenciSinif.setText("")
        self.OgrenciSinif.setObjectName("OgrenciSinif")
        self.OgrenciEmail = QtWidgets.QLineEdit(self.frame)
        self.OgrenciEmail.setGeometry(QtCore.QRect(30, 510, 361, 22))
        self.OgrenciEmail.setInputMask("")
        self.OgrenciEmail.setText("")
        self.OgrenciEmail.setObjectName("OgrenciEmail")
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
        self.OgrenciSilB = QtWidgets.QPushButton(self.frame)
        self.OgrenciSilB.setGeometry(QtCore.QRect(950, 550, 41, 41))
        self.OgrenciSilB.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images2/icons8-delete-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OgrenciSilB.setIcon(icon2)
        self.OgrenciSilB.setIconSize(QtCore.QSize(20, 20))
        self.OgrenciSilB.setObjectName("OgrenciSilB")
        self.OgrenciGuncB = QtWidgets.QPushButton(self.frame)
        self.OgrenciGuncB.setGeometry(QtCore.QRect(890, 550, 41, 41))
        self.OgrenciGuncB.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images2/icons8-update-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OgrenciGuncB.setIcon(icon3)
        self.OgrenciGuncB.setIconSize(QtCore.QSize(20, 20))
        self.OgrenciGuncB.setObjectName("OgrenciGuncB")
        self.OgrenciGetirB = QtWidgets.QPushButton(self.frame)
        self.OgrenciGetirB.setGeometry(QtCore.QRect(830, 550, 41, 41))
        self.OgrenciGetirB.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images2/icons8-syllabus-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OgrenciGetirB.setIcon(icon4)
        self.OgrenciGetirB.setIconSize(QtCore.QSize(20, 20))
        self.OgrenciGetirB.setObjectName("OgrenciGetirB")

        self.CikisB = QtWidgets.QPushButton(Form)
        self.CikisB.setGeometry(QtCore.QRect(1250, 4, 41, 41))
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
        self.label_9.setGeometry(QtCore.QRect(33, 560, 200, 50))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("""
        QLabel{
        color:red;
        }
        """)

        self.OgrenciEkleB.clicked.connect(self.ogrenciEkle)
        self.OgrenciSilB.clicked.connect(self.ogrenciSilll)
        self.OgrenciGuncB.clicked.connect(self.ogrenciGuncelle)
        self.OgrenciGetirB.clicked.connect(self.ogrenciGetirr)
        self.CikisB.clicked.connect(Form.close)





        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.OgrenciAd.setPlaceholderText(_translate("Form", "Öğrenci Adı"))
        self.OgrenciSoyad.setPlaceholderText(_translate("Form", "Öğrenci Soyadı"))
        self.OgrenciNo.setPlaceholderText(_translate("Form", "Öğrenci No"))
        self.OgrenciSinif.setPlaceholderText(_translate("Form", "Sınıf"))
        self.OgrenciEmail.setPlaceholderText(_translate("Form", "E-mail"))
        self.label.setText(_translate("Form", "Ad"))
        self.label_2.setText(_translate("Form", "Soyad"))
        self.label_3.setText(_translate("Form", "No"))
        self.label_4.setText(_translate("Form", "Sınıf"))
        self.label_5.setText(_translate("Form", "E-mail"))
        self.label_9.setText(_translate("Form",""))
        self.loadData()


import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormAS = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi2(FormAS)
    FormAS.show()
    sys.exit(app.exec_())

"""QPushButton:hover:!pressed
{
  border: 1px solid red;
}"""