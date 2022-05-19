class Dosya:
    def __init__(self):
        with open("Metin.txt", "r", encoding="utf-8") as file:
            DosyaIcerigi = file.read()
            kelimeler = DosyaIcerigi.split() # bütün metni kelime kelime bölerek kelimeler listesine atıyoruz
            self.SadeKelimeler = []
            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ") # tuttuğumuz kelimede olmasını istemediğimiz karakterleri çıkarıyoruz
                i = i.strip(".")
                i = i.strip(",")
                i = i.strip("(")
                i = i.strip(")")
                i = i.strip("?")
                self.SadeKelimeler.append(i) # istenmeyen karakterler çıkarıldıktan sonra her kelime listeye ekleniyor
    def TumKelimeler(self): # Her kelimeden birer tane almak için kelimeler kümesi oluşturuluyor.
        KelimelerKumesi = set()
        for i in self.SadeKelimeler:
            KelimelerKumesi.add(i)
        print("- TÜM KELİMELER -")
        for i in KelimelerKumesi:
            print("  ",i,"\n*************")
    def KelimeFrekansi(self): # Kelimenin kullanım sıklığı bulunuyor.
        KelimeSozlugu = dict()
        for i in self.SadeKelimeler:
            if(i in KelimeSozlugu):
                KelimeSozlugu[i] += 1
            else:
                KelimeSozlugu[i] = 1
        for kelime,adet in KelimeSozlugu.items():
            print("{} kelimesinden {} adet kullanılmıştır.".format(kelime,adet))

dosya1 = Dosya()
dosya1.KelimeFrekansi()