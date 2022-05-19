class BankaHesabi():
    def __init__(self,isim,hesap_no,bakiye=0):
        self.isim = isim
        self.hesap_no = hesap_no
        self.bakiye = bakiye
        self.banka = "Ziraat Bankası"
    def Yatirma(self,miktar):
        self.bakiye += miktar
    def Cekme(self,miktar):
        if(miktar <= self.bakiye):
            self.bakiye -= miktar
        else:
            print("Yeterli bakiyeniz bulunmamaktadır.")
    def BilgileriYazdir(self):
        print("""
                {}
            Sayın {}, hesap bilgileriniz;
            Hesap Numarası: {}
            Bakiye: {} """.format(self.banka,self.isim,self.hesap_no,self.bakiye))
a,b = input("Kullanıcının adını ve hesap numarasını giriniz: ").split(",")
BankaHesabi1 = BankaHesabi(a,b)

while 1:
    secim = input("""
        1.) Bilgilerimi Göster
        2.) Para Yatırma
        3.) Para Çekme
        İşlemi tuşlayınız: 
    """)
    try:
        secim = int(secim)
    except:
        pass
    if(secim == 1):
        BankaHesabi1.BilgileriYazdir()
    elif(secim == 2):
        m = int(input("Yatırılacak miktarı giriniz: "))
        BankaHesabi1.Yatirma(m)
    elif(secim == 3):
        m = int(input("Çekilecek miktarı giriniz: "))
        BankaHesabi1.Cekme(m)
    elif(secim == 4):
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz işlem.")

