import sqlite3

import time
import sys
import random

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def renkliYıldız():
    print("\033[" + str(96) + "m" + "*****" + "\033[0m")

def sekilliCizgi():

    return   "\033[" + str(106) + "m" + " " + "\033[0m"

def sekilliBosluk():

    return "\033[" + str(106) + "m" + "                                                                                                            " + "\033[0m"

class Ogrenci():

    def __init__(self,OgrenciAd,OgrenciSoyad,OgrenciNo,OgrenciSınıf,OgreniciEmail):

        self.OgrenciAd = OgrenciAd
        self.OgrenciSoyad = OgrenciSoyad
        self.OgrenciNo = OgrenciNo
        self.OgrenciSınıf = OgrenciSınıf
        self.OgrenciEmail = OgreniciEmail

    def __str__(self):

        return "Öğrenci Adı: {}\nÖğrenci Soyadı: {}\nÖğrenci No: {}\nSınıfı: {}\nÖğrenci Email: {}".format(self.OgrenciAd,self.OgrenciSoyad,self.OgrenciNo,self.OgrenciSınıf,self.OgrenciEmail)

class Sinif():

    def __init__(self,SinifAdi,SinifNo):

        self.SinifAdi = SinifAdi
        self.SinifNo = SinifNo

    def __str__(self):

        return "Sınıf Adı: {}\n Sınıf Kodu: {}".format(self.SinifAdi,self.SinifNo)

class Ders():

    def __init__(self,DersNo,DersAdi,DersSaati,DersKredi,VizeAgirlik,FinalAgirlik,DersOgretmeNo,DersSinif):

        self.DersAdi = DersAdi
        self.DersSaati = DersSaati
        self.DersKredi = DersKredi
        self.VizeAgirlik = VizeAgirlik
        self.FinalAgirlik = FinalAgirlik
        self.DersOgretmenNo = DersOgretmeNo
        self.DersNo = DersNo
        self.DersSinif = DersSinif


    def __str__(self):

        return "Ders No: {}\nDers Adı: {}\nDers Saati: {}\nÖğretmeni: {}\nKredisi: {}\nVize Ağırlığı: {}\nFinal Ağırlığı: {}\nAçıldığı Sınıf: {}".format(self.DersNo,self.DersAdi,self.DersSaati,self.DersOgretmenNo,self.DersKredi,self.VizeAgirlik,self.FinalAgirlik,self.DersSinif)

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

                if i[2] == klnc.KlncMail :  # BURAYI EN SON MAİL VE AD OLARAK 2 KISıMA AYIR

                    renkliYıldız()
                    print("Eklemek istediginiz Kullanıcının e-mail'i veya adı sistemde bulunuyor!")
                    renkliYıldız()
                    x = 1
                    break

            if x == 0:

                sorgu2 = "INSERT INTO kullanicilar Values(?,?,?,?)"
                self.cursor.execute(sorgu2, (klnc.KlncAd, klnc.KlncSifre, klnc.KlncMail,klnc.KlncKod))

                renkliYıldız()
                print("Kullanıcı ekleniyor...")

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

    def rasgele(self):
        rand = (random.randint(1000, 10000))
        return rand

class OgrenciKayit():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti=sqlite3.connect("Ogrenciler.db")
        self.cursor=self.baglanti.cursor()
        sorgu2 = "CREATE TABLE IF NOT EXISTS siniflar(sinifAdi TEXT,sinifKod INT)"
        sorgu="CREATE TABLE IF NOT EXISTS ogrenciler(OgrenciAd TEXT,OgrenciSoyad TEXT,OgrenciNo INT,OgrenciSınıf TEXT,OgrenciEmail TEXT)"
        self.cursor.execute(sorgu2)
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):

        self.baglanti.close()

    def ogrencileri_goster(self):

        sorgu="SELECT * from ogrenciler"
        self.cursor.execute(sorgu)
        ogrenciler = self.cursor.fetchall()

        if(len(ogrenciler)==0):

            renkliYıldız()
            print("Listenizde hiç öğrenci yok!")
            renkliYıldız()

        else:

            print(sekilliBosluk())
            #print("\033[" + str(96) + "m" + "|" + "\033[0m")

            for i in ogrenciler:

                print(sekilliCizgi()+"Adı: {} ".format(i[0])+sekilliCizgi() + " Soyadı: {}".format(i[1])+sekilliCizgi() +" No: {} ".format(i[2])+sekilliCizgi()+" Sınıfı: {} ".format(i[3])+sekilliCizgi()+" Email: {}".format(i[4])+sekilliCizgi())
               # print("------------------------------------------------------------------------------------------------------------")
                print(sekilliBosluk())
                #print(i[0],i[1],i[2],i[3])

    def ogrenciEkle(self,ogr):

        if ogr.OgrenciAd.isalpha() and ogr.OgrenciSoyad.isalpha() and ogr.OgrenciNo.isnumeric():

            bayrak = 1
            sd = 0

            sorgu4 = "Select * from siniflar"
            self.cursor.execute(sorgu4, )
            siniflar = self.cursor.fetchall()

            if (len(siniflar)) == 0:

                renkliYıldız()
                print("Listenizde hiç sınıf yok!")
                renkliYıldız()

            else:

                for a in siniflar:

                    if a[0] == ogr.OgrenciSınıf:

                        bayrak = 0
                        break

                    else:

                        bayrak = 1

                if bayrak == 0:
                    sorgu3 = "Select * from ogrenciler"
                    self.cursor.execute(sorgu3, )
                    ogrenciler = self.cursor.fetchall()

                    for i in ogrenciler:

                        if i[4] == ogr.OgrenciEmail or str(i[2]) == ogr.OgrenciNo:  # BURAYI EN SON EMAİL İLE DEĞİŞTİR

                            renkliYıldız()
                            print("Eklemek istediginiz öğrencinin e-mail'i veya numarası sistemde bulunuyor!")
                            renkliYıldız()
                            sd = 1
                            break

                    if sd == 0:
                        sorgu = "INSERT INTO ogrenciler Values(?,?,?,?,?)"  # Öğrenciler tablosuna ekleme sorgusu
                        sorgu2 = "INSERT INTO kullanicilar Values(?,?,?,NULL)"  # Kullanıcılar tablosuna ekleme sorgusu
                        # Öğrenci olduğuiçin şifresini öğrenci numarasının başına 'o' ekleyerek şifre belirliyoruz
                        self.cursor.execute(sorgu,
                                            (ogr.OgrenciAd, ogr.OgrenciSoyad, ogr.OgrenciNo, ogr.OgrenciSınıf,
                                             ogr.OgrenciEmail))

                        tutucu = ogr.OgrenciNo
                        tutucu = "o" + tutucu
                        ogr.OgrenciNo = tutucu

                        self.cursor.execute(sorgu2, (ogr.OgrenciAd, ogr.OgrenciNo, ogr.OgrenciEmail,))

                        renkliYıldız()
                        print("Ogrenci ekleniyor...")

                        renkliYıldız()
                        print("Ogrenci eklendi!")
                        renkliYıldız()

                        self.baglanti.commit()

                elif bayrak == 1:

                    renkliYıldız()
                    print("Eklemek istediğiniz sınıf mevcut değil!")
                    renkliYıldız()

        else:
            renkliYıldız()
            print("""
Yanlış kayıt! lütfen aşağıdaki gibi kayıt yapınız: 

Öğrenci Adı: talha
Öğrenci Soyadı: uçar
Öğrenci No: 136
Sınıf: 123
Email: deneme@gmail.com                       
""")
            renkliYıldız()
    def ogrenciAdSil(self,ogr):

        sorgu = "DELETE FROM ogrenciler where OgrenciAd = ?"
        self.cursor.execute(sorgu, (ogr,))
        self.baglanti.commit()

    def ogrenciNoSil(self,ogr):

        sorgu = "DELETE FROM ogrenciler where OgrenciNo = ?"
        self.cursor.execute(sorgu, (ogr,))
        self.baglanti.commit()

    def ogrenciArat(self,ogr):

        sorgu = "SELECT * FROM ogrenciler "
        self.cursor.execute(sorgu,)
        ogrenciler = self.cursor.fetchall()

        if (len(ogrenciler) == 0):

            renkliYıldız()
            print("Boyle bir öğrenci bulunmuyor...")
            renkliYıldız()

        else:

            for i in ogrenciler:

                if i[0] == ogr:

                    print("Öğrenci Adı: {}\nÖğrenci Soyadı: {}\nÖğrenci No: {}\nSınıfı: {}\nÖğrenci Email: {}".format(i[0], i[1], i[2], i[3],i[4]))
                    renkliYıldız()

    def ogrenciSil(self,no):

        sorgu = "DELETE FROM ogrenciler where OgrenciNo = ?"
        self.cursor.execute(sorgu, (no,))
        self.baglanti.commit()

    def ogrenciGuncelle(self,ad,soyad,no,sinif,email):
        sorgu = "update ogrenciler set OgrenciAd = ?,OgrenciSoyad = ?,OgrenciSınıf = ?,OgrenciEmail = ? where OgrenciNo = ?"
        self.cursor.execute(sorgu, (ad,soyad,sinif,email,no))
        self.baglanti.commit()

class SinifKayit():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti=sqlite3.connect("Ogrenciler.db")
        self.cursor=self.baglanti.cursor()
        sorgu="CREATE TABLE IF NOT EXISTS siniflar(sinifAdi TEXT,sinifKod INT)"
        sorgu2 = "CREATE TABLE IF NOT EXISTS ogrenciler(OgrenciAd TEXT,OgrenciSoyad TEXT,OgrenciNo INT,OgrenciSınıf TEXT)"
        self.cursor.execute(sorgu)
        self.cursor.execute(sorgu2)
        self.baglanti.commit()

    def baglantiyi_kes(self):

        self.baglanti.close()

    def sinifGuncelle(self,ad,no):
        sorgu = "update siniflar set sinifAdi = ? where sinifKod = ?"
        self.cursor.execute(sorgu,(ad,no))
        self.baglanti.commit()

    def siniflari_goster(self):

        sorgu="SELECT * from siniflar"
        self.cursor.execute(sorgu)
        ogrenciler = self.cursor.fetchall()

        if(len(ogrenciler)==0):

            renkliYıldız()
            print("Listenizde hiç sınıf yok!")
            renkliYıldız()
        else:

            print("---------------------")

            for i in ogrenciler:

                print("|Sınıf Adı: {}|".format(i[0]))
                print("---------------------")

    def sinifEkle(self, snf):



        sorgu = "INSERT INTO siniflar Values(?,?)"
        self.cursor.execute(sorgu, (snf.SinifAdi,snf.SinifNo))
        self.baglanti.commit()

        """else:
            renkliYıldız()
            print(
Yanlış kayıt! lütfen aşağıdaki gibi kayıt yapınız: 

Sınıf Adı: 19TFBM1          )
            renkliYıldız()"""

    def sinifSil(self, snf):

        sorgu = "DELETE FROM siniflar where sinifAdi = ?"
        self.cursor.execute(sorgu, (snf,))
        self.baglanti.commit()

    def sinifAra(self,snf):

        sorgu = "SELECT * FROM siniflar "
        self.cursor.execute(sorgu,)
        sinif = self.cursor.fetchall()

        if (len(sinif) == 0):

            renkliYıldız()
            print("Boyle bir sinif bulunmuyor...")
            renkliYıldız()

        else:

            for i in sinif:

                if i[0] == snf:

                    sinif  = Sinif(sinif[0][0])
                    renkliYıldız()
                    print(sinif)

            sorgu2 = "SELECT * FROM ogrenciler "
            self.cursor.execute(sorgu2, )
            ogrenciler = self.cursor.fetchall()

            if (len(ogrenciler) == 0):

                renkliYıldız()
                print("Boyle bir öğrenci bulunmuyor...")
                renkliYıldız()

            else:

                for i in ogrenciler:

                    if i[3] == snf:

                        print("Öğrenci Adı: {}\nÖğrenci Soyadı: {}\nÖğrenci No: {}\nSınıfı: {}".format(i[0], i[1], i[2], i[3]))
                        renkliYıldız()

class DersKayit():

    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):

        self.baglanti=sqlite3.connect("Ogrenciler.db")
        self.cursor=self.baglanti.cursor()
        sorgu3 = "CREATE TABLE IF NOT EXISTS dersler(DersNo INT, DersAdi TEXT,DersSaati INT,DersKredi INT,VizeAgirlik INT,FinalAgirlik INT,DersSinif TEXT,DersOgretmenNo TEXT)"
        self.cursor.execute(sorgu3,)
        self.baglanti.commit()
    def baglantiyi_kes(self):

        self.baglanti.close()


    def dersYayinla(self,ad):

        sorgu = "SELECT * from dersler"
        self.cursor.execute(sorgu)
        dersler = self.cursor.fetchall()

        sorgu2 = "SELECT * FROM kullanicilar"
        self.cursor.execute(sorgu2)
        kullanicilar = self.cursor.fetchall()

        temp = ''

        liste = list()

        for x in kullanicilar:

            if x[0] == ad:
                temp = x[0]

        for i in dersler:

            if i[7] == temp:

                if (len(dersler) == 0):

                    print("Listenizde hiç ders yok!")


                else:

                    pass

                    for a in dersler:

                        if a[7] == temp:

                            liste.append(i)

                        else:

                            pass
        print(liste)

        return liste


    def dersleri_goster(self,ad):

        sorgu = "SELECT * from dersler"
        self.cursor.execute(sorgu)
        dersler = self.cursor.fetchall()

        sorgu2 = "SELECT * FROM kullanicilar"
        self.cursor.execute(sorgu2)
        kullanicilar = self.cursor.fetchall()

        temp = ''

        for x in kullanicilar:

            if x[0] == ad:

                temp = x[3]

        for i in dersler:

            if i[7] == temp:

                if (len(dersler) == 0):

                    renkliYıldız()
                    print("Listenizde hiç ders yok!")
                    renkliYıldız()

                else:

                    print(
                        "-------------------------------------------------------------------------------------------------------------------------------------------")

                    for a in dersler:

                        if a[7] == temp:

                            print(
                                "|Ders No: {} | Ders Adı: {} | Ders Saati: {} | Öğretmen No: {} | Kredisi: {} | Vize Ağırlığı: {} | Final Ağırlığı: {} | Açıldığı Sınıf: {}|".format(
                                    i[0], i[1], i[2], i[7], i[3], i[5], i[4], i[6]))
                            print(
                                "-------------------------------------------------------------------------------------------------------------------------------------------")

                        else:

                            print("Adınıza açılmış ders bulunmuyor.")
                            print(
                                "-------------------------------------------------------------------------------------------------------------------------------------------")
    def dersEkle(self,ders):

        flag = 0

        sorgu3 = "SELECT * FROM siniflar"
        self.cursor.execute(sorgu3)
        siniflar = self.cursor.fetchall()

        if (len(siniflar) == 0):

            renkliYıldız()
            print("Listenizde Hiç Sınıf Yok, Ders Oluşturamazsınız!")
            renkliYıldız()

        else:

            renkliYıldız()

            for i in siniflar:

                if i[0] == ders.DersSinif:

                    sorgu = "INSERT INTO dersler Values(?,?,?,?,?,?,?,?)"
                    sorgu2 = "CREATE TABLE IF NOT EXISTS {}(OgrenciAdi TEXT,OgrenciSoyadi TEXT,OgrenciNumara INT,Vize INT,Final INT,HarfNotu TEXT,Ortalama INT)".format(ders.DersAdi)
                    sorgu3 = "SELECT * FROM ogrenciler where OgrenciSınıf = ?"

                    self.cursor.execute(sorgu, (
                    ders.DersNo, ders.DersAdi, ders.DersSaati, ders.DersKredi,ders.VizeAgirlik,ders.FinalAgirlik, ders.DersSinif,ders.DersOgretmenNo ))
                    self.cursor.execute(sorgu2)
                    self.cursor.execute(sorgu3, (ders.DersSinif,))

                    ogrenciler = self.cursor.fetchall()

                    if (len(ogrenciler) == 0):

                        print("\033[" + str(91) + "m" + "Dersi Açabilceğiniz Hiç Öğrenci Yok" + "\033[0m")
                        renkliYıldız()

                    else:

                        for a in ogrenciler:
                            sorgu4 = "INSERT INTO {} VALUES(?,?,?,NULL,NULL,NULL,NULL)".format(ders.DersAdi)
                            self.cursor.execute(sorgu4, (a[0], a[1], a[2]))

                        flag = 1

                        print("Ders Oluşturuluyor...")

                        renkliYıldız()
                        print("Ders Oluşturuldu!")
                        renkliYıldız()
                    self.baglanti.commit()
                    break
                    # ÖĞRENCİLERİ  DERSE AKTAR

                else:

                    flag = 0

            if flag == 0:
                print("Listenizde Böyle Bir Sınıf Yok, Ders Oluşturamazsınız!")
                renkliYıldız()

    def dersSorgula(self,ders):

        sorgu = "SELECT * FROM dersler "
        self.cursor.execute(sorgu, )
        dersler = self.cursor.fetchall()

        if (len(dersler) == 0):

            renkliYıldız()
            print("Boyle bir ders bulunmuyor...")
            renkliYıldız()

        else:

            for i in dersler:

                if i[0] == ders:
                    print("Ders No: {}\nDers Adı: {}\nDers Saati: {}\nÖğretmeni: {}\nKredisi: {}\nAçıldığı Sınıf: {}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
                    renkliYıldız()

    def dersSil(self,ders):

        sorgu = "DELETE FROM dersler where DersNo = ?"
        self.cursor.execute(sorgu, (ders,))
        self.baglanti.commit()

    def dersGuncelle(self,ders):

        sorgu = "update dersler set DersAdi=?, DersSaati=? ,DersKredi=? ,VizeAgirlik=? ,FinalAgirlik=? ,DersSinif=? ,DersOgretmenNo=? where DersNo=?"
        self.cursor.execute(sorgu,( ders.DersAdi, ders.DersSaati, ders.DersKredi,ders.VizeAgirlik,ders.FinalAgirlik, ders.DersSinif,ders.DersOgretmenNo,ders.DersNo, ))
        self.baglanti.commit()

    def notGirisi(self,notd,no,vizee,finall):

        bayrak = 1
        bayrak2 = 1

        sorgu4 = "SELECT * FROM dersler "
        self.cursor.execute(sorgu4)
        giris = self.cursor.fetchall()

        sorgu3 = "SELECT * FROM kullanicilar "
        self.cursor.execute(sorgu3)
        kullanici = self.cursor.fetchall()

        for x in kullanici:

            if x[0] == no:

                temp = x[3]

        for b in giris:

            if b[0] == notd:

                if b[7] == temp:

                    sorgu = "SELECT * FROM  {}".format(b[1])
                    self.cursor.execute(sorgu)
                    notlar = self.cursor.fetchall()

                    if (len(notlar) == 0):

                        pass

                    else:

                        print("""******************

                            1. Vize Not Giriş

                            2. Final Not Giriş

                    ******************""")
                        secim = input("İşleminizi Seçiniz:")

                        if secim == '1':

                            renkliYıldız()

                            for a in notlar:

                                while bayrak == 1:
                                    print(a[0] + " Adındaki öğrencinin,")

                                    c = int(input("Vizesini Giriniz:"))

                                    renkliYıldız()

                                    if c>=0 and c<=100:

                                        bayrak=0
                                    else:
                                        print("Lütfen not girişini 0-100 aralığında yapınız")

                                sorgu2 = "UPDATE {} SET Vize = {} WHERE OgrenciNumara = {}".format(b[1], c, a[2])
                                self.cursor.execute(sorgu2)
                                self.baglanti.commit()

                        elif secim == '2':

                            renkliYıldız()

                            for a in notlar:

                                while bayrak2 ==1:

                                    print(a[0] + " Adındaki öğrencinin,")

                                    k = int(input("Finalini Giriniz:"))

                                    renkliYıldız()

                                    if k >= 0 and k <= 100:

                                        bayrak2 = 0
                                    else:
                                        print("Lütfen not girişini 0-100 aralığında yapınız")

                                # veritabani_sec.execute("UPDATE ogrenciler SET ogrenci_adi='Ayşe' WHERE ogrenci_no='2'")
                                sorgu3 = "UPDATE {} SET Final = {} WHERE OgrenciNumara = {}".format(b[1], k, a[2])
                                self.cursor.execute(sorgu3)
                                self.baglanti.commit()

                        else:

                            renkliYıldız()
                            print("Yanlış Seçim !")

                else:

                    renkliYıldız()
                    print("Bu sınıfın notlarını giremezsiniz!")

            else:

                renkliYıldız()
                print("Böyle bir sınıf bulunmuyor!")

    def notGir(self,no,vizee,finall,sinifad):
        print(finall)
        if(finall=="None" and vizee=="None"):
            print("ikisini de değer gir")

        elif(finall=="None" and vizee!="None"):
            sorgu3 = "UPDATE {} SET Vize = {} WHERE OgrenciNumara = {}".format(sinifad,vizee,no)
            self.cursor.execute(sorgu3)
            sorgu4 = " SELECT * From ogrenciler "
            self.cursor.execute(sorgu4)
            emailler = self.cursor.fetchall()
            for i in emailler:
                print(i)
                if i[2] == no:
                    self.Mesaj(i[4])
                    print("sa",i[4])
            self.baglanti.commit()

        else:

            sorgu2 = "SELECT * FROM dersler"
            self.cursor.execute(sorgu2)
            dersler = self.cursor.fetchall()

            for i in dersler:

                if i[1] == sinifad:

                    self.vizeTemp = i[4]
                    self.finalTemp = i[5]

            vize = float(vizee) * self.vizeTemp
            final = float(finall) * self.finalTemp
            toplam = vize + final

            toplam = int(toplam)
            if toplam >= 50:

                if (toplam >= 85 and toplam >= 50):
                    c = 'AA'
                elif toplam >= 75 and toplam < 85:
                    c = 'BA'
                elif toplam >= 70 and toplam < 75:
                    c = 'BB'
                elif toplam >= 65 and toplam < 70:
                    c = 'CB'
                elif toplam >= 60 and toplam < 65:
                    c = 'CC'
                elif toplam >= 55 and toplam < 60:
                    c = 'DC'
                elif toplam >= 50 and toplam < 55:
                    c = 'DD'

            else:
                c = 'FF'

            sorguu = "UPDATE {} SET Vize = {},Final = {} WHERE OgrenciNumara= {}".format(sinifad,int(vizee),int(finall),no)

            self.cursor.execute(sorguu)
            sorgu = " UPDATE {} SET HarfNotu = '{}', Ortalama ='{}' WHERE OgrenciNumara = {}".format(sinifad,c ,toplam, no)
            self.cursor.execute(sorgu)
            self.baglanti.commit()

    def harfNotuHesapla(self,notd,noo):

        sorgu = "SELECT * FROM {}".format(notd)
        self.cursor.execute(sorgu)
        notlar = self.cursor.fetchall()
        sorgu2 = "SELECT * FROM dersler"
        self.cursor.execute(sorgu2)
        dersler = self.cursor.fetchall()

        for i in dersler:

            if i[0] == notd:

                if i[7] == noo:

                    if len(notlar):

                        print("HEsaplanıcak not yok!")

                    else:

                        renkliYıldız()

                        for a in notlar:

                            vize = a[3] * i[4]
                            final = a[4] * i[5]
                            toplam = vize + final
                            ortalama = i[4] * a[3] + i[5] * a[4]

                            if toplam >= 50:

                                if (toplam >= 85 and toplam >= 50):
                                    c = 'AA'
                                elif toplam >= 75 and toplam < 85:
                                    c = 'BA'
                                elif toplam >= 70 and toplam < 75:
                                    c = 'BB'
                                elif toplam >= 65 and toplam < 70:
                                    c = 'CB'
                                elif toplam >= 60 and toplam < 65:
                                    c = 'CC'
                                elif toplam >= 55 and toplam < 60:
                                    c = 'DC'
                                elif toplam >= 50 and toplam < 55:
                                    c = 'DD'

                            else:
                                c = 'FF'

                            renkliYıldız()

                            sorgu2 = "UPDATE {} SET HarfNotu = '{}',Ortalama = '{}' WHERE OgrenciNumara = {}".format(
                                notd,
                                c,
                                ortalama,
                                a[2])
                            self.cursor.execute(sorgu2)
                            self.baglanti.commit()

    def Mesaj(self,maill):
        #MESAJI BANKO GÖNDERİYOR RAHATS
        mesaj = MIMEMultipart()

        mesaj["From"] = "talhaucrr@gmail.com"
        print(maill)
        mesaj["To"] = maill


        mesaj["Subject"] = "Not Girisi"

        print(self.a)

        yazi = "Notunuz Girildi!"

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


        except:

            sys.stderr.write("*****\n")
            sys.stderr.write("Mail gönderilemedi bir sorun oluştu!!\n")
            sys.stderr.write("*****")
            sys.stderr.flush()

class OgrenciKontrol():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti=sqlite3.connect("Ogrenciler.db")
        self.cursor=self.baglanti.cursor()
        self.baglanti.commit()

    def baglantiyi_kes(self):

        self.baglanti.close()

    def notGoruntule(self,ogrenciNo):

        sorgu = "SELECT * FROM dersler "
        self.cursor.execute(sorgu)
        dersler = self.cursor.fetchall()

        print("------------------------------------------------------------------------------")

        for i in dersler:

            sorgu2 = "SELECT * FROM {}".format(i[1])
            self.cursor.execute(sorgu2)
            notlar = self.cursor.fetchall()

            for a in notlar:

                if a[2] == ogrenciNo:

                    print("|Ders Adı: {} | Kredi: {} | Vize: {} | Final: {} | Harf Notu: {}|".format(i[1],i[3],a[3],a[4],a[5]))
                    print("------------------------------------------------------------------------------")

        self.baglanti.commit()

    def transKript(self):

        """sözlük = {"AA":4.00,"BA":3.50,"BB":3.00,"CB":2.50,"CC":2.00,"DC":1.50,"FF":0.00}

        krediToplamı = 0
        krediToplamı2 = 0"""
        liste = list()

        sorgu = "SELECT * FROM dersler "
        self.cursor.execute(sorgu)
        dersler = self.cursor.fetchall()

        print("------------------------------------------------------------------------------")

        for i in dersler:

            dosyaOku = open("OgrenciNotemp.txt")
            ogrenciNo = dosyaOku.read()

            sorgu2 = "SELECT * FROM {}".format(i[1])
            self.cursor.execute(sorgu2)
            notlar = self.cursor.fetchall()

            for a in notlar:

                if a[2] == int(ogrenciNo):

                    liste.append(a)
                    """krediToplamı = krediToplamı + sözlük[a[5]]*i[3]
                    krediToplamı2 = krediToplamı2 + i[3]

                    #2 saat 3 kredi
                    print("Ders Adı: {}   |   Harf Notu: {}   |   Kredisi: {}".format(i[1],a[5],i[3]))
                    print("------------------------------------------------------------------------------")
        
        print("GANO: {}".format(float(krediToplamı/krediToplamı2)))
        print("------------------------------------------------------------------------------")"""
        print(liste)
        return liste


    def sınıfNot(self,ders):

        sorgu = "SELECT * FROM dersler"
        self.cursor.execute(sorgu)
        dersler = self.cursor.fetchall()

        print("-------------------------------------------------------------------------------------------------------------------")

        for i in dersler:


            if ders == i[1]:

                sorgu2 = "SELECT * FROM {} ORDER BY Ortalama DESC ".format(i[1])#DESC(BÜYÜKTEN KÜÇÜĞE),ASC(KÜÇÜKTEN BÜYÜĞE)
                #AÇILAN DERSE HARF NOTUNUN YANINA ORTALAMA GİR
                #ORTALAMAYA GÖRE SIRALAT


                self.cursor.execute(sorgu2)
                siralama = self.cursor.fetchall()

                for a in siralama:


                    print("|Öğrenci Adı: {}      |      Vize: {}      |      Final: {}      |      Ortalama: {}      |      Harf Notu: {}|".format(a[0],a[3],a[4],a[6],a[5]))
                    print(
                        "-------------------------------------------------------------------------------------------------------------------")
    def sinifNott(self):

        liste = list()
        dosyaOku = open("OgrenciNotemp.txt")
        no = dosyaOku.read()
        print(no)
        sorgu = "select * from dersler"
        self.cursor.execute(sorgu)
        dersler = self.cursor.fetchall()

        for i in dersler:
            print(i[1])
            liste.append(i[1])
        print(self.sinifNott2(liste,no))
        return self.sinifNott2(liste,no)

    def sinifNott2(self,liste,no):

        liste2=list()
        for i in liste:

            sorgu2 = "select * from {}".format(i)
            self.cursor.execute(sorgu2)
            ogr = self.cursor.fetchall()
            if len(ogr) == 0:
                pass
            else:
                for a in ogr:

                    if a[2] == int(no):
                        liste2.append(i)

        return liste2
