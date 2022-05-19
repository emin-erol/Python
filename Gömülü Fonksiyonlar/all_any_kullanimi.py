liste1 = [1,2,3,4,5] # Hepsi True değerli liste
liste2 = [True,False,True,True] # İçinde bir tane False bulundran liste
liste3 = [0,0,0,0,0] # Hepsi False değerli liste
print(all(liste1)) # İçindeki listenin her elemanı True değerli ise True değer döndürür
print(any(liste2)) # İçindeki listenin elemanlarından herhangi birinin True olması True değer döndürtür