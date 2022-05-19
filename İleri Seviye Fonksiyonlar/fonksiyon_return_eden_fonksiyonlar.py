def AnaFonksiyon(IslemTuru): # İçinde toplama ve çarpma işlemlerini uygulayabilen fonksiyonlara sahip ana fonksiyon
    def Toplama(*args): # İçine gönderilen değerleri toplayıp return eden fonksiyon
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def Carpim(*args): # İçine gönderilen değerleri çarpıp return eden fonksiyon
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if(IslemTuru == "+"):
        return Toplama
    else:                      # IslemTuru'nun değerine göre hanagi fonksiyonun return edileceğini bulma
        return Carpim

fonk1 = AnaFonksiyon("+") # Toplama olarak girilen islem türü ana fonksiyondaki toplama fonksiyonunu kullanır
print(fonk1(1,2,3,4,5,6,7))
fonk2 = AnaFonksiyon("*") # Carpim olarak girilen islem türü ana fonksiyondaki carpim fonksiyonunu kullanır
print(fonk2(5,4,3,2,1))