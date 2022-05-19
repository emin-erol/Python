from tkinter import *
p = Tk()
p.title("Hastane Otomasyonu")
p.geometry("1920x1080")

Klinikler = ["CİLDİYE","DAHİLİYE","NÖROLOJİ","ÜROLOJİ","KBB","GÖZ"]
Klinik_isimleri = list(Klinikler)

for i in range(6):
    Klinikler[i] = Button(p)

def Kayit():
    Yazi1.config(text="KLİNİKLER")
    Yazi1.place(x=730,y=100)
    Buton1.destroy()
    k = 0

    y1 = 300
    for i in range(3):
        x1 = 400
        for j in range(2):
            Klinikler[k].config(text=Klinik_isimleri[k],font="Times 36 bold",bg="Yellow",width=10)
            Klinikler[k].pack()
            Klinikler[k].place(x=x1,y=y1)
            k += 1
            x1 += 700
        y1 += 200


Yazi1 = Label(p,text="- HASTANE OTOMASYONU -",font="Times 48 bold")
Yazi1.pack()
Yazi1.place(x=450,y=300)
Buton1 = Button(p,text="SIRA AL",font="Times 36 bold",bg="Yellow",command=Kayit)
Buton1.pack()
Buton1.place(x=800,y=500)


p.mainloop()