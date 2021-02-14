class isci():
    def __init__(self, ad, soyad, maas, departman):
        self.__ad = ad  #encapsulation icin ismin başına "__" koyulur, böylece artık private olur.
        self.__soyad = soyad                          #artık dışarıdan değişirilemez ve ulaşılamaz.
        self.__maas = maas
        self.departman = departman

    def getAd(self):  #private veriye ulaşmak için get metodu kullanılır ---->1
        return self.__ad
    def getSoyad(self):
        return self.__soyad
    def getMaas(self):
        return self.__maas


    def setMaas(self, güncel_maas):  #private veriyi degistirmek için set metodu kullanılır --->2
        self.__maas = güncel_maas
        

        

isci1 = isci("burcu","masat",4500,"bilişim") 

print("ad: {} \nsoyad: {} \nmaaş: {} \ndepartman: {}".format(isci1.getAd(),isci1.getSoyad(),isci1.getMaas(),isci1.departman))
#ad yerine getAd(), soyad yerine getSoyad(), maas yerine getMaas() cağırdık.. ------>1

isci1.setMaas(5000) #maasi güncelledik
print("maaş güncellendi:",isci1.getMaas()) #maas verisine ulastık

