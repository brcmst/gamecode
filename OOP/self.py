class kitap:
    tur = ""
    sayfa = 0
    isim = ""
    okudugum_sayfa = 0
    
    
    def sayı(self):  #class içinde fonk. yazarsak ilk parametreyi self yazmak zorundayız
                     #self ile class içindeki değişkeni kullanabiliriz
        kalan = self.sayfa - self.okudugum_sayfa
        print("kalan sayfa sayısı: ",self.sayfa)
        

kitap1 = kitap()       #nesne olusturduk..
kitap1.tur = "makale"
kitap1.isim = "modern bilim"
kitap1.sayfa = 250
kitap1.okudugum_sayfa = 50


print("kitap1 nesnesinin adı: ",kitap1.isim)
print("kitap1 nesnesinin türü: ",kitap1.tur)
print("kitap1 nesnesinin sayfa sayısı: ",kitap1.sayfa)
print("kitap1 nesnesinin okuduğum sayfa sayısı: ",kitap1.okudugum_sayfa)


kitap1.sayı() #  ------>  class içindeki fonk. cagrilisi
