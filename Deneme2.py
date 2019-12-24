kAdi = "sa"
sifre = "sa"
rasgele=123


dosya = open("Bilgilerr.txt","w")
dosya.write("{} {} {}".format(kAdi,sifre,rasgele))
dosya.close()

dosya2= open("Bilgilerr.txt","r")
temp = dosya2.readlines()
for i in temp:
    a = i.split(" ")
print(a[0])
print(a[1])
print(a[2])

dosya2.close()