def carpimTablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} * {} = {}".format(i,j,i*j)

gnr = carpimTablosu()
itr = iter(gnr)
while True:
    try:
        print(next(itr))
    except StopIteration:
        print("TABLO OLUSTURULDU !!!")
        break