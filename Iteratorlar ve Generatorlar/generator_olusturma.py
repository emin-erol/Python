def kareleriAl(): # 1'den 6'ya kadar olan sayıların karelerini hesaplayıp klasik yolla bellekte tutma
    sonuc = []
    for i in range(1,6):
        sonuc.append(i**2)
    return sonuc

print(kareleriAl())

def kareleriAl(): # 1'den 6'ya kadar olan sayıları kullanıcı çağırdıktan sonra sırasıyla üretebilen fonksiyon
    for i in range(1,6):
        yield i**2

generator = kareleriAl() # Fonksiyondaki değerleri tutabilecek bir generator oluşturduk
iterator = iter(generator) # Oluşturulan generatorda gezinebilmek için iterator oluşturduk
print(next(iterator)) # iteratorun ilk elemanına erişim sağlamak istedik

generator2 = liste = (i**2 for i in range(1,6)) # Köşeli parantezler yerimne normal parantezler kullanarak
                                               # list comprehension yöntemi ile generator oluşturabiliriz.
iterator2 = iter(generator2)
print(next(iterator2))
print(next(iterator2))
