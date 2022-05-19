def MukemmeleriBul(fonk):
    def wrapper(sayilar):
        MukemmelSayilar = []
        for i in sayilar:
            bolenler_toplami = 0
            for j in range(1,i):
                if i%j == 0:
                    bolenler_toplami += j
            if(bolenler_toplami == i):
                MukemmelSayilar.append(i)
        print(MukemmelSayilar)
        fonk(sayilar)
    return wrapper

@MukemmeleriBul
def AsallariBul(sayilar):
    AsalSayilar = []
    for i in sayilar:
        if i == 1:
            continue
        else:
            sayac = 0
            for j in range(2,i):
                if(i%j == 0):
                    sayac += 1
            if sayac == 0:
                AsalSayilar.append(i)
    for i in AsalSayilar:
        print(i)
ornek1 = AsallariBul(range(1,1000))