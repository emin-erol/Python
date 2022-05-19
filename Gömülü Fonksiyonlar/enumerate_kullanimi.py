a = list(enumerate(["Emin","Zehra","Rahime","Fevziye"]))
print(a)
# liste icinde demet olustararak her bir demete ilgili listenin indisi ve indis numarası kaydedilir

liste = ["a","b","c","d","e","f","g"]
for i,j in enumerate(liste):
    if(i%2 == 0):
        print(j)

# for icinde gonderilen listenin indis numaralari cift olan elemanlari yazdirdik