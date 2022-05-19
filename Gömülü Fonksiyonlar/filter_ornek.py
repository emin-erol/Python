adet = int(input("Kayıt sayısını giriniz: "))
telNo = []
def Filtrele(numaralar):
    if(len(numaralar[0]) == 10):
        return True
    else:
        return False
for i in range(adet):
    a = input("Tel No Giriniz: ")
    telNo.append(a)
print(list(filter(Filtrele,telNo)))