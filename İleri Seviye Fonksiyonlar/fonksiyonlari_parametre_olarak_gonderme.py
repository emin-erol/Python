def Toplama(a,b):
    return a+b

def Cikarma(a,b):
    return a-b

def Carpma(a,b):
    return a*b

def Bolme(a,b):
    return a/b

def AnaFonksiyon(fonk1,fonk2,fonk3,fonk4,IslemTuru):
    if(IslemTuru == "+"):
        print(fonk1(4,7))
    elif(IslemTuru == "-"):
        print(fonk2(8,5))    # İşlem türüne göre belirli fonksiyonu çağırma
    elif(IslemTuru == "*"):
        print(fonk3(3,4))
    elif(IslemTuru == "/"):
        print(fonk4(20,4))
    else:
        print("Gecersiz işlem türü!")

IslemTipi = input("İşlem türünü giriniz: ")
ornek1 = AnaFonksiyon(Toplama,Cikarma,Carpma,Bolme,IslemTipi) # Her işlem fonksiyonu ana fonksiyona parametre
                                                              # olarak gönderildi.