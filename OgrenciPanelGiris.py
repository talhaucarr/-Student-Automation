import sqlite3
import tkinter as tk

#import getpass

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import sys

import random

import time

from OgretmenPanel import *
from OgrenciPanel import *
def win_getpass(prompt='Password: ', stream=None):
    """Prompt for password with echo off, using Windows getch()."""
    import msvcrt
    for c in prompt:
        msvcrt.putwch(c)
    pw = ""
    while 1:
        c = msvcrt.getwch()
        if c == '\r' or c == '\n':
            break
        if c == '\003':
            raise KeyboardInterrupt
        if c == '\b':
            if pw == '':
                pass
            else:
                pw = pw[:-1]
                msvcrt.putwch('\b')
                msvcrt.putwch(" ")
                msvcrt.putwch('\b')
        else:
            pw = pw + c
            msvcrt.putwch("*")
    msvcrt.putwch('\r')
    msvcrt.putwch('\n')
    return pw
def Cikis():

    renkliYıldız()
    print("Çıkış Yapılıyor...")
    time.sleep(1)
    renkliYıldız()
    print("Çıkış Yapıldı!")
    renkliYıldız()
    print("Güle Güle!")
    renkliYıldız()
    sys.exit()

class Kullanıcı():

    def __init__(self,KlncAd,KlncSifre,KlncMail,KlncKod):

        self.KlncAd = KlncAd
        self.KlncSifre = KlncSifre
        self.KlncMail = KlncMail
        self.KlncKod = KlncKod

    def __str__(self):

        return "Kullanıcı Adı: {}\nŞifre: {}\nEmail: {}\nID: {}".format(self.KlncAd, self.KlncSifre, self.KlncMail,self.KlncKod)

class Kullanicilar():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("Ogrenciler.db")
        self.cursor = self.baglanti.cursor()
        sorgu3 = "CREATE TABLE IF NOT EXISTS kullanicilar(KullanıcıAdi TEXT,Sifre TEXT,Mail TEX,Kod TEXT)"
        self.cursor.execute(sorgu3)
        self.baglanti.commit()

    def baglantiyi_kes(self):

        self.baglanti.close()

    def kullaniciEkle(self,klnc):

        temp = 0
        x = 0

        if temp == 0:

            sorgu3 = "Select * from kullanicilar"
            self.cursor.execute(sorgu3, )
            kullan = self.cursor.fetchall()

            for i in kullan:

                if i[2] == klnc.KlncMail or i[0] == klnc.KlncAd:  # BURAYI EN SON MAİL VE AD OLARAK 2 KISıMA AYIR

                    renkliYıldız()
                    print("Eklemek istediginiz Kullanıcının e-mail'i veya adı sistemde bulunuyor!")
                    renkliYıldız()
                    x = 1
                    break

            if x == 0:
                print(klnc.KlncMail)
                b = Mesaj(klnc.KlncMail)

                kod = input("Doğrulama Kodunu Giriniz:")

                if int(kod) == b:  # BURAYI DEĞİŞTİRMEN GEREKİYOR İLK KODU YOLLAMAMASI LAZIM

                    print("Kod doğru!")

                else:

                    renkliYıldız()
                    print("Kodu Yanlış Girdiniz. Kayıt Başarısız!")
                    renkliYıldız()

                sorgu2 = "INSERT INTO kullanicilar Values(?,?,?,?)"
                self.cursor.execute(sorgu2, (klnc.KlncAd, klnc.KlncSifre, klnc.KlncMail,klnc.KlncKod))

                renkliYıldız()
                print("Kullanıcı ekleniyor...")
                time.sleep(1)
                renkliYıldız()
                print("Kullanıcı eklendi!")
                renkliYıldız()

                self.baglanti.commit()


    def kullaniciGiris(self,ad,sifre):

        sorgu = "SELECT * FROM kullanicilar WHERE KullanıcıAdi = ? and Sifre = ?"

        self.cursor.execute(sorgu,(ad,sifre))

        data = self.cursor.fetchall()

        if len(data) == 0:

            renkliYıldız()
            print("Böyle bir kullanıcı yok")
            renkliYıldız()
            sys.exit()

        else:

            renkliYıldız()
            print("Giriş Başarılı!")
            renkliYıldız()

    def sifreDegistir(self,sifre,mail):

        sorgu = "UPDATE kullanicilar set  Sifre = ? where Mail = ?"

        self.cursor.execute(sorgu, (sifre,mail))

        self.baglanti.commit()

    def kullaniciSil(self,mail):

        sorgu = "DELETE FROM kullanicilar where Sifre = ?"
        self.cursor.execute(sorgu, (mail,))
        self.baglanti.commit()

    def kullaniciSil2(self,no):

        sorgu = "DELETE FROM kullanicilar where Mail = ?"
        self.cursor.execute(sorgu, (no,))
        self.baglanti.commit()

    def kullaniciGoruntule(self):

        sorgu = "Select * from kullanicilar"
        self.cursor.execute(sorgu)
        kullaniclar = self.cursor.fetchall()
        if (len(kullaniclar) == 0):
            print("Listenizde hiç kullanıcı yok!")
        else:
            for i in kullaniclar:
                renkliYıldız()
                print("Kullanıcı Adı:",i[0],"Şifre:",i[1])
                renkliYıldız()

def Mesaj(maill):

    mesaj = MIMEMultipart()

    mesaj["From"] = "talhaucrr@gmail.com"

    mesaj["To"] = maill

    a = rasgele()

    mesaj["Subject"] = "Şifre Doğrulama"

    print(a)

    yazi = "Doğrulama Kodunuz:%s" % (a)

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

        return a

    except:

        sys.stderr.write("*****\n")
        sys.stderr.write("Mail gönderilemedi bir sorun oluştu!!\n")
        sys.stderr.write("*****")
        sys.stderr.flush()

def rasgele():

    rand = (random.randint(1000, 10000))
    return rand

def reis():

    pencere = tk.Tk()
    pencere.geometry('200x70')
    etiket = tk.Label(text='Hoş geldin REİS')
    etiket.pack()
    düğme = tk.Button(text='Hoş bulduk aslanım', command=pencere.destroy)
    düğme.pack()
    pencere.mainloop()

kullanici = Kullanicilar()

while True:
    uzunRenkliYıldız()
    print("""
        Okul Programına Hoşgeldiniz.

        1. Giriş Yap

        2. Kayit Ol

        3. Şifremi Unuttum

        Geri dönmek için 'z', çıkmak için 'q' ya basınız.
        """)
    uzunRenkliYıldız()

    seçim = input("İşleminizi Seçiniz:")

    if seçim == 'q':

        Cikis()

    if seçim == 'z':

        break

    elif seçim == '1':

        kAdı = input("Kullanıcı Adı:")
        kSifre = input("Şifre:")

        if kAdı=='0' and kSifre=='0':

            reis()

            while True:

                uzunRenkliYıldız()
                print("""
        Hoş Geldin Reis

        1. Kullanıcı Silme

        2. Kullanıcıları Görüntüle
        
        3. Öğrenci Sil
        
        4. Ders Sil
        
        5. Sınıf Sil

        Geri dönmek için 'z', çıkmak için 'q' ya basınız.
        """)
                uzunRenkliYıldız()

                secim2 = input("İşleminizi Seçiniz:")

                if secim2 == 'q':

                    Cikis()

                elif secim2 == 'z':

                    break

                elif secim2 == '1':

                    sil = input("Kimi silmek istiyorsunuz:")
                    kullanici.kullaniciSil(sil)
                    print("Kullanıcı siliniyor...")
                    print("*****\n")
                    time.sleep(1)
                    print("Kullanıcı silindi!")

                elif secim2 == '2':

                    kullanici.kullaniciGoruntule()

                elif secim2 == '3':

                    uzunRenkliYıldız()
                    print("""
        1. Ogrenci Adına Göre Silme İşlemi

        2. Ogrenci Numarasına Göre Silme İşlemi

        Geri dönmek için 'z' ye basınız.
    """)
                    uzunRenkliYıldız()

                    işlem2 = input("Silme işleminizi giriniz:")

                    if işlem2 == 'z':

                        renkliYıldız()
                        print("Silme işleminden çıkıldı")
                        renkliYıldız()
                        continue

                    elif işlem2 == '1':

                        ogr2 = input("Öğrenci adı giriniz:")
                        print("Öğrenci siliniyor...")
                        time.sleep(1)
                        ogrenci.ogrenciAdSil(ogr2)
                        kullanici.kullaniciSil(ogr2)
                        renkliYıldız()
                        print("Öğrenci silindi")
                        renkliYıldız()

                    elif işlem2 == '2':

                        ogr3 = input("Öğrenci no giriniz:")
                        renkliYıldız()
                        print("Öğrenci siliniyor...")
                        time.sleep(1)
                        ogrenci.ogrenciNoSil(ogr3)
                        ogr3 = 'o' + ogr3
                        kullanici.kullaniciSil(ogr3)
                        renkliYıldız()
                        print("Öğrenci silindi")
                        renkliYıldız()

                elif secim2 == '4':

                    drs = int(input("Ders No Giriniz:"))
                    print("Ders Siliniyor...")
                    time.sleep(1)
                    derss.dersSil(drs)
                    renkliYıldız()
                    print("Ders Silindi!")
                    renkliYıldız()

                elif secim2 == '5':

                    snf2 = input("Sınıf adı giriniz:")
                    print("Sınıf siliniyor...")
                    time.sleep(1)
                    snf.sinifSil(snf2)
                    renkliYıldız()
                    print("Sınıf silindi")
                    renkliYıldız()

                else:

                    renkliYıldız()
                    print("Hatali Seçim!")
                    renkliYıldız()

        else:

            kullanici.kullaniciGiris(kAdı,kSifre)

            if kSifre[0] == 'o':

                anaGiris2(kAdı,kSifre)

            elif kSifre[0] != 'o':#BURDAKİ HATAYI DÜZELT

                anaGiris(kAdı)


    elif seçim == '2':

        #Kayıt Olma yeri

        kullaniciAdi = input("Kullanıcı Adı:")
        kullaniciSifre = input("Şifre:")
        Email = input("E-mail:")

        yeni_kullanici = Kullanıcı(kullaniciAdi, kullaniciSifre, Email,rasgele())
        kullanici.kullaniciEkle(yeni_kullanici)

    elif seçim == '3':

        #Şifre Unutma Yeri
        s = input("E-mail Adresinizi Giriniz:")

        #Mesaj(s)

        c = Mesaj(s)

        kod2 = input("Doğrulama Kodunu Giriniz:")

        if int(kod2) == c:

            sifre = input("Yeni Şifrenizi Giriniz:")
            kullanici.sifreDegistir(sifre,s)
            renkliYıldız()
            print("Şifre Değişiyor...")
            time.sleep(1)
            renkliYıldız()
            print("Şifre Değişti!")
            renkliYıldız()

        else:

            renkliYıldız()
            print("Kod Hatalı!!")
            renkliYıldız()
            sys.stderr.flush()

    else:

        renkliYıldız()
        print("Hatali Seçim!")
        renkliYıldız()


