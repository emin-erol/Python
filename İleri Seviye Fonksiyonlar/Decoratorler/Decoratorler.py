import time

def KareHesapla(sayilar):
    sonuc = []
    baslama = time.time()
    for i in sayilar:
        sonuc.append(i ** 2)
    bitis = time.time()
    print("Bu fonksiyon ",str(bitis-baslama),"saniye surdu.")
    return sonuc

def KupHesapla(sayilar): # Süre hesaplama için her gerekli kod iki fonksiyonda da yazıldı ve kod tekrarı yaşandı
    sonuc = []
    baslama = time.time()
    for i in sayilar:
        sonuc.append(i ** 3)
    bitis = time.time()
    print("Bu fonksiyon ", str(bitis - baslama), "saniye surdu.")
    return sonuc

KareHesapla(range(100000))
KupHesapla(range(100000))

def ZamanHesapla(fonk): # Her fonksiyonda kulanabileceğimiz şekilde bir zaman hesaplama decorator fonksiyonu oluşturduk
    def wrapper(sayilar):
        baslama = time.time()
        sonuc = fonk(sayilar)
        bitis = time.time()
        print(fonk.__name__,"fonksiyonu,",str(bitis-baslama),"saniye surdu")
        return sonuc
    return wrapper

@ZamanHesapla
def KareHesapla(sayilar):
    sonuc = []
    for i in sayilar:
        sonuc.append(i ** 2)
    return sonuc

@ZamanHesapla
def KupHesapla(sayilar):
    sonuc = []
    for i in sayilar:
        sonuc.append(i ** 3)
    return sonuc

KareHesapla(range(100000))
KupHesapla(range(100000))