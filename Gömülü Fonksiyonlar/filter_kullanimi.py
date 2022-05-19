a = list(filter(lambda x: x%2 == 0,[1,2,3,4,5,6,7,8,9,10]))
print(a)
# gonderilen listedeki elemanlardan fonksiyonda true deger alanlari filtreleme islemi yapar

def AsalMi(x): # gonderilen objeye gore asal ise True, değilse False degerini donduren fonksiyon
    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:
        i = 2
        while(i < x):
            if(x%i == 0):
                return False
            i += 1
        return True

b = list(filter(AsalMi,range(1,20)))
print(b)
# 1 den 20 ye kadar olan sayilar AsalMi() fonksiyonuna gonderilip degeri True olanlar b listesinde tutulur