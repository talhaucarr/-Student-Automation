from OgrenciKayit import *

import random

ogrenci = OgrenciKayit()
snf = SinifKayit()
derss = DersKayit()

def uzunRenkliYıldız():
    print("\033[" + str(96) + "m" + "*************************************" + "\033[0m")

def renkliYıldız():
    print("\033[" + str(96) + "m" + "*****" + "\033[0m")

def rastgele():

    a = random.randint(100,1000)
    return a

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

def anaGiris(aD):
    while True:

        uzunRenkliYıldız()
        print("""
        Merhaba {}, Öğretmen Bilgi Sistemine Hoşgeldin.

        1. Sınıf İşlemleri

        2. Öğrenci İşlemleri

        3. Ders İşlemleri

        Çıkmak için 'q' ya basınız.
        """.format(aD))
        uzunRenkliYıldız()


        işlem3 = input("Ana menü işleminizi giriniz:")

        if işlem3 == 'q':

            Cikis()

        elif işlem3 == '1':

            uzunRenkliYıldız()
            print("""
        Sınıf İşlemleri.
            
        İşlemler;

        1. Sınıfları Göster

        2. Sınıf Ara

        3. Sınıf Ekle

        Geri dönmek için 'z', çıkmak için 'q' ya basınız.
    """)
            uzunRenkliYıldız()
            while True:

                işlem4 = input("Sınıf işleminizi seçiniz:")

                if işlem4 == 'q':

                    Cikis()

                elif işlem4 == 'z':

                    break

                if işlem4 == '1':

                    snf.siniflari_goster()

                elif işlem4 == '2':

                    sinifadi = input("Sınıf adını giriniz:")
                    renkliYıldız()
                    print("Sınıf araniyor...")
                    renkliYıldız()
                    time.sleep(1)
                    snf.sinifAra(sinifadi)

                elif işlem4 == '3':

                    rast = (random.randint(1000, 10000))

                    snfad = input("Sınıf Adı:")
                    yeni_sinif = Sinif(snfad.upper(),rast)
                    renkliYıldız()
                    print("Sınıf oluşturuluyor...")
                    time.sleep(1)
                    snf.sinifEkle(yeni_sinif)
                    renkliYıldız()
                    print("Sınıf Oluşturuldu!")
                    renkliYıldız()

        elif işlem3 == '2':

            uzunRenkliYıldız()
            print("""
        Öğrenci İşlemleri.

        İşlemler;

        1. Öğrencileri Göster

        2. Öğrenci Sorgulama

        3. Öğrenci Ekle

        Geri dönmek için 'z', çıkmak için 'q' ya basınız.
""")
            uzunRenkliYıldız()

            while True:

                işlem = input("Öğrenci işleminizi giriniz:")

                if işlem == 'q':

                    Cikis()

                elif işlem == 'z':

                    break

                elif işlem == '1':

                    ogrenci.ogrencileri_goster()

                elif işlem == '2':

                    isim = input("Hangi öğrenciyi istiyorsunuz:")
                    renkliYıldız()
                    print("Öğrenci araniyor...")
                    renkliYıldız()
                    time.sleep(1)
                    ogrenci.ogrenciArat(isim.capitalize())

                elif işlem == '3':

                    ad = input("Ogrenci Adı:")
                    soyad = input("Ogrenci Soyadı:")
                    no = input("Ogrenci No:")
                    sinif = input("Sınıf:")
                    email = input("Email:")
                    yeni_ogrenci = Ogrenci(ad.capitalize(), soyad.capitalize(), no, sinif,
                                           email)
                    ogrenci.ogrenciEkle(yeni_ogrenci)

                else:

                    renkliYıldız()
                    print("Geçersiz işlem!")
                    renkliYıldız()

        elif işlem3 == '3':

            while True:
                uzunRenkliYıldız()
                print("""
        Not İşlemleri.
            
        İşlemler;

        1. Ders Ekle

        2. Mevcut Dersleri Gör

        3. Ders Sorgula

        4. Not Girişi

        5. Harf Notu Hesaplama

        Geri dönmek için 'z', çıkmak için 'q' ya basınız.
    """)
                uzunRenkliYıldız()

                işlem5 = input("Not işleminizi seçiniz:")

                if işlem5 == 'q':

                    Cikis()

                elif işlem5 == 'z':

                    break

                elif işlem5 == '1':

                    dersad = input("Ders Adı:")
                    derssaat = int(input("Ders Saati:"))
                    derskredi = int(input("Ders Kredisi:"))
                    dersVize = float(input("Dersin Vize Ağırlığı:"))
                    dersFinal = float(input("Dersin Final Ağırlığı:"))
                    dersOgr = input("Ders Öğretmeni:")
                    dersSnf = input("Dersi Açmak İstediğiniz Sınıfı Giriniz:")

                    if (dersVize+dersFinal == 1):

                        yeni_ders = Ders(rastgele(), dersad.capitalize(), derssaat, derskredi, dersVize, dersFinal, dersOgr.capitalize(),dersSnf)
                        derss.dersEkle(yeni_ders)

                    else:

                        renkliYıldız()
                        print("Final ve Vizenin toplamı 1.00'ın altında kalıyor!")


                elif işlem5 == '2':

                    derss.dersleri_goster(aD)

                elif işlem5 == '3':

                    ders41 = input("Aratmak istediğiniz dersin adını giriniz:")

                    derss.dersSorgula(ders41)

                elif işlem5 == '4':

                    renkliYıldız()
                    giris = int(input("Not Girişi İçin Sınıf Kodunu Giriniz:"))
                    derss.notGirisi(giris,aD)

                elif işlem5 == '5':

                    renkliYıldız()
                    giris = int(input("Harf Notunu Hesaplamak İçin Sınıf Kodunu Giriniz:"))
                    derss.harfNotuHesapla(giris,aD)
                    renkliYıldız()
                    print("Hesaplama Başarılı!")

        else:

            renkliYıldız()
            print("Geçersiz İşlem!")
            renkliYıldız()



