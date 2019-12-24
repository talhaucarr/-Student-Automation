from OgrenciKayit import *

ogrencii = OgrenciKayit()
ogrenci2 = OgrenciKontrol()##OGRENCİ2 YERİNE DAHA MANTIKLI ŞEY KOY

def renkliYıldız():
    print("\033[" + str(96) + "m" + "*****" + "\033[0m")
def uzunRenkliYıldız():
    print("\033[" + str(96) + "m" + "*************************************" + "\033[0m")
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
def anaGiris2(isim,No):

    while True:

        uzunRenkliYıldız()
        print("""
        Merhaba {}, Öğrenci Bilgi Sistemine Hoşgeldin.

        1. Not Görüntüle
        
        2. Sınıf Not Durumu
   
        3. Transkript

        Geri dönmek için 'z', çıkmak için 'q' ya basınız.
        """.format(isim))

        uzunRenkliYıldız()

        işlemm = input("İşleminizi Seçiniz:")

        if işlemm == 'q':

            Cikis()

        elif işlemm == 'z':

            break

        elif işlemm == '1':

            No = No[1:]
            ogrenci2.notGoruntule(int(No))

        elif işlemm == '2':

            ogrenci2.sınıfNot('Mat1')

        elif işlemm == '3':

            No = No[1:]
            ogrenci2.transKript(int(No))

        else:

            renkliYıldız()
            print("Hatali seçim!")
            renkliYıldız()
        #import os
        #os.startfile("C:/Users/TestFile.txt", "print") YAZICIDAN TRANSKRİPT CIKTISI ALMAK İÇİN

