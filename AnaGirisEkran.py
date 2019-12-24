# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dosyaadi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import ogrenciEkran,ogretmenEkrani
from OgrenciKayit import *

kullaniciIslem = Kullanicilar()

class Ui_Form(object):

    def yolla(self,mail):

        self.Mesaj(mail)
        self.koduDosyaYaz()
        self.bilgileriDosyaYaz()

    def rasgele(self):

        rand = (random.randint(1000, 10000))
        return rand

    def onayla(self):

        kod = self.dogrulamaLine.text()
        dosya = open("Dogrulama.txt", "r")
        temp = dosya.read()

        dosya.close()
        if (int(kod) == int(temp)):
            self.kayitOl2()
            print("annen")
        else:
            print("olmadi knk")

    def cikis(self):
        sys.exit()

    def Mesaj(self,maill):
        #MESAJI BANKO GÖNDERİYOR RAHATS
        mesaj = MIMEMultipart()

        mesaj["From"] = "talhaucrr@gmail.com"
        print(maill)
        mesaj["To"] = maill

        self.a = self.rasgele()
        self.koduDosyaYaz()

        mesaj["Subject"] = "Şifre Doğrulama"

        print(self.a)

        yazi = "Doğrulama Kodunuz:%s" % (self.a)

        # https://myaccount.google.com/lesssecureapps?pli=1 BURAYA GİRİP DAHA AZ GÜVENLİ UYGULAMALARA İZİN VERİ AÇMAMIZ GEREKİYOR
        mesaj_govdesi = MIMEText(yazi, "plain")

        mesaj.attach(mesaj_govdesi)

        try:

            mail = smtplib.SMTP("smtp.gmail.com", 587)

            mail.ehlo()

            mail.starttls()

            mail.login("talhaucrr@gmail.com", "T-lha26.41")

            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

            renkliYıldız()
            print("Mail Başarıyla Gönderildi!!!")
            renkliYıldız()

            mail.close()

            return self.a

        except:

            sys.stderr.write("*****\n")
            sys.stderr.write("Mail gönderilemedi bir sorun oluştu!!\n")
            sys.stderr.write("*****")
            sys.stderr.flush()

    def kayitOl(self):

        self.kAdi = self.kayitKAdi.text()
        self.sifre = self.kayitSifre.text()
        self.email = self.kayitMail.text()
        self.yolla(self.email)

    def kayitOl2(self):

        #self.ui.setupUi(self.window)
        """self.window.hide()
        dosya2 = open("Bilgiler.txt", "r")
        temp = dosya2.readlines()
        for i in temp:
            a = i.split(" ")

        print(a[0])
        print(a[1])
        print(a[2])

        dosya2.close()"""
        try:
            yeni_kullanici = Kullanıcı(self.kAdi, self.sifre, self.email, self.rasgele())
            kullaniciIslem.kullaniciEkle(yeni_kullanici)
            self.label_9.setText("Kayit Başarılı!")
        except Exception:
            print("ulaa")

    def koduDosyaYaz(self):

        dosya = open("Dogrulama.txt","w")
        dosya.write("{}".format(self.a))
        dosya.close()

    def bilgileriDosyaYaz(self):
        dosya = open("Bilgiler.txt","w")
        dosya.write("{} {} {}".format(self.kAdi,self.sifre,self.email))
        dosya.close()

    def dosyaYaz(self):

        sifre = self.lineEdit_2.text()
        ths = open("OgrenciNotemp.txt", "w")
        ths.write(sifre[1:])
        ths.close()

    def ogretmenGiris(self):
        self.window = QtWidgets.QWidget()
        self.ui = ogretmenEkrani.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def ogrenciGirisss(self):
        self.window = QtWidgets.QWidget()
        self.ui = ogrenciEkran.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def kGirisi(self):

        kAd = self.lineEdit.text()
        sifre = self.lineEdit_2.text()
        kullaniciIslem.kullaniciGiris(kAd,sifre)
        if sifre[:1]=="o":
            self.dosyaYaz()
            Form.hide()
            self.ogrenciGirisss()
        else:
            self.dosyaYaz2()
            Form.hide()
            self.ogretmenGiris()

    def dosyaYaz2(self):
        sifre = self.lineEdit.text()
        ths = open("OgretmenTemp.txt", "w")
        ths.write(sifre)
        ths.close()

    def setupUi(self, Form):
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(1099, 703)
        Form.setStyleSheet(" *{\n"
"font-family:century gothic;\n"
"font-size:18px;\n"
"}\n"
"QFrame{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"}\n"
"#Form{\n"
"    background:url(:/images2/taslar.jpg);\n"
"}\n"
"QPushButton{\n"
"background:#cfaf8c;\n"
"border-radius:60px;\n"
"}\n"
"QToolButton{\n"
"background:rgba(194,175,161,0.5);\n"
"border-radius:60px;\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"background:transparent\n"
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
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid#717072;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(590, 60, 461, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 520, 421, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 170, 421, 22))
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 330, 421, 22))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 130, 261, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 290, 261, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(50, 60, 461, 581))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.kayitOlB = QtWidgets.QPushButton(self.frame_2)
        self.kayitOlB.setGeometry(QtCore.QRect(20, 520, 421, 41))
        self.kayitOlB.setObjectName("kayitOlB")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 47, 13))
        self.label_5.setObjectName("label_5")
        self.kayitKAdi = QtWidgets.QLineEdit(self.frame_2)
        self.kayitKAdi.setGeometry(QtCore.QRect(20, 100, 421, 20))
        self.kayitKAdi.setObjectName("kayitKAdi")
        self.kayitSifre = QtWidgets.QLineEdit(self.frame_2)
        self.kayitSifre.setGeometry(QtCore.QRect(20, 220, 421, 20))
        self.kayitSifre.setObjectName("kayitSifre")
        self.kayitMail = QtWidgets.QLineEdit(self.frame_2)
        self.kayitMail.setGeometry(QtCore.QRect(20, 330, 421, 20))
        self.kayitMail.setObjectName("kayitMail")
        self.dogrulamaLine = QtWidgets.QLineEdit(self.frame_2)
        self.dogrulamaLine.setGeometry(QtCore.QRect(20, 420, 81, 20))
        self.dogrulamaLine.setObjectName("dogrulamaLine")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 410, 71, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background:rgba(194,175,161,0.5);\n"
"border-radius:20px;\n"
"font-size:13px;\n"
"}\n"
"QPushButton:hover{\n"
"color:black;\n"
"border-radius:15px;\n"
"background:rgb(194,175,161);\n"
"}")

        self.pushButton_2.setObjectName("pushButton_2")

        self.CikisB = QtWidgets.QPushButton(Form)
        self.CikisB.setGeometry(QtCore.QRect(1050, 4, 41, 41))
        self.CikisB.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images2/icons8-exit-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CikisB.setIcon(icon4)
        self.CikisB.setIconSize(QtCore.QSize(20, 20))
        self.CikisB.setObjectName("OgrenciCikisB")
        self.CikisB.setStyleSheet("""QPushButton:hover
        {
          
        border - radius: 15px;
        background: rgba(255, 0, 0, 0.4);


        }""")

        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(250, 420, 80, 13))
        self.label_9.setObjectName("label_9")

        self.pushButton_2.clicked.connect(self.onayla)
        self.pushButton.clicked.connect(self.kGirisi)
        self.kayitOlB.clicked.connect(self.kayitOl)
        self.CikisB.clicked.connect(self.cikis)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Giriş Yap"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.kayitKAdi.setPlaceholderText(_translate("Form", "Username"))
        self.kayitSifre.setPlaceholderText(_translate("Form", "Password"))
        self.kayitMail.setPlaceholderText(_translate("Form", "E-mail"))
        self.dogrulamaLine.setPlaceholderText(_translate("Form", "Kod"))
        self.label.setText(_translate("Form", "Kullanıcı Adı"))
        self.label_2.setText(_translate("Form", "Şifre"))
        self.kayitOlB.setText(_translate("Form", "Kayit Ol"))
        self.label_3.setText(_translate("Form", "Kullanici Adı"))
        self.label_4.setText(_translate("Form", "Şifre"))
        self.label_5.setText(_translate("Form", "Email"))
        self.label_9.setText(_translate("Form", ""))
        self.pushButton_2.setText(_translate("Form", "Doğrula"))

import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
