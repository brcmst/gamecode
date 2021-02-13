class isci(): 
    def __init__(self,ad,soyad,maas,departman):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.departman = departman

    def cagri(self):
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nsoyisim: {}\nMaaş: {} \nDepartman: {}\n".format(self.ad,self.soyad,self.maas,self.departman))

    def bolum(self): #isci sınıfına bolum adlı metod tanımladık
        print("işçi bölümü..")



        

class isveren(isci):
    def __init__(self,ad,soyad,maas,departman,ek_gelir):
        super().__init__(ad,soyad,maas,departman)
        self.ek_gelir = ek_gelir

    def bolum(self):
        print("işveren bölümü..")#overriding : miras alan sınıfta tekrar metodu tanımladık.. eski metod iptal olur.

        

isveren1 = isveren("ali","tuna",4500,"müdür",500) 



print("işveren ad: {} \nişveren soyad: {} \nişveren maas: {} \nişveren departman: {} \nişveren ek gelir: {}".format(isveren1.ad,isveren1.soyad,isveren1.maas,isveren1.departman,isveren1.ek_gelir))

isveren1.bolum() #overriding sonucu
