#listedeki stringlerden sadece rakam içerenleri ekrana yazdır...

liste = ["ali","canan","334","4h4h4","12121"]

for i in liste:
    try:
        degisken = int(i)
        print(i)
    
    except ValueError:
        print("hata")
    
