from PIL import Image,ImageFilter

image = Image.open("doga.jpg") # pythonda resmi açar
image.save("doga2.jpg") # resmi kaydeder
image.rotate(180).save("doga3.jpg") # resmi döndürür
image.convert(mode = "L").save("doga4.jpg") # resmi siyah beyaza çevirir
boyut = (800,500)
# image.thumbnail(boyut) resmin boyutunu değiştirir
image.save("doga5.jpg")
image.filter(ImageFilter.GaussianBlur(2)).save("doga6.jpg") # resmi buğulaştırır
alan = (517,427,1128,697)
image.crop(alan).save("doga7.jpg")

