class ogrenci():
    def __init__(self,ad,soyad,no,vize,final):
        self.ad = ad   # -----> ogrenci objesinin ozellikleri
        self.soyad = soyad
        self.no = no
        self.vize = vize
        self.final = final


    #notlar adlı metod
    def notlar(self):
        print("vize notu: {} final notu: {}".format(self.vize,self.final))


ogrenci1 = ogrenci("burcu","masat",245,85,79) #-->yeni nesne
ogrenci2 = ogrenci("ayşe","sayın",543,46,87)

print(ogrenci1.ad, ogrenci1.soyad)

ogrenci1.notlar() 





