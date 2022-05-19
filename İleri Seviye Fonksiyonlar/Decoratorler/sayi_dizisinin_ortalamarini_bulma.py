def Ekstra(fonk):
    def wrapper(sayilar):
        CiftlerAdedi = 0
        CiftlerToplami = 0
        TeklerAdedi = 0
        TeklerToplami = 0
        for i in sayilar:
            if(i%2 == 0):
                CiftlerToplami += i
                CiftlerAdedi += 1
            else:
                TeklerToplami += i
                TeklerAdedi += 1
        print("Tek sayilarin ortalamasi = {:.2f}".format(TeklerToplami/len(sayilar)))
        print("Cift sayilarin ortalamasi = {:.2f}".format(CiftlerToplami/len(sayilar)))
        fonk(sayilar)
    return wrapper

@Ekstra
def OrtalamaBul(sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    print("Genel ortalama = {:.2f}".format(toplam/len(sayilar)))

ornek1 = OrtalamaBul([12,54,4,8,41,63])