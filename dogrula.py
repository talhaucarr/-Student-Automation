# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dogrula.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import kayitOlEkran

class Ui_Form(object):

    def onayla(self):

        self.ui = kayitOlEkran.Ui_Form()

        dogrulamaKodu = self.lineEdit.text()
        dosya = open("Dogrulama.txt", "r")
        temp = dosya.read()
        dosya.close()
        print(type(dogrulamaKodu))
        print("burda")
        if(int(temp) == int(dogrulamaKodu)):
            print("burda")
            self.ui.kayitOl2()
            #dosya2 = open("DonusDegeri.txt","w")
            #dosya2.write("1")
            print("burda")
            #dosya2.close()
        else:

            return 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(223, 74)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 10, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(64, 40, 91, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.onayla)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Doğrula"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
