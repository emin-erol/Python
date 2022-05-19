from datetime import datetime
print(datetime.now()) # .now() fonksiyonu şuanki zamanı gösterir.
su_an = datetime.now() # Şuanki zamanı bir değişkende tuttuk
print(su_an.year) # .year, .hour,.month gibi fonksiyonlar tarihteki ilgili kısmı tutar.
print(datetime.ctime(su_an)) # Girilen tarihi tutar.
print(datetime.strftime(su_an,"%Y")) # .strftime fonksiyonu tarihin belli bir kısım bilgisini alabilmek için kullanılır.
                                     # %Y = Yıl, %B = Ay, %D = Gün, %X = Saat, %A = Gün ismi
saniye = datetime.timestamp(su_an) # .timestamp, Girilen tarihin saniye cinsinden değerini verir.
print(saniye)
su_an2 = datetime.fromtimestamp(saniye) # .fromtimestamp, saniye cinsinden girilen tarihi normale çevirir.
print(su_an2)

tarih = datetime(2020,3,7) # Kullanıcının girdiği tarihi tutar.
print(su_an-tarih) # Kullanıcıdan alınan tarihin şimdiki zaman ile arasındaki farkı yazdırma işlemi.