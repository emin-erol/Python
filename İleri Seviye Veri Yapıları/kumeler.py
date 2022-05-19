x = set("Emin Erol")
print(x)

y = {1,2,3,4,5} # Kume olusturduk
y = list(y) # Elemana erişebilmek için liste formatına çevirdik
print(y[0])

a = {1,2,3,4}
a.add(5) # a kümesine '5' elemanını ekledik eğer kümede zaten olsaydı ekleme olmazdı
print(a)

b = {2,4,5,6,7}
print(a.difference(b)) # a/b işlemini gerçekleştirir

a.difference_update(b) # a/b işlemini yapıp sonucunu a kümesi olarak eşitler
print(a)

b.discard(7) # b kümesinden içine girilen değer çıkarılır eğer kümede yoksa bir şey değişmez
print(b)

k1 = {1,3,5,7,9}
k2 = {1,2,3,4,5}
print(k1.intersection(k2)) # k1 n k2 işlemini yapar

k1.intersection_update(k2) # k1 n k2 işlemini yapıp sonucu k1 kümesine eşitler
print(k1)

kume1 = {17,23,42,51,77}
kume2 = {81,99,64,55,78}
kume3 = {42,11,77,32,44}
print(kume1.isdisjoint(kume2)) # girilen kümelerin kesişim kümesi var ise false yoksa True döndürür
print(kume1.isdisjoint(kume3)) # 1 ve 3. kümelerin kesişimleri olduğundan false değer döndürür

a = {1,2,3}
b = {1,2,3,4,5,6}
print(a.issubset(b)) # a kümesi b kümesinin alt kümesi ise True değilse False değer dündürür

print(kume1.union(kume2)) # kume1 U kume2 işlemini yapar

