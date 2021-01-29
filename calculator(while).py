############################
#                          # 
# While ile hesap makinesi #
#                          #
############################

#toplama 1, çıkarma 2, çarpma 3, bölme 4, çıkış 5

sayi1 = int(input("birinci sayı: "))
sayi2 = int(input("ikinci sayı: "))

while True:
    islem = input("işlem seçiniz: ")

    if(islem == "1"):
        print(sayi1 + sayi2)
    elif(islem == "2"):
        print(sayi1-sayi2)
    elif(islem == "3"):
        print(sayi1*sayi2)
    elif(islem == "4"):
        print(sayi1/sayi2)
    elif(islem == "5"):
        print("çıkış yapılıyor..")
        break
    else:
        print("hatalı tuşlama")
