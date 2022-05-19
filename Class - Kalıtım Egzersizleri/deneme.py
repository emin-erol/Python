class Ogrenci():
    def __init__(self,ad,soyad,ogr_no):
        self.ad = ad
        self.soyad = soyad
        self.ogr_no = ogr_no
    def Dersler(self):
        print("""
        Dersler:\n
            1.) Turk Dili ve Edebiyatı
            2.) Tarih
            3.) Mesleki İngilizce""",end="")
    def BilgileriGoster(self):
        print("""
        Bilgiler:\n
            Öğrenci Adı: {}
            Soyadı :{}
            Okul Numarası: {}""".format(self.ad, self.soyad, self.ogr_no))

class BirinciSinif(Ogrenci):
    def Dersler(self):
        super().Dersler()
        print("""
            4.)Fizik 1
            5.)Matematik 1
            6.)Algoritma ve Programlama
            7.)Bilgisayar Mühendisliğine Giriş""")
    def TatilGunleri(self):
        print("\n\t\tTatil Günleri: Perşembe ve Cuma")

class IkinciSinif(Ogrenci):
    def __init__(self,ad,soyad,ogr_no,ort1):
        super().__init__(ad,soyad,ogr_no)
        self.ort1 = ort1
    def Dersler(self):
        super().Dersler()
        print("""
            4.)Fizik 2
            5.)Matematik 2
            6.)Nesne Yönelimli Programlama
            7.)Veri Yapıları""")
    def TatilGunleri(self):
        print("\n\t\tTatil Günleri: Pazartesi ve Çarşamba")
    def BilgileriGoster(self):
        super().BilgileriGoster()
        print("\n\t\t\t1. Sınıf Ortalaması: {}".format(self.ort1))

class UcuncuSinif(Ogrenci):
    def __init__(self,ad,soyad,ogr_no,ort1,ort2):
        super().__init__(ad,soyad,ogr_no)
        self.ort1 = ort1
        self.ort2 = ort2
    def Dersler(self):
        super().Dersler()
        print("""
            4.)Ayrık Matematik
            5.)Lineer Cebir
            6.)Olasılık ve İstatistik
            7.)Web Programlama""")
    def TatilGunleri(self):
        print("\n\t\tTatil Günleri: Persembe")
    def BilgileriGoster(self):
        super().BilgileriGoster()
        print("""
            1. Sınıf Ortalaması: {}
            2. Sınıf Ortalaması: {}""".format(self.ort1,self.ort2))

class DorduncuSinif(Ogrenci):
    def __init__(self,ad,soyad,ogr_no,ort1,ort2,ort3):
        super().__init__(ad,soyad,ogr_no)
        self.ort1 = ort1
        self.ort2 = ort2
        self.ort3 = ort3
    def Dersler(self):
        super().Dersler()
        print("""
            4.)Lojik Devreler
            5.)Elektronik Devreler
            6.)Mikro İşlemciler""")
    def TatilGunleri(self):
        print("\n\t\tTatil Günleri: Cuma")
    def BilgileriGoster(self):
        super().BilgileriGoster()
        print("""
            1. Sınıf Ortalaması: {}
            2. Sınıf Ortalaması: {}
            3. Sınıf Ortalaması: {}""".format(self.ort1,self.ort2,self.ort3))

a = input("Ogrenci Adı: ")
b = input("Soyadı: ")
c = int(input("Okul Numarası: "))
d = int(input("Sınıfı: "))
if(d == 1):
    ogr = BirinciSinif(a,b,c)
    ogr.BilgileriGoster()
    ogr.Dersler()
    ogr.TatilGunleri()
elif(d == 2):
    e = float(input("Öğrencinin 1. Sınıf Ortalaması: "))
    ogr = IkinciSinif(a,b,c,e)
    ogr.BilgileriGoster()
    ogr.Dersler()
    ogr.TatilGunleri()
elif(d == 3):
    e = float(input("Öğrencinin 1. Sınıf Ortalaması: "))
    f = float(input("Öğrencinin 2. Sınıf Ortalaması: "))
    ogr = UcuncuSinif(a,b,c,e,f)
    ogr.BilgileriGoster()
    ogr.Dersler()
    ogr.TatilGunleri()
elif(d == 4):
    e = float(input("Öğrencinin 1. Sınıf Ortalaması: "))
    f = float(input("Öğrencinin 2. Sınıf Ortalaması: "))
    g = float(input("Öğrencinin 3. Sınıf Ortalaması: "))
    ogr = DorduncuSinif(a,b,c,e,f,g)
    ogr.BilgileriGoster()
    ogr.Dersler()
    ogr.TatilGunleri()