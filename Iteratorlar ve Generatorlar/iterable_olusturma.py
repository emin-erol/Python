class Kumanda():
    def __init__(self,kanalListesi):
        self.kanalListesi = kanalListesi
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index < len(self.kanalListesi):
            return self.kanalListesi[self.index]
        else:
            self.index = -1
            raise StopIteration

kumanda = Kumanda(["aTV","Fox TV","Show TV","Kanal D"])
iterator = iter(kumanda)
while True:
    try:
        print(next(kumanda))
    except StopIteration:
        print("Bütün kanallar gezildi.")
        break