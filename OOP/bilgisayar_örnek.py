#
#bilgisayar sınıfı
#

class bilgisayar():
    def __init__(self,durum = "kapalı",ses = 0,dosyalar = ["bilgisayarım","belgelerim"]):
        print("bilgisayar oluşturuluyor......")
        self.durum = durum
        self.ses = ses
        self.dosyalar = dosyalar


    def pcAc(self):
        print("bilgisayar açıldı....")
        self.durum = "açık"

    def pcKapat(self):
        print("bilgisayar kapandı....")
        self.durum = "kapalı"


    def sesAyar(self):
        while True:
            deger = input("ses artırmak için '+', azaltmak için '-', çıkış için 'e' basınız.")
            if(deger == "+"):
                if(self.ses >= 0 or self.ses < 100):
                    self.ses += 1
                    print("ses:",self.ses)

            if(deger == "-"):
                if(self.ses <= 100 or self.ses >0):
                    self.ses -= 1
                    print("ses:",self.ses)

            elif(deger == "e"):
                print("ses ayarından çıkılıyor....")
                break

            else:
                print("mevcut ses:",self.ses)


    def dosyaEkle(self,y_dosya):
        print("dosya eklendi.",y_dosya)
        self.dosyalar.append(y_dosya)
        

    def dosyaSil(self,s_dosya):
        print("dosya silindi.")
        self.dosyalar.remove(s_dosya)


            
comp = bilgisayar()

print("""
yapmak istediğiniz işlemi seçin:
1: bilgisayarı aç

2: bilgisayarı kapat

3: ses ayarı

4: çıkış

5: dosya oluştur/sil

""")

while True:
    islem = int(input("işlem seçiniz:"))

    if(islem == 1):
        if(comp.durum == "açık"):
            print("bilgisayar zaten açık..")
        comp.pcAc()

    elif(islem == 2):
        if(comp.durum == "kapalı"):
            print("bilgisayar zaten kapalı..")
        comp.pcKapat()

    elif(islem == 3):
        comp.sesAyar()

    elif(islem == 4):
        print("çıkış yapılıyor.....")
        break

    elif(islem == 5):
        d_durumu = input("dosya eklemek için 'yeni', silmek için 'sil' yazınız.")
        if(d_durumu == "yeni"):
            ekle = input("dosya adı giriniz:")
            comp.dosyaEkle(ekle)

        elif(d_durumu == "sil"):
            print("silmek istediğiniz dosya adını girin.",comp.dosyalar)
            silme = input()
            comp.dosyaSil(silme)
        print("dosyalar:",comp.dosyalar)

    else:
        print("geçersiz işlem.....")
        

        
    


















    

        
        
