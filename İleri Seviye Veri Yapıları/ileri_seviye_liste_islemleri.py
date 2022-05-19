l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2) # l2 listesini l1 listesine ekler
print(l1)

l2.insert(0,3) # belirtilen indekse belirtilen değer atanır örnekte 0. indekse '3' değeri atandı
print(l2)

print(l1.pop()) # içine indeks değeri girilmediğinde son elemanı silip kendinde tutar
print(l1)

a = [123,23,131,3,2]
a.remove(23) # içine girilen değeri listeden siler eğer değer listede yoksa hata verir
print(a)

a = [1,3,2,6,7,5,3,5,3,2,5,7,4,2]
print(a.index(7)) # 7 değerini baştan başlayarak kaçıncı indiste olduğunu bulup yazar
print(a.index(5,3,6)) # 5 değerini 3. ve 6. indis arasında arar varsa yazar yoksa hata verir

print(a.count(3)) # içine girilen değerin listede kaç tane olduğunu yazar hiç yoksa 0 yazar

a.sort() # a listesini küçükten büyüğe doğru sıralar
print(a)
a.sort(reverse=True) # reverse durumu True olduğunda büyükten küçüğe doğru sıralama yapar
print(a)

