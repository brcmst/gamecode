#parametreli fonk. ile isim ile merhaba ...isim.. yazdır

isim = input("isim: ") #kullanıcıdan alınan deger

def myFonk(a):         #fonksiyon içinde belirlenen argüman adı önemsizdir
    print("merhaba ",a)
    
myFonk(isim)           #fonksiyonu kullanıcıdan aldığımız değeri parametre olarak gönderdik

