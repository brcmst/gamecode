class isci(): #--> isci adlı sınıf olusturduk
    def __init__(self,ad,soyad,maas,departman):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.departman = departman


class isveren(isci): #---> isci sınıfından miras aldık
    pass #--> sonra tanımlayacagımızı belirttik (yoksa hata alırız)

isveren1 = isveren("ali","tuna",4500,"müdür") # --->nesne olusturduk


print("işveren ad: {} \nişveren soyad: {}".format(isveren1.ad,isveren1.soyad))
#isveren sınıfının özelliklerinin otomatik tanımlandıgını görmüs olduk
#kalıtımda bulunun özellikler tüm sınıflar ortak olmalı!
