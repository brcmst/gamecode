# decorator , fazla kod yazmayı onler

# asagıdaki 2 fonk ne kadar surdugunu ogrenmek icin import time deriz
import time

def kare_hesap(sayı):
    sonuc = list()
    basla = time.time()
    
    for i in sayı:
        sonuc.append(i ** 2)

    bitir = time.time()

    print("kare al fonk suresi (sn) =", str(bitir-basla))
    return sonuc

def kup_hesap(sayı):
    sonuc = list()
    basla2 = time.time()
    for i in sayı:
        sonuc.append(i ** 3)
    bitir2 = time.time()
    print("kare al fonk suresi (sn) =", str(bitir2-basla2))
    return sonuc
    

kare_hesap(range(150000))
kup_hesap(range(150000))

# aslında sure hesaplarken kod tekrarı yapmıs olduk
# ayrıca fonk asıl amacı sure hesabı degil..
print("***********************************")



# simdi decorator fonk ile zaman hesabı yapalım
print("decorator ile fonk zaman hesabı")

#ekstra zaman hesapla fonk yazıldı
def zaman_hesap(func):
    def wrapper(sayı):
        basla = time.time()
        sonuc = func(sayılar)
        bitir = time.time()

        print(func.__name__ + " " + str(bitir-basla) + "sn sürdü.")
        return sonuc
    return wrapper
    
@zaman_hesap    #bu sekilde decoratoru kullanabiliriz
def kare_hesap2(sayı):
    sonuc = list()
    for i in sayı:
        sonuc.append(i ** 2)
    return sonuc


@zaman_hesap
def kup_hesap2(sayı):
    sonuc = list()
    for i in sayı:
        sonuc.append(i ** 3)
    return sonuc
    

kare_hesap(range(150000))
kup_hesap(range(150000))
























