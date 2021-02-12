#isimli parametreli fonk. ile 2 sayı çarpımı

sayi1 = int(input("birinci sayı: "))
sayi2 = int(input("ikinci sayı: "))

def carpım(a,b):
    print("iki sayının çarpımı : ",a*b)

carpım(a = sayi1,b = sayi2)
#isimsiz parametrede sıralama önemlidir, isimli p.'de sıra önemli değildir..
#isimli parametre kullanılacaksa tümüne isim verilmeli, yoksa hata alınır.
