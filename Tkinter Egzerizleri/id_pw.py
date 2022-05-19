from tkinter import *

pencere = Tk()
pencere.title("Final Dosyası")
id = "coolsheytan"
pw = "mhvp45341"

idBasligi = Label(pencere,text="Kullanıcı Adı:",bg="Yellow",font=("Calibri",16))
idSorgusu = Entry(font=("Calibri",16))
sifreBasligi = Label(pencere,text="Şifre: ",bg="Yellow",font=("Calibri",16))
sifreSorgusu = Entry(font=("Calibri", 16))
UyariNotu = Label(pencere,text="Kullanıcı adı veya parola hatalı, yeniden deneyiniz.",bg="Red",font=("Calibri",16))

def GirisKontrol():
    KullaniciAdi = idSorgusu.get()
    sifre = sifreSorgusu.get()
    if(id == KullaniciAdi and pw == sifre):
        idBasligi.destroy()
        idSorgusu.destroy()
        sifreBasligi.destroy()
        sifreSorgusu.destroy()
        OnaylaButonu.destroy()
        UyariNotu.destroy()
        BasariNotu = Label(pencere,text="GİRİŞ BAŞARILI!",bg="Green",font=("Calibri",36))
        BasariNotu.pack()
        BasariNotu.place(x=800,y=350)
    if(id != KullaniciAdi or pw != sifre):
        UyariNotu.pack()
        UyariNotu.place(x=400,y=300)


OnaylaButonu = Button(pencere,text="ONAYLA",bg="Green",font=("Calibri",16),command=GirisKontrol)
def GirisYap():
    GirisYazisi.destroy()
    GirisButonu.destroy()
    CikisButonu.destroy()
    idBasligi.pack()
    idBasligi.place(x=400,y=400)
    idSorgusu.pack()
    idSorgusu.place(x=550,y=400)
    sifreBasligi.pack()
    sifreBasligi.place(x=400,y=500)
    sifreSorgusu.pack()
    sifreSorgusu.place(x=550,y=500)
    OnaylaButonu.pack()
    OnaylaButonu.place(x=500,y=600)

def CikisYap():
    pencere.destroy()
GirisYazisi = Label(pencere,text="...HOŞGELDİNİZ...",bg="Yellow",font=("Calibri",36))
GirisYazisi.pack()
GirisYazisi.place(x = 700,y=350)
GirisButonu = Button(pencere,text="GİRİŞ",bg="Green",font=("Calibri",24),command=GirisYap)
GirisButonu.pack()
GirisButonu.place(x=700,y=500)
CikisButonu = Button(pencere,text="ÇIKIŞ",bg="Red",font=("Calibri",24),command=CikisYap)
CikisButonu.pack()
CikisButonu.place(x=1020,y=500)
pencere.mainloop()