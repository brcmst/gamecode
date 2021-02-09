########################################
# Math modülündeki hazır fonksiyonları #
# ile gelişmiş bir hesap makinesi...   #
########################################


print("""************************************************************
işlemler: toplama - cikarma - bölme - carpma -
log - log10 - kombinasyon - cos - sin - tan -
faktoriyel - mod - karekok - üs
*************************************************************""")



import math


while True:

    x = int(input("sayı:"))

    islem = input("yapmak istediğiniz işlem: ")
    
    if(islem == "log10"):
        print(math.log10(x))
    elif(islem == "log"):
        y = int(input("sayı:"))
        print(math.log(x,y))
    elif(islem == "kombinasyon"):
        y = int(input("sayı:"))
        print(math.comb(x,y))
    elif(islem == "cos"):
        print(math.cos(x))
    elif(islem == "sin"):
        print(math.sin(x))
    elif(islem == "tan"):
        print(math.tan(x))
    elif(islem == "faktoriyel"):
        print(math.factorial(x))
    elif(islem == "mod"):
        y = int(input("sayı:"))
        print(math.fmod(x,y))
    elif(islem == "karekok"):
        print(math.sqrt(x))
    elif(islem == "üs"):
        y = int(input("sayı:"))
        print(math.pow(x,y))

    elif(islem == "toplama"):
        y = int(input("sayı:"))
        print(x+y)
    elif(islem == "cikarma"):
        y = int(input("sayı:"))
        print(x-y)
    elif(islem == "carpma"):
        y = int(input("sayı:"))
        print(x*y)
    elif(islem == "bolme"):
        y = int(input("sayı:"))
        if(y == 0):
            print("sıfıra bölünmez..hata")
            break
        print(x/y)
        

   
    if(islem == "cikis"):
        print("çıkış yapılıyor...")
        break
    

    
    
