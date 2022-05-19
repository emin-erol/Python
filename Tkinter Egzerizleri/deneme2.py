from tkinter import *
pencere = Tk()
pencere.title("Şifre Kontrol Uygulaması")
pencere.geometry("400x700")
pw = "uxvjp.911"
def SifreKontrol():
    sifre = sifre_entry.get()
    sifre_entry.destroy()
    sifre_label.destroy()
    giris_button.destroy()
    cikis_button.destroy()
    if(pw == sifre):
        giris_label.config(text="Giriş Başarılı",bg="green")
    else:
        giris_label.config(text="SIKTIRGIT",bg="black",fg="white")

def cikis():
    giris_label['text'] = "PROGRAM KAPATILIYOR"
    pencere.after(2000,pencere.destroy())
pencere.protocol("WM_DELETE_WINDOW",cikis)
giris_label = Label(text="HOSGELDINIZ",bg="yellow",font=("Consolas",24))
giris_label.pack()
giris_label.place(x=800,y=150)
sifre_label = Label(text="Şifre giriniz: ",font=("Consolas",16))
sifre_label.pack()
sifre_label.place(x=100,y=300)
sifre_entry = Entry(font=("Consolas",16))
sifre_entry.pack()
sifre_entry.place(x=320,y=300)
giris_button = Button(text="GİRİŞ",bg="green",font=("Consolas",20),command=SifreKontrol)
giris_button.pack()
giris_button.place(x=200,y=400)
cikis_button = Button(text="ÇIKIŞ",bg="red",font=("Consolas",20),command=cikis)
cikis_button.pack()
cikis_button.place(x=400,y=400)
mainloop()