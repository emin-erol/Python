def Fibonacci():
    a = 1
    b = 1
    yield a # a ve b değişkenlerini istenildiğinde kullanılacak şekilde yield ifadesini kullandık
    yield b
    while True:
        a,b = b,b+a # Fibonacci serisinin elemanları oluşturuluyor
        yield b # Oluşan eleman istenildiğinde çağırılacak şekilde yield ifadesi kullandık

for i in Fibonacci(): # yield b ifadesindeki fibonacci elemanı 100000 den büyük olmadığı sürece elemanları yazan döngü.
    if(i > 100000):
        break
    print(i)