class AracBilgileri():
    def __init__(self,motor_hacmi,silindir_sayisi,vites_turu):
        self.motor_hacmi = motor_hacmi
        self.silindir_sayisi = silindir_sayisi
        self.vites_turu = vites_turu

class Arac(AracBilgileri):
    def __init__(self,motor_hacmi,silindir_sayisi,vites_turu,renk,kasa_tipi,model):
        super().__init__(motor_hacmi,silindir_sayisi,vites_turu)
        self.renk = renk
        self.kasa_tipi = kasa_tipi
        self.model = model
    def BilgileriGoster(self):
        print("""
        Aracın motor hacmi: {}
        Aracın silindir sayısı: {}
        Aracın vites türü: {}
        Aracın rengi: {}
        Aracın kasa tipi: {}
        Aracın modeli: {}
        """.format(self.motor_hacmi,self.silindir_sayisi,self.vites_turu,self.renk,self.kasa_tipi,self.model))

print("Arac bilgilerini giriniz: ")
a = int(input("Motor Hacmi: "))
b = int(input("Silindir Sayısı: "))
c = input("Vites Türü: ")
d = input("Rengi: ")
e = input("Kasa Tipi: ")
f = int(input("Modeli: "))
Arac1 = Arac(a,b,c,d,e,f)
Arac1.BilgileriGoster()