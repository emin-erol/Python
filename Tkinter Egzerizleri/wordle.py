from tkinter import *
import random
Kelimeler = [
"ABİDE","ABİYE","ACEMİ","AHİZE","AİDAT","AKTİF","AMİGO","ANTİK","ARAZİ","ARŞİV","ASABİ","AVİZE","BAHİS","BASİT",
"BEKÇİ","BESİN","BEŞİK","BEYİN","BİBER","BİDON","BİLET","BİLİM","BİLYE","BİREY","BUTİK","CAHİL","CAZİP","CEVİZ",
"CİLVE","CİMRİ","CİSİM","ÇEKİÇ","ÇELİK","ÇEŞİT","ÇEYİZ","ÇİÇEK","ÇİLEK","ÇİZGİ","DAİRE","DELİK","DEMİR","DERGİ",
"DEYİM","DİKEN","DİLEK","DİLİM","DİREK","DİVAN","DÖVİZ","EBEDİ","EKSİK","ELİPS","EMZİK","ESPRİ","EŞSİZ","ETKİN",
"ETNİK","EVRİM","EZELİ","FACİA","FAKİR","FEDAİ","FİDAN","FİDYE","FİGÜR","FİZİK","FOSİL","GAFİL","GEÇİT","GEDİK",
"GEYİK","GİRİŞ","GİZEM","GORİL","HACİM","HACİZ","HADİS","HAKİM","HATİM","HAZİN","HİCİV","HİLAL","HİSSE","İBARE",
"İBRET","İDDİA","İFADE","İHALE","İHBAR","İKRAM","İLAHİ","İLAVE","İMKAN","İNKAR","İNSAN","İPUCU","İRADE","İRONİ",
"İSLAM","İSPAT","İSYAN","İZZET","KABİN","KADİM","KAİDE","KATİP","KAVİS","KEFİL","KEMİK","KEŞİF","KİBAR","KİLİT",
"KİRİŞ","KİTAP","KLİŞE","KOMİK","KROKİ","KULİS","LİDER","LİKİT","LİMON","LİSAN","LİSTE","MADDİ","MERMİ","MESAİ",
"MEVKİ","MİDYE","MİLLİ","MİMAR","MİRAS","MİZAH","MİZAN","MOTİF","MUCİT","NAKİT","NARİN","NAZİK","NEHİR","NİKAH",
"NİMET","NİŞAN","NİYET","NİZAM","OPTİK","OTİZM","ÖNERİ","PARTİ","PASİF","PEŞİN","PİLAV","PİLOT","PİPET","PİYON",
"PİZZA","RAKİP","REJİM","RESİM","REZİL","RİTİM","RUTİN","SABİT","SEBEP","SEBİL","SEÇİM","SEDİR","SEFİR","SERGİ",
"SERİN","SEVGİ","SEZGİ","SİCİL","SİHİR","SİLAH","SİLGİ","SİMGE","SİNİR","SİPER","SİREN","SİVİL","SOSİS","ŞAHİT",
"ŞARKI","ŞEHİR","ŞEHİT","ŞERİT","ŞİFRE","ŞİRİN","TABİR","TAHİN","TAKSİ","TAMİR","TAYİN","TELİF","TEORİ","TEPSİ",
"TERİM","TERZİ","TESİS","TESTİ","TETİK","TİNER","TİTİZ","TRİKO","ÜNİTE","VAHŞİ","VAKİT","VARİL","VEKİL","VERGİ",
"VEZİR","VİRAJ","VİRÜS","VİTES","YEMİN","YETİM","YETKİ","YİĞİT","ZALİM","ZAMİR","ZARİF","ZEHİR","ZEMİN","ZİRVE"]
p = Tk()
p.title("Wordle")
p.geometry("1920x1080")

harfler = ["","","","",""]
labellar = ["","","","",""]
for i in range(5):
    labellar[i] = Label(p,width=2,font="Times 36 bold")
for i in range(5):
    harfler[i] = Entry(p,width=2,font="Times 36")
no = random.randint(0,228)
kelimem = Kelimeler[no]

def Cikis():
    p.destroy()

def KelimeKontrol():
    sayac1 = 0
    i = 0
    x1 = 700
    while(i<5):
        kontrol = harfler[i].get()
        if(kontrol == kelimem[i]):
            labellar[i].config(text=kontrol,font=("Times New Roman", 36), bg="Green")
            labellar[i].pack()
            labellar[i].place(x=x1, y=400)
            sayac1 += 1
        else:
            j=0
            sayac=0
            while(j<5):
                if(kontrol == kelimem[j]):
                    sayac += 1
                j += 1
            if(sayac > 0):
                labellar[i].config(text=kontrol, font=("Times New Roman", 36), bg="Yellow")
                labellar[i].pack()
                labellar[i].place(x=x1, y=400)
            else:
                labellar[i].config(text=kontrol, font=("Times New Roman", 36), bg="Red")
                labellar[i].pack()
                labellar[i].place(x=x1, y=400)
        harfler[i].delete(0,'end')
        i += 1
        x1 += 100
    if(sayac1 == 5):
        for i in range(5):
            harfler[i].destroy()
        Yazi1.config(text="TEBRİKLER",font="Times 48 bold italic")
        Yazi1.place(x=700,y=550)
        GirisButonu.destroy()

def Oyun():
    Yazi1.config(text="Lütfen kelimenizi giriniz:",font=("Times New Roman",24))
    Yazi1.place(x=700,y=200)
    x1 = 700
    for i in range(5):
        harfler[i].pack()
        harfler[i].place(x=x1,y=300)
        x1 +=100
    GirisButonu.config(text="ONAYLA",font=("Times New Roman",14),bg="Green",command=KelimeKontrol)
    GirisButonu.place(x=1200,y=310)

Yazi1 = Label(p,text="- WORDLE -",font="Times 48 bold italic")
Yazi1.pack()
Yazi1.place(x=720,y=300)
GirisButonu = Button(p,text="OYUNA BAŞLA",bg="Green",font=("Times New Roman",20),command=Oyun)
GirisButonu.pack()
GirisButonu.place(x=800,y=600)
p.mainloop()