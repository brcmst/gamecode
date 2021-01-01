print("""
*************************************

ATM Makinesine Hoşgeldiniz.

işlemler;

1. Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan çıkmak için 'q' ya basınız..

*************************************
""")
bakiye = 2345


while True:
    islem = input("işlem giriniz: ")
    
    if(islem == "1"):
        print("bakiyeniz: ",bakiye)

    elif(islem == "2"):
        print("para yatırmak istediğiniz miktar ve hesap no giriniz..")
        islem2 = int(input("miktar: "))
        islem21 = input("hesap no: ")
        print("para gönderiliyor..gönderildi")
        x = bakiye-islem2
        print("kalan paranız: ",x)
        
    elif(islem == "3"):
        islem3 = int(input("çekmek istediğiniz miktar: "))
        xx = bakiye-islem3 
        print("kalan paranız: ",xx)

    elif(islem == "q"):
        print("sistemden çıkılıyor..")
        break

    else:
        print("geçersiz islem,tekrar deneyin..")
        
