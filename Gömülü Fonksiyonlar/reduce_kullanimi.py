from functools import reduce

a = reduce(lambda x,y:x*y,[1,2,3,4,5])
print(a)
# listenin solundan baslayarak 2 indisi fonksiyondaki isleme sokarak devam eder ve sonuncunda bir deger dondurur