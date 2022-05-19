import os
print(os.getcwd()) # Bulunduğumuz dosyanın hangi dizinde olduğunu tutar.
print(os.listdir()) # Bulunduğumuz dizindeki dosyaları tutar.
# os.mkdir("mkdir_ornegi") # Bulunulan dizinde yeni bir dosya açmayı sağlar.
# os.makedirs("mkdir_ornegi2/basarili") # Bulunulan dizinde dosya içinde dosya açmayı sağlar.
# os.rmdir("mkdir_ornegi2/basarili") # Belirtilen yerdeki dosyayı siler.
# os.removedirs("mkdir_ornegi2/basarili") # Girilen dosyayı ve onun alt dosyalarını örnekteki gibi siler.
# os.rename("test1.txt","test2.txt") # Dizindeki belirtilen dosyanın adını girilen isim ile değiştirir.
print(os.stat("test2.txt")) # Girilen dosyanın tüm bilgilerini gösterir.
for a,b,c in os.walk("C:/Users/Pc/Desktop"): # Girilen dizindeki dosyaları gezer.
    for i in c:
        if(i.endswith(".txt")):
            print("Dosya Yolu:",a)
            print("Dosya Adı:",i)
            print("*"*30)