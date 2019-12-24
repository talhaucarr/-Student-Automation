# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ogretmenekran.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ogrenciEkleEkrani import Ui_Form2
import dersKayit,notGiris,akademikTakvim,sinifEkrani,sys,ogrenciEkleEkrani


class Ui_Form(object):

    def studentWindow(self):

        self.window =   QtWidgets.QWidget()
        self.ui = ogrenciEkleEkrani.Ui_Form2()
        self.ui.setupUi2(self.window)
        self.window.show()

    def studyWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = dersKayit.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def classWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = sinifEkrani.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def takvimWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = akademikTakvim.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def notGirisWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = notGiris.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def Cikis(self):
        sys.exit()

    def setupUi(self, Form):
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(1303, 771)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Downloads/icons8-university-25.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(" *{\n"
"font-family:century gothic;\n"
"font-size:24px;\n"
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
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(110, 20, 1091, 731))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 90, 211, 201))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images2/icons8-student-male-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")



        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 90, 211, 201))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images2/icons8-study-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 90, 211, 201))
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images2/icons8-class-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 400, 211, 201))
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images2/icons8-calendar-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(780, 400, 211, 201))
        self.pushButton_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images2/icons8-exit-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 400, 211, 201))
        self.pushButton_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images2/icons8-syllabus-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5.setStyleSheet("""QPushButton:hover
                        {
                          border-radius:15px;
                          background:rgba(255, 0, 0, 0.4);


                        }""")

        self.pushButton.clicked.connect(self.studentWindow)
        self.pushButton_2.clicked.connect(self.studyWindow)
        self.pushButton_4.clicked.connect(self.takvimWindow)
        self.pushButton_3.clicked.connect(self.classWindow)
        self.pushButton_6.clicked.connect(self.notGirisWindow)
        self.pushButton_5.clicked.connect(self.Cikis)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
