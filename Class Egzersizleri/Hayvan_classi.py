class Hayvan():
    def __init__(self,isim,cins,ayak_sayisi):
        self.isim = isim
        self.cins = cins
        self.ayak_sayisi = ayak_sayisi
    def BilgileriGoster(self):
        print("""
        Hayvanın adı: {}
        Hayvanın Cinsi: {}
        Hayvanın Ayak Sayısı: {}""".format(self.isim,self.cins,self.ayak_sayisi))

a,b,c = input("Hayvanın Adını, Cinsini ve Ayak Sayısını Giriniz: ").split()
Hayvan1 = Hayvan(a,b,c)
Hayvan1.BilgileriGoster()