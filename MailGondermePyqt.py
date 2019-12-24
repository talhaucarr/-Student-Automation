import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(293, 252)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 271, 201))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 220, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)

        self.pushButton.clicked.connect(self.yolla)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def yolla(self):

        mesaj1 = self.textEdit.toPlainText()
        gonderilcek_kisi = self.lineEdit.text()

        mesaj = MIMEMultipart()

        mesaj["From"] = "talhaucrr@gmail.com"

        mesaj["To"] = gonderilcek_kisi

        mesaj["Subject"] = "Smtp Mail Gonderme"

        yazi = """
        {}
        """.format(mesaj1)

        # https://myaccount.google.com/lesssecureapps?pli=1 BURAYA GİRİP DAHA AZ GÜVENLİ UYGULAMALARA İZİN VERİ AÇMAMIZ GEREKİYOR
        mesaj_govdesi = MIMEText(yazi, "plain")

        mesaj.attach(mesaj_govdesi)

        try:

            mail = smtplib.SMTP("smtp.gmail.com", 587)

            mail.ehlo()

            mail.starttls()

            mail.login("talhaucrr@gmail.com", "T-lha26.41")

            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

            print("Mail Başarıyla Gönderildi!!!")

            mail.close()

        except:

            sys.stderr.write("Bir sorun oluştu!!")

            sys.stderr.flush()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Gönder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
