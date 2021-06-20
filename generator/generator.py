# generator bellekte yer kaplamaz

#generator kullanmadan fonksiyon
def kare_al():
    sonuc = []

    for i in range(1,6):
        sonuc.append(i ** 2)
    return sonuc

print(kare_al()) #cok daha fazla sayı olsa bellegi isgal etmis olacaktı

print("*****************")



#generator ile fonksiyon
print("generator")

def kare_al2():
    for i in range(1,6):
        yield i ** 2

generator = kare_al2()  #aslında obje olusturduk
print(generator)
# yield dedigimiz icin aslında generator objemizde bir deger henuz uretilmedi
# bu degerler biz o degere erismek istedigimizde uretilir sadece

iterator = iter(generator) # generator objeden iterator obje urettik
print(next(iterator)) #generatorun bir sonraki degerine erismek icin
print(next(iterator))
print(next(iterator))


print("*****************")
print("list comp generatore cevirme")

liste3 = [i * 3 for i in range(5)]
print(liste3)     #list comp
#simdi bunu generatore cevirelim

generator2 = (i * 3 for i in range(5))  #köseli parantez yerine normal parantez kullandık
print(generator2)
iterator2 = iter(generator2)
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))

#sadece deger basıcaksak bellekte yer kaplamaması icin kullanılması mantıklı






