import random
import time

isim = input("Merhaba! İsminiz nedir ?")
print("Sayı tahmin oyununa hoşgeldin")

print("Şimdi 1-50 arası sayı tahmin et",isim)



secilen = random.randint(1,50) #1-50 arası random sayı üretir
can = 6

while True:
    deger = int(input("Tahmin ettiğin sayı: "))

    if(deger < secilen):
        print("Bakalım bilebilecek misin, sorgulanıyor..")
        
        time.sleep(1)
        print("Bilemedin! Daha büyük bir sayı söyle!!")

        can -= 1

    elif(deger > secilen):
        print("Acaba? sorgulanıyor..")
        
        time.sleep(1)
        print("Bilemedin! Daha küçük bir sayı söyle!!")

        can -= 1

    else:
        time.sleep(1)
        print("Tebriklerr!!!! Kazandın ",isim)
        break
    if(can == 0):
        print("Kazanamadın...")
        print("Doğru tahmin: ",secilen)
        break

        
        

        
        
