class Kareler():
    def __init__(self,maksimum):
        self.maksimum = maksimum
        self.sayim = 0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.sayim <= self.maksimum):
            sonuc = self.sayim ** 2
            self.sayim += 1
            return sonuc
        else:
            self.sayim = 0
            raise StopIteration

ornek1 = Kareler(8)
itr = iter(ornek1)
while True:
    try:
        print(next(itr))
    except StopIteration:
        print("Yazma işlemi bitti.")
        break