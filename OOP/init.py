class palet():

    #init ilkleme için kullanılır, nesne üretilirken çalışan ilk fonksiyondur.
    def __init__(self,sayi = 0, renk = "secilmedi"): #varsayılan degerler atadık,ilkleme işlemi sırasında..
        self.sayi = sayi
        self.renk = renk
        print("yapıcı fonksiyon yani init çalıştı..")
        

boya1 = palet() #nesne olusturduk ------------> deger atamadıgımız için varsayılanlar çıktıdır
#nesne olusturdugumuz gibi init fonk. calisir..
print("boya1 nesnesinin boya sayısı",boya1.sayi)
print("boya1 nesnesinin boya rengi",boya1.renk)


boya2 = palet(5,"mor") #nesne olustu, degerler sırayla atandı
print("boya2 nesnesinin boya sayısı",boya2.sayi)
print("boya2 nesnesinin boya rengi",boya2.renk)

