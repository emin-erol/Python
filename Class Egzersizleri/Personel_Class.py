class Personel():
    def __init__(self,ad,soyad,yas,maas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.maas = maas
    def Yazdir(self):
        print("""
        Personelin Adı: {}
        Soyadı: {}
        Yaşı: {}
        Maaşı: {}""".format(self.ad,self.soyad,self.yas,self.maas))

adlar = []
soyadlar = []
yaslar = []
maaslar = []

a = int(input("Kayit sayisini giriniz: "))
for i in range(a):
    x = input("Personelin Adı: ")
    adlar.append(x)
    y = input("Soyadı: ")
    soyadlar.append(y)
    z = int(input("Yaşı: "))
    yaslar.append(z)
    t = int(input("Maaşı: "))
    maaslar.append(t)

objeler = []

for i in range(a):
    b = str(i)
    x = "Personel0".replace("0", b)
    objeler.append(x)
    objeler[i] = Personel(adlar[i],soyadlar[i],yaslar[i],maaslar[i])
    objeler[i].Yazdir()