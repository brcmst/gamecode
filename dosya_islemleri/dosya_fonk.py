#acılan dosyalar mutlaka kapatılmalı..python da bulunan blok sayesinde işimiz bitince dosya otomatik kapanıyor
#-----blok------
with open("oku.txt","r",encoding = "utf-8") as f:
    for i in f:
        print(i) #--->bloğun dışına çıkılınca dosya otomatik kapanır..





#seek fonksiyonu: imlec istenen bayt konumuna gönderilebilir
#tell fonksiyonu: dosya imlecinin hangi baytta oldugunu söyler
with open("oku.txt","r",encoding = "utf-8") as f:
    print(f.tell())#----dosya imlecinin konumu söyler


    

with open("oku.txt","r",encoding = "utf-8") as f:
    print(f.tell())
    f.seek(10)
    print(f.tell())#----dosya imlecinin yeri degisir


    
    


with open("oku.txt","r",encoding = "utf-8") as f:
    f.seek(3)
    oku = f.read(14) #3'ten başlayarak 11 karakter okur
    print(oku)
