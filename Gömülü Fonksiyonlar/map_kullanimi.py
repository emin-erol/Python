def hesapla(x):
    return x**2
a = list(map(hesapla,(2,3,4,5)))
print(a)

# hesapla() fonksiyonuna liste gönderilerek fonksiyondaki işlemler listenin tüm elemanlarına uygulanır

l1 = [1,2,3,4]
l2 = [5,6,7,8]

b = list(map(lambda x,y: x*y,l1,l2))
print(b)
# l1 ve l2 listelerinin elemanlarini sirasiyla birbirleri ile toplama islemi yapilir