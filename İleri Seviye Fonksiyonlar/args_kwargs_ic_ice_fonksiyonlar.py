def args_kullanimi(*args): # Gönderilen değişkenlerin hepsini bir demette tutup işlem yapar.
    for i in args:
        print(i)
args_kullanimi(1,2,3,4,5,6,7)

def kwargs_kullanimi(**kwargs): # Gönderilen nesneleri isimleriyle beraber alıp bir sözlüğe aktararak işlem yapar.
    for i,j in kwargs.items():
        print(i,":",j)
kwargs_kullanimi(ad="Emin",soyad="Erol",yas=21)

def fonksiyon(*args): # 1 den 7 ye kadar olan sayıları bir demette tuttu
    def toplama(args): # demeti alan fonksiyon her bir elemanı toplayarak bir toplam değeri return etti
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(toplama(args)) # demet alt fonksiyona gönderildi
fonksiyon(1,2,3,4,5,6,7)