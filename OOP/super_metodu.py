class isci(): 
    def __init__(self,ad,soyad,maas,departman):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.departman = departman

    def cagri(self):
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nsoyisim: {}\nMaaş: {} \nDepartman: {}\n".format(self.ad,self.soyad,self.maas,self.departman))



        
#isverene baska ek özellikler eklemek icin super() metodu kullanılır..
class isveren(isci):
    def __init__(self,ad,soyad,maas,departman,ek_gelir):
        super().__init__(ad,soyad,maas,departman) #böylece aynı özellikleri tekrar yazmaktan kurtuluruz.
        self.ek_gelir = ek_gelir #eklemek istediğimiz özelliği yazdık

        

isveren1 = isveren("ali","tuna",4500,"müdür",500) #ekledigimiz özellige deger atadık



print("işveren ad: {} \nişveren soyad: {} \nişveren maas: {} \nişveren departman: {} \nişveren ek gelir: {}".format(isveren1.ad,isveren1.soyad,isveren1.maas,isveren1.departman,isveren1.ek_gelir))
