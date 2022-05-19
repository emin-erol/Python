def BasamakToplama(fonk):
    def wrapper(a,b):
        basamak_toplami = (fonk(a,b)%10) + (fonk(a,b)//10)
        print("Sonuc:",fonk(a,b))
        print("Basamak Toplami:",basamak_toplami)
        fonk(a,b)
    return wrapper

@BasamakToplama
def Toplama(a,b):
    return a+b
@BasamakToplama
def Cikarma(a,b):
    return a-b
@BasamakToplama
def Carpma(a,b):
    return a*b
@BasamakToplama
def Bolme(a,b):
    return a/b

while True:
    a,opr,b = input("Islemi giriniz: ").split()
    a = int(a)
    b = int(b)
    if(opr == "+"):
        islem = Toplama(a,b)
    elif(opr == "-"):
        islem = Cikarma(a,b)
    elif(opr == "*"):
        islem = Carpma(a,b)
    elif(opr == "/"):
        islem = Bolme(a,b)
    else:
        print("Gecersiz islem!")